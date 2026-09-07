# Maintenance / 维护手册

## Local workflow / 本地工作流

This repository is prepared for `zlxxlz1026/awesome-gpt-6-astra`. Remote creation and synchronization are handled by the owner. No scheduled collector is enabled. / 本项目按 `zlxxlz1026/awesome-gpt-6-astra` 准备，由仓库所有者创建远程仓库并同步。尚未启用定时采集。

The collector is a human/agent review process; `catalog.py` operates offline and does not crawl X. / 采集由人工或智能体在 X 上完成；脚本离线维护数据，不会自动抓取 X。

## Data contract / 数据约定

- `data/cases.json`: one logical work per stable slug; bilingual `title`, `summary`, `workflow`, `limitations`; category; tool tags; source IDs; model evidence; prompt availability; reproduction state. / 每个逻辑作品一条记录，稳定 ID 不随标题翻译改变。
- `data/sources.json`: one post per decimal string `post_id`; never store X IDs as JavaScript numbers. Includes all accepted, pending, rejected, duplicate and unavailable records. / 数字 ID 必须以字符串保存，避免精度损失；所有审核状态都保留。
- `data/categories.json`: stable category IDs and bilingual labels. / 稳定分类标识及双语名称。
- `data/search-runs.json`: search date, exact queries, actual coverage and next steps. / 保存每轮检索词与真实覆盖范围，不能声称已抓全。
- READMEs, `docs/source-ledger.md` and `data/source-ledger.csv` are generated outputs. CSV is a view, not a second editable database. / 双语目录和台账自动生成，CSV 不单独编辑。

## Deduplication / 去重

1. Normalize direct post URLs to a numeric post ID; strip query parameters, fragments and photo/video suffixes; treat X and Twitter domains as aliases. / 按数字 ID 去重，分享参数、媒体后缀和域名差异不影响判断。
2. Check every recorded status before opening a post. `check-url` and `add-source` never fetch content; registering a duplicate leaves the existing record unchanged. / 打开前检查全部状态，重复登记不会覆盖原记录。
3. Merge multiple posts about the same artifact under one `case_id`. A quote/repost without added value becomes `duplicate` with a reason and the existing case ID. / 同作品多帖归并；无增量转述标记重复并注明关联案例。
4. Different post IDs do not prove different content. Compare creator, project/demo identity and outcome manually. Text similarity is only a review hint because translations and copy-paste prompts can mislead. / 异 ID 不等于新内容，人工比较作者、作品和结果。
5. Explicitly revisit pending/unavailable posts when there is new information. Preserve first-seen dates and update last-checked dates; Git history records changes. / 有新增线索时主动复查，不让去重永久屏蔽待处理项。

## Review checklist / 审核要点

- Original X source is accessible and model attribution explicit. / 原帖可访问且模型明确。
- A specific result and transferable method are present. / 有具体成果和可借鉴方法。
- Missing prompts, assets, costs and reproduction gaps are stated. / 明确缺失信息。
- Original and translated text are distinguished; author claims are not presented as benchmark results. / 区分原文、翻译和作者自述。
- Inspect video before making claims about its visual quality. Current seed cases are text-verified and not playback-audited. / 判断视觉质量前必须观看视频；当前种子案例只完成文字核验。

## Next collection pass / 下一轮

Review pending videos, seek original prompts, and expand software engineering, games, research and office automation. Mix English and Chinese searches; Japanese originals are welcome. Use X search and author threads, not off-platform case databases. / 复查待核验视频，补充原始提示词，扩展软件工程、游戏、研究和办公案例；仅从 X 收录。

## Future website / 后续网页

Consume the existing JSON, filter by category, tools and language, show verification and prompt availability, and always link back to the X source. Keep videos as outbound links until embedding/reuse is deliberately implemented. / 网页直接读取现有 JSON，按分类、工具和语言筛选，展示核验与提示词状态并保留原帖入口。

## First GitHub sync / 首次同步

Create an empty public repository named `awesome-gpt-6-astra` under `zlxxlz1026`, then sync this local directory. If using GitHub CLI after restoring login:

```sh
gh repo create zlxxlz1026/awesome-gpt-6-astra --public --source=. --remote=origin --push
```

Run this only after the initial local commit exists. / 此命令要求本地已有首次提交。
