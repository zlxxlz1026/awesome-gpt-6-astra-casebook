#!/usr/bin/env python3
"""Offline catalog maintenance. Python 3.10+, standard library only."""
import argparse
import csv
import io
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
        for field in ('title', 'summary', 'workflow', 'limitations'):
            assert all(c[field][lang].strip() for lang in ('en', 'zh')), f'Missing translation: {c["id"]}'
        assert c['model'] == 'gpt-6-astra'
        assert c['model_evidence'] in ('author-stated', 'visible-model-label')
        assert c['reproduction'] in ('not-tested', 'partial', 'reproduced')
        assert c['primary_source_id'] in c['source_ids']
        assert c['source_ids'] and len(set(c['source_ids'])) == len(c['source_ids'])
        for sid in c['source_ids']:
            assert sid not in owned, 'One post cannot belong to multiple cases'
            owned.add(sid)
            assert sm[sid]['status'] == 'accepted' and sm[sid]['case_id'] == c['id']
            assert sm[sid]['verification'] == 'x-post-read'
        if c['prompt'] is not None:
            assert c['prompt']['source_id'] in c['source_ids'] and c['prompt']['text'].strip()
    return cases, sources, categories

def render():
    cases, sources, categories = validate()
    sm = {s['post_id']: s for s in sources}
    files = {}
    for lang, filename in [('en', 'README.md'), ('zh', 'README.zh-CN.md')]:
        zh = lang == 'zh'
        lines = ['# Awesome GPT-6 Astra', '', '[English](README.md) | [简体中文](README.zh-CN.md)', '',
          '精选 X 上有具体成果的 GPT-6 Astra 使用案例，整理方法、工具与局限，帮助你获得可实践的灵感。' if zh else 'A curated collection of concrete GPT-6 Astra use cases from X, with methods, tools and limitations to help you turn inspiration into practice.', '',
          f'**{len(cases)} 个案例 · {len(sources)} 条来源记录 · 仅收录 X 来源**' if zh else f'**{len(cases)} cases · {len(sources)} tracked sources · X sources only**', '',
          '原帖阅读与效果复现分别记录；请查看各案例的状态及局限。未公开的提示词不作补写。' if zh else 'Source review and reproduction are tracked separately; see each case’s status and limitations. Undisclosed prompts are not invented.', '',
          '## 分类' if zh else '## Categories', '',
          '| 分类 | 案例数 |' if zh else '| Category | Cases |', '| --- | ---: |']
        for cat in categories:
            count = sum(c['category'] == cat['id'] for c in cases)
            label = f'[{cat[lang]}](#{cat["id"]})' if count else cat[lang]
            lines.append(f'| {label} | {count} |')
        lines += ['', '空分类代表待补充方向。' if zh else 'Empty categories are collection priorities.']
        for cat in categories:
            selected = [c for c in cases if c['category'] == cat['id']]
            if not selected: continue
            lines += ['', f'<a id="{cat["id"]}"></a>', '', f'## {cat[lang]}']
            for c in selected:
                s=sm[c['primary_source_id']]
                lines += ['', f'### {c["title"][lang]}', '', c['summary'][lang], '',
                  f'- {"原帖" if zh else "Source"}: [@{s["author"]}]({s["url"]}) · {s["published_date"]}',
                  f'- {"方法" if zh else "Method"}: {c["workflow"][lang]}',
                  f'- {"工具" if zh else "Tools"}: {", ".join(c["tags"]) or ("未披露" if zh else "Not disclosed")}',
                  f'- {"局限" if zh else "Limitations"}: {c["limitations"][lang]}',
                  f'- {"模型归属" if zh else "Model evidence"}: {c["model_evidence"]} · {"复现" if zh else "Reproduction"}: {c["reproduction"]}',
                  f'- {"提示词" if zh else "Prompt"}: ' + ((f'[Open / 查看]({sm[c["prompt"]["source_id"]]["url"]})') if c['prompt'] else ('未公开' if zh else 'Not disclosed'))]
        lines += ['', '## 参与和维护' if zh else '## Contributing & maintenance', '',
          '[贡献指南 / Contributing](CONTRIBUTING.md) · [去重台账 / Source ledger](docs/source-ledger.md) · [维护流程 / Maintenance](docs/MAINTENANCE.md)', '',
          '数据保存在 [cases.json](data/cases.json) 与 [sources.json](data/sources.json)，双语目录和台账由脚本生成；未来网页可直接使用同一数据。' if zh else 'The source of truth is [cases.json](data/cases.json) and [sources.json](data/sources.json). The bilingual catalog and ledger are generated; a future website can consume the same data.', '',
          '## 致谢与许可' if zh else '## Credits & license', '',
          '参考 [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) 的分类、多语言与结构化整理思路。本项目独立编写，未复制案例库；与 OpenAI 无隶属关系。' if zh else 'Inspired by the categories, multilingual navigation and structured curation in [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2). Independently authored; its case database is not copied. Not affiliated with OpenAI.', '',
          '项目原创代码和文字采用 [MIT](LICENSE)。链接中的原帖、提示词及媒体版权属于原作者，不因收录而重新授权。' if zh else 'Original project code and writing are [MIT licensed](LICENSE). Linked posts, prompts and media remain under their authors’ rights and are not relicensed by inclusion.', '']
        files[filename]='\n'.join(lines)
    lines=['# Source ledger / 来源去重台账', '', 'Generated from `data/sources.json`. All statuses prevent accidental re-ingestion; pending items may be explicitly revisited. / 所有状态均参与去重；待核验项可主动复查。', '', '| Post / 原帖 | Status / 状态 | Case / 案例 | Checked / 检查日期 | Reason / 原因 |', '| --- | --- | --- | --- | --- |']
    for s in sources:
        reason=s['reason'].replace('|','\\|').replace('\n',' ')
        lines.append(f'| [@{s["author"]} · {s["post_id"]}]({s["url"]}) | {s["status"]} | {s["case_id"] or "—"} | {s["last_checked_at"]} | {reason} |')
    files['docs/source-ledger.md']='\n'.join(lines)+'\n'
    buf=io.StringIO(newline='')
    writer=csv.DictWriter(buf,fieldnames=list(sources[0]) if sources else ['post_id','url','status'])
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
