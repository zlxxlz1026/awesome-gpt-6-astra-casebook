# Maintenance / 维护手册

## Local workflow / 本地工作流

This repository is maintained at `zlxxlz1026/awesome-gpt-6-astra-casebook`. No scheduled collector is enabled. / 本项目维护于 `zlxxlz1026/awesome-gpt-6-astra-casebook`，当前未启用定时采集。

The collector is a human/agent review process; `catalog.py` operates offline and does not crawl X. / 采集由人工或智能体在 X 上完成；脚本离线维护数据，不会自动抓取 X。

## Data contract / 数据约定

- `data/cases.json`: one logical work per stable slug; bilingual `title`, `summary`, `workflow`, `limitations`; category; tool tags; source IDs; model evidence; and a verified public prompt. / 每个逻辑作品一条记录，稳定 ID 不随标题翻译改变，并包含已核验的公开提示词。
- `data/sources.json`: one supporting post per decimal string `post_id`; never store IDs as JavaScript numbers. Release versions contain sources attached to curated cases. / 每条支撑来源一条记录，数字 ID 必须以字符串保存，避免精度损失；发布版本只保留正式案例对应的来源。
- `data/categories.json`: stable category IDs and bilingual labels. / 稳定分类标识及双语名称。
- `data/search-runs.json`: search date, exact queries, actual coverage and next steps. / 保存每轮检索词与真实覆盖范围，不能声称已抓全。
- READMEs, `docs/collection-index.md`, `docs/source-ledger.md` and `data/source-ledger.csv` are generated outputs. The collection index is the compact, one-case-per-row view shared by parallel agents; edit the JSON sources instead. / 双语目录、收录索引和台账均自动生成；收录索引是一案例一行、供并行 Agent 共用的快速视图，修改时仍以 JSON 数据为准。

## Deduplication / 去重

1. Start every collection pass by reading `docs/collection-index.md`; it exposes each accepted case, result post, prompt post and all supporting post IDs in one table. / 每轮收集先查看 `docs/collection-index.md`，一张表即可核对每个正式案例的成果帖、提示词帖和全部来源 ID。
2. Normalize direct post URLs to a numeric post ID; strip query parameters, fragments and photo/video suffixes; treat X and Twitter domains as aliases. / 按数字 ID 去重，分享参数、媒体后缀和域名差异不影响判断。
3. Run `check-url` before opening a candidate and use `add-source` immediately when an agent starts reviewing a new URL. Both commands are offline; registering a duplicate leaves the existing record unchanged. / 打开候选帖前运行 `check-url`；Agent 开始审核新链接时立即使用 `add-source` 登记。这两个命令都不会联网，重复登记也不会覆盖原记录。
4. Merge multiple posts about the same artifact under one `case_id`. A quote/repost without added value becomes `duplicate` with a reason and the existing case ID. / 同作品多帖归并；无增量转述标记重复并注明关联案例。
5. Different post IDs do not prove different content. Compare creator, project/demo identity and outcome manually. Text similarity is only a review hint because translations and copy-paste prompts can mislead. / 异 ID 不等于新内容，人工比较作者、作品和结果。
6. Explicitly revisit pending/unavailable posts when there is new information. Preserve first-seen dates and update last-checked dates; Git history records changes. / 有新增线索时主动复查，不让去重永久屏蔽待处理项。

## Review checklist / 审核要点

- Original X source is accessible and model attribution explicit. / 原帖可访问且模型明确。
- A specific result and transferable method are present. / 有具体成果和可借鉴方法。
- The author’s exact prompt is public, attributable and linked from the case. / 作者提示词原文公开、可归属，并由案例直接链接。
- Dependencies, supplied assets, costs and visible shortcomings are stated when relevant. / 相关依赖、输入素材、成本和可见缺点均如实说明。
- Original and translated text are distinguished; author claims are not presented as benchmark results. / 区分原文、翻译和作者自述。
- Inspect the media before making claims about visual quality. / 判断视觉质量前必须查看实际媒体内容。

## Next collection pass / 下一轮

Seek original prompts and expand software engineering, games, research and office automation. Mix English, Chinese and Japanese searches, then verify every candidate in the creator’s original thread. / 继续寻找公开原始提示词，扩展软件工程、游戏、研究和办公案例；混合使用中、英、日文检索，并回到创作者原帖逐一核验。

## Learning guides and evidence / 学习指南与证据

`data/case-notes.json` stores optional bilingual prerequisite notes and editorial prompt breakdowns for selected cases. Each note must cite source IDs already attached to that case. Missing details must remain explicitly unknown; distinguish recorded facts from suggestions. The generator appends notes after the unchanged creator prompt in category pages and the full gallery, and links featured notes from the READMEs. / 该文件维护精选案例的双语使用前提与提示词拆解，引用来源必须属于对应案例；缺失信息明确标出，并区分已有事实与项目建议。生成器在作者原文之后追加分析，同时在首页提供深读入口。

Category covers are explicitly selected in `data/categories.json` using `cover.case_id` and `cover.height` (currently 160 px for every active category). The cover must belong to the category; changing case order does not change the cover. Height-only sizing preserves the image's aspect ratio. / 分类封面由数据中的案例 ID 和高度明确指定，目前统一 160 像素；案例必须属于该分类，调整案例顺序不会替换封面，仅指定高度以保留图片比例。

`docs/categories/*.md` are generated bilingual category pages. Edit the JSON and generator, then run `build`; never hand-edit these outputs. README links lead to category pages. The complete galleries and their stable case/category anchors remain available for existing links. Prompt labels come from `prompt.display`, distinguishing full text from excerpts without changing the original text. / 中英文分类页由脚本自动生成，首页直达分类页；完整图册及原有案例、分类锚点继续保留。提示词完整度直接读取已有数据，不改动作者原文。

Maintain beginner paths in `data/learning-paths.json`, editorial guides in `docs/guides/`, and evidence-backed run reports under `docs/reproduction/` using its record requirements. Keep source facts, editorial recommendations and run evidence visibly separate. / 新手路径、专题编辑内容与有证据的运行报告分别维护，并明确区分来源事实、项目建议与运行证据。

## Future website / 后续网页

For the current GitHub repository, see [discoverability settings and checks](DISCOVERABILITY.md). README search wording and navigation live in `scripts/catalog.py` and are regenerated from the catalog. / 当前仓库的搜索优化配置与核验见[搜索优化维护说明](DISCOVERABILITY.md)；首页文案与导航在生成脚本中维护。

Consume the existing JSON, filter by category, tools and language, show verification and prompt availability, and always link back to the X source. Keep videos as outbound links until embedding/reuse is deliberately implemented. / 网页直接读取现有 JSON，按分类、工具和语言筛选，展示核验与提示词状态并保留原帖入口。
