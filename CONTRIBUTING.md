# Contributing / 贡献指南

English: Submit the creator’s original post with a concrete result, explicit GPT-6 Astra attribution, the public prompt, a useful method, and honest limitations. Popularity alone is not enough. Announcements, generic praise and reposts without additional evidence do not qualify. We accept multilingual originals; each curated case must have original English and Chinese summaries.

中文：提交创作者原帖，要求有具体成果、明确的 GPT-6 Astra 归属、公开提示词、值得借鉴的方法与如实说明的局限。不以点赞量代替质量；发布新闻、泛泛赞美和没有新增证据的搬运不进入精选案例。原帖语言不限，案例须提供英文和中文原创摘要。

1. Check the generated [`docs/collection-index.md`](docs/collection-index.md) and run `python3 scripts/catalog.py check-url 'https://x.com/author/status/POST_ID'` before opening a known post again. This shared index is the quick reference for agents working in parallel. / 先查看自动生成的[收录索引](docs/collection-index.md)，并运行查重命令；这是多个 Agent 并行收集时共用的快速索引。
2. Register an unseen link with `add-source URL --reason 'Why review this / 收集原因'` as soon as review starts so another agent can see that it is claimed. Do not include it in a release until its prompt is public and verified. / 开始审核新链接时立即登记，避免其他 Agent 重复处理；提示词公开并核验前不要纳入发布版本。
3. Read the original post. Capture creator, date, model evidence, exact public prompt, outcome, workflow and limitations. Do not treat search snippets or third-party mirrors as verification. / 阅读原帖并记录作者、日期、模型证据、公开提示词原文、成果、方法和局限；搜索摘要和镜像不算核验。
4. Add an original bilingual entry to `data/cases.json`; mark its source `accepted` and `x-post-read`. Use the same case ID for updates to the same work; add the new post ID to `source_ids`. / 为同一作品的更新沿用案例 ID，追加来源。
5. Run validation, generation and tests, then review both READMEs. / 校验、生成并检查双语目录。

```sh
python3 scripts/catalog.py validate
python3 scripts/catalog.py build
python3 -m unittest discover -s tests
python3 scripts/catalog.py build --check
```

Prompts are required for every curated case. Preserve the author’s wording, identify whether the catalog shows the full text or an opening excerpt, and always link to the post containing it. Never reconstruct or paraphrase a missing prompt as if it were the original. / 每个正式案例都必须有公开提示词。保留作者原文，标明目录展示的是全文还是开头摘录，并始终链接到提示词所在原帖；不得把推测或改写包装成作者原文。

Media: Link to the original post by default. Do not rehost media without permission. Inspect the actual result before describing its visual quality. / 默认链接原帖，不擅自转载媒体；描述视觉质量前必须查看实际成果。
