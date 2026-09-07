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
    return json.loads((ROOT / 'data' / name).read_text())

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
    return cases, sources, categories

def render():
    cases, sources, categories = validate()
    sm = {s['post_id']: s for s in sources}
    active = [cat for cat in categories if any(c['category'] == cat['id'] for c in cases)]
    files = {}
    def esc(value):
        return html.escape(str(value), quote=True)
    def image_path(c, nested=False):
        url=c['preview']['url']
        return '../'+url if nested and not url.startswith('https://') else url
    for lang, filename in [('en', 'README.md'), ('zh', 'README.zh-CN.md')]:
        zh = lang == 'zh'
        gallery = 'docs/gallery.zh-CN.md' if zh else 'docs/gallery.md'
        label = lambda en, cn: cn if zh else en
        lines = ['<div align="center">', '', '# 📚 Awesome GPT-6 Astra', '',
          '**'+label('Curated GPT-6 Astra use cases. See the result. Explore the prompt. Build your own.', 'GPT-6 Astra 实战案例精选 · 看作品，读提示词，动手创造。')+'**', '',
          '[English](README.md) · [简体中文](README.zh-CN.md)', '',
          f'**{len(cases)} {label("cases", "个案例")} · {len(active)} {label("categories", "个分类")}**', '', '</div>', '',
          label('A growing collection of creative and practical work made with GPT-6 Astra, pairing each result with its creator’s public prompt.', '收集 GPT-6 Astra 的创意与实用作品，将成果展示与作者公开的提示词放在一起，方便浏览、学习和尝试。'), '',
          f'📖 [{label("Browse all cases", "浏览全部案例")}]({gallery}) · ✨ [{label("Latest additions", "最新收录")}]({gallery}#latest) · ➕ [{label("Submit a case", "推荐案例")}](https://github.com/zlxxlz1026/awesome-gpt-6-astra-casebook/issues/new?template=submit-case.md)', '',
          '## 🖼️ '+label('Case Album', '案例图册'), '', '<table>']
        for offset in range(0,len(active),3):
            lines.append('<tr>')
            for cat in active[offset:offset+3]:
                selected=[c for c in cases if c['category']==cat['id']]
                cover=selected[0]
                link=f'{gallery}#{cat["id"]}'
                lines += ['<td width="33%" align="center" valign="top">',
                  f'<h3>{cat["emoji"]} {esc(cat[lang])}</h3>',
                  f'<p>{len(selected)} {label("case" if len(selected) == 1 else "cases", "个案例")}</p>',
                  f'<a href="{link}"><img src="{esc(image_path(cover))}" alt="{esc(cover["preview"]["alt"][lang])}" width="360"></a>',
                  f'<p>{esc(cat["description"][lang])}</p>',
                  f'<p><a href="{link}"><b>{label("View Cases →", "查看案例 →")}</b></a></p>', '</td>']
            lines.append('</tr>')
        lines += ['</table>', '', '## ✨ '+label('Latest Additions', '最新收录'), '',
          '| '+label('Case | Category | Creator', '案例 | 分类 | 作者')+' |', '| --- | --- | --- |']
        for c in list(reversed(cases))[:6]:
            cat=next(x for x in active if x['id']==c['category']);s=sm[c['primary_source_id']]
            lines.append(f'| [{c["title"][lang]}]({gallery}#{c["id"]}) | {cat["emoji"]} {cat[lang]} | [@{s["author"]}]({s["url"]}) |')
        lines += ['', '## 🤝 '+label('Contribute', '参与共建'), '',
          label('Found something worth trying? Share the result and its public prompt through an issue or pull request. See the [contribution guide](CONTRIBUTING.md).', '发现值得尝试的作品？欢迎通过 Issue 或 PR 分享成果与公开提示词，详见[贡献指南](CONTRIBUTING.md)。'), '',
          '## License', '',
          label('Original project code and writing: [MIT](LICENSE). Referenced works, prompts and previews belong to their respective creators. This is an independent community project.', '项目原创代码与文字采用 [MIT](LICENSE) 许可。引用作品、提示词与预览图的权利归各自作者所有。本项目为独立社区整理。'), '']
        files[filename]='\n'.join(lines)
        lines=['# '+label('📖 Astra Casebook — Full Gallery','📖 Astra Casebook · 完整案例图册'), '',
          '[English](gallery.md) · [简体中文](gallery.zh-CN.md) · ['+label('Home','返回首页')+'](../'+filename+')', '', '<a id="latest"></a>', '',
          '## ✨ '+label('Latest Additions','最新收录'), '']
        for c in list(reversed(cases))[:6]:
            lines.append(f'- [{c["title"][lang]}](#{c["id"]})')
        for cat in active:
            lines += ['',f'<a id="{cat["id"]}"></a>', '', f'## {cat["emoji"]} {cat[lang]}']
            for c in [c for c in cases if c['category']==cat['id']]:
                source=sm[c['primary_source_id']];prompt=sm[c['prompt']['source_id']]
                lines += ['',f'<a id="{c["id"]}"></a>', '',f'### {c["title"][lang]}','',
                  f'[![{c["preview"]["alt"][lang]}]({image_path(c,True)})]({source["url"]})','',c['summary'][lang],'',
                  f'**{label("Creator", "作者")}**: [@{source["author"]}]({source["url"]}) · {source["published_date"]}<br>',
                  f'**{label("Tools & techniques", "工具与技术")}**: {", ".join(c["tags"])}','',
                  '**'+label('How it works','创作方法')+'**','',c['workflow'][lang],'',
                  '**'+label('What to know','值得注意')+'**','',c['limitations'][lang],'',
                  '**'+label('Prompt','提示词')+'**','']
                if c['prompt']['display']=='full':
                    lines += ['```text',c['prompt']['text'],'```','']
                else:
                    lines += ['> '+c['prompt']['text'],'',label('Opening excerpt; the author’s complete prompt is linked below.','以上为开头摘录，完整提示词见下方作者原帖。'),'']
                lines += [f'↗ [{label("Read the original prompt", "查看作者完整提示词")}]({prompt["url"]}) · [{label("Watch the demo", "观看演示")}]({source["url"]})','']
        files[gallery]='\n'.join(lines)
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
                if not path.exists() or path.read_bytes() != content.encode(): stale.append(name)
            else: path.write_bytes(content.encode())
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
