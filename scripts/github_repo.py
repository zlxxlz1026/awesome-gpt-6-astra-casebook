#!/usr/bin/env python3
"""Maintain this repository's About metadata and private traffic snapshots.

Uses GH_TOKEN/GITHUB_TOKEN or the existing Git credential helper, in memory only.
"""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

ROOT = Path(__file__).resolve().parents[1]
REPO = 'zlxxlz1026/awesome-gpt-6-astra-casebook'
DESCRIPTION = ('📚 Awesome GPT-6 Astra: curated use cases, prompt examples & demos for coding, '
               'websites, UI design, 3D, video, automation and games. '
               'GPT-6 Astra 实战案例与提示词合集，中英双语，附作者原帖与创作流程。')
TOPICS = 'gpt-6-astra gpt-6 awesome awesome-list generative-ai llm use-cases ai-prompts prompt-engineering ai-coding web-development game-development computer-use'.split()


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def credential():
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        return token
    result = subprocess.run(
        ['git', '-c', f'safe.directory={ROOT.as_posix()}', 'credential', 'fill'],
        input=f'url=https://github.com/{REPO}.git\nusername=zlxxlz1026\n\n',
        text=True, capture_output=True, timeout=30, cwd=ROOT,
        env={**os.environ, 'GIT_TERMINAL_PROMPT': '0', 'GCM_INTERACTIVE': 'never'})
    fields = dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)
    if result.returncode or not fields.get('password'):
        raise RuntimeError('GitHub credentials unavailable. Sign in with Git Credential Manager or set GH_TOKEN.')
    return fields['password']


class GitHub:
    def __init__(self):
        self.token = credential()
        self.opener = build_opener(NoRedirect())

    def request(self, path='', method='GET', payload=None):
        if path and not path.startswith('/'):
            raise ValueError('Expected a repository-relative API path')
        request = Request(
            f'https://api.github.com/repos/{REPO}{path}',
            data=None if payload is None else json.dumps(payload).encode('utf-8'),
            method=method,
            headers={'Authorization': f'Bearer {self.token}',
                     'Accept': 'application/vnd.github+json',
                     'Content-Type': 'application/json',
                     'User-Agent': 'astra-casebook-maintenance',
                     'X-GitHub-Api-Version': '2022-11-28'})
        with self.opener.open(request, timeout=30) as response:
            return json.load(response)


def merge_topics(existing):
    merged = list(dict.fromkeys(existing + TOPICS))
    if len(merged) > 20:
        raise ValueError('More than 20 combined topics; choose topics manually. No metadata changed.')
    return merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['status', 'apply-metadata', 'traffic'])
    args = parser.parse_args()
    api = GitHub()
    if args.command == 'status':
        repo = api.request()
        print(json.dumps({key: repo.get(key) for key in
                          ('full_name', 'description', 'topics', 'permissions', 'default_branch')}, ensure_ascii=False))
    elif args.command == 'apply-metadata':
        topics = merge_topics(api.request('/topics')['names'])
        api.request('', 'PATCH', {'description': DESCRIPTION})
        api.request('/topics', 'PUT', {'names': topics})
        result = api.request()
        if result['description'] != DESCRIPTION or set(result['topics']) != set(topics):
            raise RuntimeError('Metadata verification failed; inspect current About settings.')
        print(json.dumps({'description': result['description'], 'topics': result['topics']}, ensure_ascii=False))
    else:
        snapshot = {'repository': REPO, 'captured_at': datetime.now(timezone.utc).isoformat(),
                    'window': 'GitHub rolling 14-day window; snapshots overlap', 'data': {}, 'errors': {}}
        for name in ('views', 'clones', 'popular/referrers', 'popular/paths'):
            try:
                snapshot['data'][name] = api.request('/traffic/' + name)
            except HTTPError as error:
                snapshot['errors'][name] = f'HTTP {error.code}'
        output = ROOT / '.local' / 'traffic'
        output.mkdir(parents=True, exist_ok=True)
        path = output / (datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.json')
        path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'Saved private snapshot: {path}')
        print(json.dumps({name: {key: data[key] for key in ('count', 'uniques')}
                          for name, data in snapshot['data'].items() if name in ('views', 'clones')}))
        if snapshot['errors']:
            raise RuntimeError('Some traffic endpoints were unavailable: ' + json.dumps(snapshot['errors']))


if __name__ == '__main__':
    try:
        main()
    except HTTPError as error:
        raise SystemExit(f'GitHub API returned HTTP {error.code}; check authentication and repository permissions.')
    except (URLError, subprocess.TimeoutExpired):
        raise SystemExit('GitHub request or credential lookup timed out or could not connect.')
    except (RuntimeError, ValueError) as error:
        raise SystemExit(str(error))
