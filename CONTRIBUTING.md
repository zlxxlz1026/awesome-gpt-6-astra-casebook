# Contributing / 贡献指南

English: Submit a direct X post link with a concrete result, explicit GPT-6 Astra attribution, a useful method, and honest limitations. Prefer the original creator. Popularity alone is not enough. Announcements, generic praise and reposts without additional evidence do not qualify. We accept multilingual originals; each curated case must have original English and Chinese summaries.

中文：提交 X 原帖链接，要求有具体成果、明确的 GPT-6 Astra 归属、值得借鉴的方法与如实说明的局限。优先原作者；不以点赞量代替质量。发布新闻、泛泛赞美和没有新增证据的搬运不进入精选案例。原帖语言不限，案例须提供英文和中文原创摘要。

1. Check `data/sources.json` or run `python3 scripts/catalog.py check-url 'https://x.com/author/status/POST_ID'` before reading a known post again. / 先查台账，避免重复打开已处理原帖。
2. Register an unseen link with `add-source URL --reason 'Why review this / 收集原因'`. It enters `pending`, not the public catalog. / 新链接先进入待核验队列。
3. Read the original post. Capture creator, date, model evidence, outcome, workflow and limitations. Do not treat search snippets or third-party mirrors as verification. / 阅读原帖并记录证据，搜索摘要和镜像不算核验。
4. Add an original bilingual entry to `data/cases.json`; mark its source `accepted` and `x-post-read`. Use the same case ID for updates to the same work; add the new post ID to `source_ids`. / 为同一作品的更新沿用案例 ID，追加来源。
5. Run validation, generation and tests, then review both READMEs. / 校验、生成并检查双语目录。

```sh
python3 scripts/catalog.py validate
python3 scripts/catalog.py build
python3 -m unittest discover -s tests
python3 scripts/catalog.py build --check
```

Prompts: `null` means undisclosed. Never reverse-engineer a prompt and label it as the author's. If a prompt is provided, store `{"text": "...", "source_id": "..."}` only when redistribution is permitted, and preserve attribution. Otherwise link to it. / 未公开提示词填 `null`；不得把推测包装成原文。只有允许再分发时才保存提示词正文，否则只保留链接。

Media: Link to the original X post by default. Do not rehost media without permission. Record whether a video was actually watched; the presence of a video is not a playback audit. / 默认链接原帖，不擅自转载媒体；区分“有视频”与“已观看核验”。

A source being readable does not mean its claims are reproduced. Use `not-tested`, `partial`, or `reproduced` and document the actual environment and observed results when testing. / 原帖可读不代表效果复现；复现时记录环境和实测结果。
