#!/usr/bin/env python3
"""Offline catalog maintenance. Python 3.10+, standard library only."""
import argparse
import csv
import io
import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]

def normalize_url(url):
    u = urlsplit(url.strip())
    if u.scheme not in ('http', 'https') or u.hostname not in ('x.com', 'www.x.com', 'mobile.x.com', 'twitter.com', 'www.twitter.com', 'mobile.twitter.com') or u.username or u.password or u.port:
        raise ValueError('Expected a direct X/Twitter post URL')
    m = re.fullmatch(r'/(?:([A-Za-z0-9_]{1,15})/status|i/web/status|i/status)/([0-9]+)(?:/(?:photo|video)/[0-9]+)?/?', u.path)
    if not m:
        raise ValueError('Expected a post, not a profile, short URL or analytics URL')
    author, pid = m.groups()
    return pid, f'https://x.com/{author}/status/{pid}' if author else f'https://x.com/i/web/status/{pid}'

def read(name):
    return json.loads((ROOT / 'data' / name).read_text(encoding='utf-8'))

def validate():
    cases, sources, categories = read('cases.json'), read('sources.json'), read('categories.json')
    def unique(rows, key):
        values = [r[key] for r in rows]
        assert len(values) == len(set(values)), f'Duplicate {key}'
    unique(cases, 'id'); unique(sources, 'post_id'); unique(categories, 'id')
    sm = {s['post_id']: s for s in sources}
    cm = {c['id']: c for c in cases}
    cats = {c['id'] for c in categories}
    active_categories = {c['category'] for c in cases}
    for category in categories:
        if category['id'] in active_categories:
            assert category.get('emoji'), f'Missing category emoji: {category["id"]}'
            assert all(category.get('description', {}).get(lang, '').strip() for lang in ('en', 'zh')), f'Missing category description: {category["id"]}'
            cover = category.get('cover', {})
            assert cover.get('case_id') in cm, f'Missing category cover: {category["id"]}'
            assert cm[cover['case_id']]['category'] == category['id'], 'Cover must belong to its category'
            assert type(cover.get('height')) is int and 80 <= cover['height'] <= 180, 'Cover height must be 80–180 pixels'
    for s in sources:
        assert normalize_url(s['url'])[0] == s['post_id'], 'Post ID mismatch'
        assert s['status'] in ('pending', 'accepted', 'rejected', 'duplicate', 'unavailable')
        assert s['reason'].strip()
        for key in ('first_seen_at', 'last_checked_at'):
            date.fromisoformat(s[key])
        if s['status'] == 'accepted':
            assert s['case_id'] in cm
            assert s['post_id'] in cm[s['case_id']]['source_ids']
        if s['case_id'] is not None:
            assert s['case_id'] in cm
    owned = set()
    for c in cases:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', c['id'])
        assert c['category'] in cats
        assert 'reproduction' not in c, 'Reproduction status is not part of a curated case'
        for field in ('title', 'summary', 'workflow', 'limitations'):
            assert all(c[field][lang].strip() for lang in ('en', 'zh')), f'Missing translation: {c["id"]}'
        assert c['model'] == 'gpt-6-astra'
        assert c['model_evidence'] in ('author-stated', 'visible-model-label')
        assert c['primary_source_id'] in c['source_ids']
        assert c['source_ids'] and len(set(c['source_ids'])) == len(c['source_ids'])
        for sid in c['source_ids']:
            assert sid not in owned, 'One post cannot belong to multiple cases'
            owned.add(sid)
            assert sm[sid]['status'] == 'accepted' and sm[sid]['case_id'] == c['id']
            assert sm[sid]['verification'] == 'x-post-read'
        assert c.get('prompt'), 'A public prompt is required'
        assert c['prompt']['availability'] == 'public', 'A public prompt is required'
        assert c['prompt']['source_id'] in c['source_ids'] and c['prompt']['text'].strip()
        assert c['prompt']['display'] in ('full', 'excerpt')
        date.fromisoformat(c['prompt']['verified_at'])
        assert c['preview']['source_id'] in c['source_ids']
        assert all(c['preview']['alt'][lang].strip() for lang in ('en','zh'))
        preview = c['preview']['url']
        if not preview.startswith('https://'):
            assert preview.startswith('assets/previews/') and '..' not in Path(preview).parts
            assert (ROOT / preview).is_file(), 'Missing preview file'
    notes = read('case-notes.json')
    unique(notes, 'case_id')
    for note in notes:
        assert note['case_id'] in cm, 'Unknown case in editorial notes'
        assert note['source_ids'] and set(note['source_ids']).issubset(cm[note['case_id']]['source_ids']), 'Editorial sources must belong to the case'
        for section, keys in [('prerequisites', ('software', 'assets', 'services', 'access')),
                              ('analysis', ('goal', 'constraints', 'delivery', 'acceptance', 'lesson'))]:
            for key in keys:
                assert all(note.get(section, {}).get(key, {}).get(lang, '').strip() for lang in ('en', 'zh')), f'Missing bilingual editorial field: {note["case_id"]}/{section}/{key}'
    return cases, sources, categories

def render():
    cases, sources, categories = validate()
    notes = {note['case_id']: note for note in read('case-notes.json')}
    paths = read('learning-paths.json')
    case_map = {c['id']: c for c in cases}
    for entry in paths:
        assert entry['case_id'] in case_map, 'Unknown learning-path case'
        for lang in ('en', 'zh'):
            assert entry['goal'][lang].strip() and entry['reason'][lang].strip()
            suffix = '.zh-CN' if lang == 'zh' else ''
            assert (ROOT / f'docs/guides/{entry["guide"]}{suffix}.md').is_file(), 'Missing learning guide'
    sm = {s['post_id']: s for s in sources}
    active = [cat for cat in categories if any(c['category'] == cat['id'] for c in cases)]
    files = {}
    def esc(value):
        return html.escape(str(value), quote=True)
    def image_path(c, nested=False):
        url=c['preview']['url']
        return '../'*int(nested)+url if nested and not url.startswith('https://') else url
    for lang, filename in [('en', 'README.md'), ('zh', 'README.zh-CN.md')]:
        zh = lang == 'zh'
        gallery = 'docs/gallery.zh-CN.md' if zh else 'docs/gallery.md'
        label = lambda en, cn: cn if zh else en
        suffix = '.zh-CN' if zh else ''
        def category_path(category_id):
            return f'docs/categories/{category_id}{suffix}.md'
        def case_link(c):
            return f'{category_path(c["category"])}#{c["id"]}'
        def prompt_label(c):
            return label('Full prompt', '完整提示词') if c['prompt']['display'] == 'full' else label('Prompt excerpt', '提示词摘录')
        def case_lines(c, depth):
            source=sm[c['primary_source_id']];prompt=sm[c['prompt']['source_id']]
            result = ['',f'<a id="{c["id"]}"></a>', '',f'### {c["title"][lang]}','',
              f'**{prompt_label(c)}** · [{label("Original prompt", "提示词原帖")}]({prompt["url"]})', '',
              f'[![{c["preview"]["alt"][lang]}]({image_path(c,depth)})]({source["url"]})','',c['summary'][lang],'',
              f'**{label("Creator", "作者")}**: [@{source["author"]}]({source["url"]}) · {source["published_date"]}<br>',
              f'**{label("Tools & techniques", "工具与技术")}**: {", ".join(c["tags"])}','',
              '**'+label('How it works','创作方法')+'**','',c['workflow'][lang],'',
              '**'+label('What to know','值得注意')+'**','',c['limitations'][lang],'',
              '**'+label('Prompt','提示词')+'**','']
            if c['prompt']['display']=='full':
                result += ['```text',c['prompt']['text'],'```','']
            else:
                result += ['> '+c['prompt']['text'],'',label('Opening excerpt; the author’s complete prompt is linked below.','以上为开头摘录，完整提示词见下方作者原帖。'),'']
            result += [f'↗ [{label("Read the original prompt", "查看作者完整提示词")}]({prompt["url"]}) · [{label("Watch the demo", "观看演示")}]({source["url"]})','']
            if c['id'] in notes:
                note = notes[c['id']]
                result += ['#### '+label('Before you try it', '使用前提'), '',
                  label('Based on the material already recorded in this catalog. Missing information is not evidence that a dependency or asset is unnecessary.', '依据本目录已收录资料整理；信息未说明，不代表不需要相关依赖或素材。'), '',
                  '| '+label('Item | Recorded information', '项目 | 已知信息与缺口')+' |', '| --- | --- |']
                for key, en, cn in [('software', 'Software & environment', '软件与环境'), ('assets', 'Input assets', '输入素材'), ('services', 'Services & accounts', '服务与账号'), ('access', 'Code & demo access', '源码与演示入口')]:
                    value = note['prerequisites'][key][lang].replace('|', '\\|').replace('\n', '<br>')
                    result.append(f'| {label(en, cn)} | {value} |')
                result += ['', '#### '+label('Prompt breakdown — editorial analysis', '提示词拆解 · 项目分析'), '',
                  label('The creator’s prompt is above. The analysis and suggested checks below are project commentary, not the creator’s wording or an independently tested result.', '作者提示词原文见上方。以下拆解和验收建议是项目分析，不是作者原文，也不是独立实测结果。'), '']
                for key, en, cn in [('goal', 'Goal', '目标'), ('constraints', 'Constraints', '约束'), ('delivery', 'Deliverable', '交付'), ('acceptance', 'Suggested checks', '验收建议'), ('lesson', 'Takeaway', '可借鉴之处')]:
                    result += [f'**{label(en, cn)}**：{note["analysis"][key][lang]}', '']
                result += [label('Recorded sources: ', '所依据的已收录来源：') + ' · '.join(f'[@{sm[sid]["author"]} · {sid}]({sm[sid]["url"]})' for sid in note['source_ids']), '']
            return result
        lines = ['<div align="center">', '', '# 📚 '+label('Awesome GPT-6 Astra — Use Cases & Prompts', 'Awesome GPT-6 Astra — 实战案例与提示词'), '',
          '**'+label('Curated GPT-6 Astra use cases. See the result. Explore the prompt. Build your own.', 'GPT-6 Astra 实战案例精选 · 看作品，读提示词，动手创造。')+'**', '',
          '[English](README.md) · [简体中文](README.zh-CN.md)', '',
          f'**{len(cases)} {label("cases", "个案例")} · {len(active)} {label("categories", "个分类")}**', '', '</div>', '',
          label('Explore GPT-6 Astra use cases, prompt examples and community demos for app and website development, UI design, 3D creation, video storytelling, computer use, engineering and games. Each case connects the result to its creator’s public prompt, tools, workflow and original source.', 'GPT-6 Astra 实战案例与提示词合集，涵盖应用与网站开发、UI 设计、三维创作、视频叙事、电脑操作与自动化、工程原型和游戏开发。每个案例整理作品展示、作者公开提示词、工具与技术、创作方法及原始来源，方便查找应用示例与学习思路。'), '',
          f'📖 [{label("Browse all cases", "浏览全部案例")}]({gallery}) · 🧾 [{label("Collection index", "收录索引")}](docs/collection-index.md) · ✨ [{label("Latest additions", "最新收录")}]({gallery}#latest) · ➕ [{label("Submit a case", "推荐案例")}](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/issues/new?template=submit-case.md)', '',
          '## '+label('Start here', '新手从这里开始'), '',
          label('Three reading paths selected for clear learning goals. These are source-based recommendations, not difficulty ratings or independently reproduced results.', '按学习目标精选的三个阅读入口。选择依据为已收录资料，不代表难度评级或独立复现结果。'), '',
          '| '+label('Your goal | Start with | Prompt | Why this case', '你的目标 | 推荐入口 | 提示词 | 选择理由')+' |', '| --- | --- | --- | --- |']
        for entry in paths:
            c = case_map[entry['case_id']]
            lines.append(f'| {entry["goal"][lang]} | [{c["title"][lang]}]({case_link(c)}) | {prompt_label(c)} | {entry["reason"][lang]} |')
        suffix = '.zh-CN' if zh else ''
        lines += ['', f'📘 [{label("Interactive web & 3D guide", "交互网页与三维创作指南")}](docs/guides/web-3d{suffix}.md) · 🎮 [{label("Game prompt guide", "游戏提示词指南")}](docs/guides/game-prompts{suffix}.md)', '',
          '### '+label('Case breakdowns', '案例深读'), '',
          label('Read the available prerequisites and our analysis of goals, constraints, delivery and acceptance checks:', '查看使用前提，以及目标、约束、交付与验收要求的逐项分析：'), '']
        for cid in notes:
            c = case_map[cid]
            lines.append(f'- [{c["title"][lang]}]({case_link(c)})')
        lines += ['', '## 🖼️ '+label('Case Album', '案例图册'), '', '<table>']
        for offset in range(0,len(active),3):
            lines.append('<tr>')
            for cat in active[offset:offset+3]:
                selected=[c for c in cases if c['category']==cat['id']]
                cover=case_map[cat['cover']['case_id']]
                link=category_path(cat['id'])
                # Height-only sizing preserves the original aspect ratio on GitHub.
                image_size = f'height="{cat["cover"]["height"]}"'
                lines += ['<td width="33%" align="center" valign="top">',
                  f'<h3>{cat["emoji"]} {esc(cat[lang])}</h3>',
                  f'<p>{len(selected)} {label("case" if len(selected) == 1 else "cases", "个案例")}</p>',
                  f'<a href="{link}"><img src="{esc(image_path(cover))}" alt="{esc(cover["preview"]["alt"][lang])}" {image_size}></a>',
                  f'<p>{esc(cat["description"][lang])}</p>',
                  f'<p><a href="{link}"><b>{label("View Cases →", "查看案例 →")}</b></a></p>', '</td>']
            lines.append('</tr>')
        lines += ['</table>', '', '## ✨ '+label('Latest Additions', '最新收录'), '',
          '| '+label('Case | Category | Prompt | Creator', '案例 | 分类 | 提示词 | 作者')+' |', '| --- | --- | --- | --- |']
        for c in list(reversed(cases))[:6]:
            cat=next(x for x in active if x['id']==c['category']);s=sm[c['primary_source_id']]
            lines.append(f'| [{c["title"][lang]}]({case_link(c)}) | {cat["emoji"]} {cat[lang]} | {prompt_label(c)} | [@{s["author"]}]({s["url"]}) |')
        lines += ['', '<a id="all-cases"></a>', '', '## '+label('All GPT-6 Astra examples by category', '按分类查找 GPT-6 Astra 案例'), '',
          label('Choose an example to read its workflow, limitations and public prompt. Tool names describe the collected work; they are not a list of required integrations.', '点击案例查看创作方法、注意事项和公开提示词。工具名称来自收录作品，不代表模型必须搭配这些工具使用。'), '']
        for cat in active:
            lines += ['### '+cat['emoji']+' '+cat[lang], '', f'[{label("Open category", "打开分类页面")}]({category_path(cat["id"])})', '']
            for c in cases:
                if c['category'] == cat['id']:
                    lines.append(f'- [{c["title"][lang]}]({case_link(c)}) — **{prompt_label(c)}** · '+', '.join(c['tags']))
            lines.append('')
        lines += ['## '+label('Using this GPT-6 Astra prompt collection', '如何使用这份 GPT-6 Astra 提示词合集'), '',
          label('1. Pick a category and open a case that matches what you want to build.\n2. Read the workflow and limitations, then follow the original demo and prompt links. Some entries show an excerpt; the complete prompt remains in the creator’s post.\n3. Adapt the prompt to your own assets, tools and constraints. Results can vary; this collection does not claim every example has been independently reproduced.', '1. 选择与你的目标相关的分类，打开具体案例。\n2. 阅读创作方法和注意事项，再访问作品演示与提示词原帖。部分案例仅展示摘录，完整提示词需查看作者原帖。\n3. 根据自己的素材、工具和需求调整提示词。实际效果可能不同，本合集不声称所有案例均经过独立复现。'), '',
          '## '+label('Frequently asked questions', '常见问题'), '',
          '### '+label('Where can I find GPT-6 Astra prompt examples?', '在哪里查看 GPT-6 Astra 提示词示例？'), '',
          label(f'Open the [full case gallery]({gallery}). Every curated entry links to a public prompt and its creator’s original result, with tools and a short workflow summary.', f'打开[完整案例图册]({gallery})。每个正式收录案例都附有公开提示词和作者作品原帖链接，同时整理工具与简要创作流程。'), '',
          '### '+label('Is this an official project or a benchmark?', '这是官方项目或性能评测吗？'), '',
          label('No. Awesome GPT-6 Astra is an independent community collection. Model attribution follows the recorded source evidence, such as the creator’s statement or a visible model label. Demos illustrate individual projects, not controlled benchmark results.', '不是。Awesome GPT-6 Astra 是独立社区整理项目。模型归属依据记录的来源证据，例如作者自述或可见模型标签；演示展示的是具体作品，不是受控性能评测。'), '',
          '### '+label('Can I reuse the prompts and preview images?', '可以复用提示词和预览图吗？'), '',
          label('Referenced prompts, works and previews belong to their creators. Check the original source and its terms before reuse; the repository’s MIT license covers original project code and writing.', '引用提示词、作品和预览图的权利归原作者所有，复用前请查看原始来源与相应条款；仓库 MIT 许可适用于项目原创代码和文字。'), '',
          '## 🤝 '+label('Contribute', '参与共建'), '',
          label('Found something worth trying? Share the result and its public prompt through an issue or pull request. See the [contribution guide](CONTRIBUTING.md).', '发现值得尝试的作品？欢迎通过 Issue 或 PR 分享成果与公开提示词，详见[贡献指南](CONTRIBUTING.md)。'), '',
          '## License', '',
          label('Original project code and writing: [MIT](LICENSE). Referenced works, prompts and previews belong to their respective creators. This is an independent community project.', '项目原创代码与文字采用 [MIT](LICENSE) 许可。引用作品、提示词与预览图的权利归各自作者所有。本项目为独立社区整理。'), '']
        files[filename]='\n'.join(lines)
        lines=['# '+label('📖 GPT-6 Astra Use Cases & Prompt Examples — Full Gallery','📖 GPT-6 Astra 实战案例与提示词 · 完整图册'), '',
          '[English](gallery.md) · [简体中文](gallery.zh-CN.md) · ['+label('Home','返回首页')+'](../'+filename+')', '',
          label('Browse community examples with result previews, tools, workflows, limitations and public prompt sources. Entries marked as excerpts link to the creator’s complete prompt. This independent collection records source claims and does not guarantee reproduction.', '浏览社区实战案例，查看作品预览、工具、创作方法、注意事项与公开提示词来源。标为摘录的条目提供作者完整提示词链接。本独立合集记录来源信息，不保证复现效果。'), '',
          '## '+label('Browse by category', '分类导航'), '']
        for cat in active:
            count=sum(c['category']==cat['id'] for c in cases)
            lines.append(f'- [{cat["emoji"]} {cat[lang]}](#{cat["id"]}) · {count} · [{label("Category page", "分类页面")}](categories/{cat["id"]}{suffix}.md)')
        lines += ['', '<a id="latest"></a>', '', '## ✨ '+label('Latest Additions','最新收录'), '']
        for c in list(reversed(cases))[:6]:
            lines.append(f'- [{c["title"][lang]}](#{c["id"]}) · **{prompt_label(c)}**')
        for cat in active:
            lines += ['',f'<a id="{cat["id"]}"></a>', '', f'## {cat["emoji"]} {cat[lang]}', '', cat['description'][lang]]
            for c in [c for c in cases if c['category']==cat['id']]:
                lines += case_lines(c, 1)
        files[gallery]='\n'.join(lines)
        for cat in active:
            selected = [c for c in cases if c['category'] == cat['id']]
            page = [f'# {cat["emoji"]} GPT-6 Astra — {cat[lang]}', '',
              f'[English]({cat["id"]}.md) · [简体中文]({cat["id"]}.zh-CN.md) · [{label("Home", "返回首页")}](../../{filename}) · [{label("Full gallery", "完整图册")}](../{Path(gallery).name})', '',
              cat['description'][lang], '',
              f'**{len(selected)} {label("cases", "个案例")}**', '',
              label('Prompt labels describe how much text is shown here. For excerpts, follow the original prompt link for the complete text.', '提示词标签表示本页展示的完整度。标为摘录的案例，请访问提示词原帖查看全文。'), '',
              '<a id="cases"></a>', '', '## '+label('Choose a case', '选择案例'), '']
            for c in selected:
                page.append(f'- [{c["title"][lang]}](#{c["id"]}) · **{prompt_label(c)}**')
            for c in selected:
                page += case_lines(c, 2)
                page += [f'[{label("Back to case list", "返回案例目录")}](#cases)', '']
            page += ['## '+label('Other categories', '其他分类'), '']
            for other in active:
                if other['id'] != cat['id']:
                    page.append(f'- [{other["emoji"]} {other[lang]}]({other["id"]}{suffix}.md)')
            files[category_path(cat['id'])] = '\n'.join(page)+'\n'
    lines=['# Collection index / 已收录索引', '',
      'Generated from `data/cases.json` and `data/sources.json`. Check this page or run `python3 scripts/catalog.py check-url URL` before reviewing a candidate. / 本页由案例与来源数据自动生成；开始审核候选案例前，请先检查本页或运行查重命令。', '',
      '| Case ID | Case / 案例 | Category / 分类 | Result / 成果 | Prompt / 提示词 | All source IDs / 全部来源 ID |',
      '| --- | --- | --- | --- | --- | --- |']
    catmap={c['id']:c for c in categories}
    def cell(value):
        return str(value).replace('|','\\|').replace('\n',' ')
    for c in cases:
        category=catmap[c['category']]
        result=sm[c['primary_source_id']]
        prompt=sm[c['prompt']['source_id']]
        source_links='<br>'.join(f'[{sid}]({sm[sid]["url"]})' for sid in c['source_ids'])
        lines.append(
          f'| `{c["id"]}` | {cell(c["title"]["en"])}<br>{cell(c["title"]["zh"])} | '
          f'{category.get("emoji", "")} {cell(category["en"])}<br>{cell(category["zh"])} | '
          f'[@{result["author"]}]({result["url"]}) | [@{prompt["author"]}]({prompt["url"]}) | {source_links} |')
    files['docs/collection-index.md']='\n'.join(lines)+'\n'
    lines=['# Source ledger / 来源台账', '', 'Generated from `data/sources.json`. Every listed post supports a curated case. / 每条来源都对应一个正式收录案例。', '', '| Post / 原帖 | Status / 状态 | Case / 案例 | Checked / 检查日期 | Reason / 原因 |', '| --- | --- | --- | --- | --- |']
    for s in sources:
        reason=s['reason'].replace('|','\\|').replace('\n',' ')
        lines.append(f'| [@{s["author"]} · {s["post_id"]}]({s["url"]}) | {s["status"]} | {s["case_id"] or "—"} | {s["last_checked_at"]} | {reason} |')
    files['docs/source-ledger.md']='\n'.join(lines)+'\n'
    buf=io.StringIO(newline='')
    writer=csv.DictWriter(buf,fieldnames=list(sources[0]) if sources else ['post_id','url','status'],lineterminator='\n')
    writer.writeheader();writer.writerows(sources)
    files['data/source-ledger.csv']=buf.getvalue()
    return files

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('validate')
    build=sub.add_parser('build');build.add_argument('--check',action='store_true')
    check=sub.add_parser('check-url');check.add_argument('url')
    add=sub.add_parser('add-source');add.add_argument('url');add.add_argument('--reason',required=True)
    args=parser.parse_args()
    if args.command == 'validate':
        cases,sources,_=validate(); print(f'Valid: {len(cases)} cases, {len(sources)} sources')
    elif args.command == 'build':
        stale=[]
        for name,content in render().items():
            path=ROOT/name
            if args.check:
                # Git may check out text as CRLF on Windows; compare content, not line endings.
                if not path.exists() or path.read_text(encoding='utf-8') != content: stale.append(name)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode())
        if stale: raise SystemExit('Regenerate files: '+', '.join(stale))
        print('Generated files are current' if args.check else 'Catalog and ledger generated')
    else:
        pid,url=normalize_url(args.url)
        sources=read('sources.json')
        existing=next((s for s in sources if s['post_id']==pid),None)
        if existing:
            print(json.dumps({'result':'already-tracked','source':existing},ensure_ascii=False,indent=2))
        elif args.command == 'check-url':
            print(json.dumps({'result':'new','post_id':pid,'url':url}))
        else:
            today=date.today().isoformat()
            author=urlsplit(url).path.split('/')[1]
            sources.append(dict(post_id=pid,url=url,author=author if author!='i' else None,published_date=None,first_seen_at=today,last_checked_at=today,status='pending',case_id=None,verification='not-read',media='not-audited',reason=args.reason))
            (ROOT/'data/sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
            print('Added pending source; review it and run build')

if __name__=='__main__': main()
