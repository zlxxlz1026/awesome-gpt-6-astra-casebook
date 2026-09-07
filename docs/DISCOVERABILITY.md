# GitHub discoverability / 仓库搜索优化

This project currently uses GitHub repository pages, not a separately hosted website. / 当前优化对象为 GitHub 仓库，尚未部署独立网站。

## Repository About settings / 仓库简介设置

The description and 13 topics below were applied and verified through the GitHub API on 2026-09-07. For later edits, use the About gear icon or the explicit maintenance command below. Preserve existing relevant topics. / 以下简介和 13 个主题已于 2026-09-07 通过 GitHub API 更新并核验。以后可通过 About 齿轮或下方维护命令更新，保留已有相关主题。

Description:

```text
📚 Awesome GPT-6 Astra: curated use cases, prompt examples & demos for coding, websites, UI design, 3D, video, automation and games. GPT-6 Astra 实战案例与提示词合集，中英双语，附作者原帖与创作流程。
```

Configured topics (GitHub allows up to 20 total):

```text
gpt-6-astra gpt-6 awesome awesome-list generative-ai llm use-cases ai-prompts prompt-engineering ai-coding web-development game-development computer-use
```

Avoid unrelated trending topics, unverified model aliases or claims of official affiliation. A website field should point only to a real published site. / 不添加无关热词、未经证实的模型别名或官方身份表述；Website 仅填写实际已发布的网站。

## Content maintenance / 内容维护

Beginner selections are maintained in `data/learning-paths.json`; bilingual editorial guides live in `docs/guides/`. Keep original editorial templates distinct from creator prompts. / 新手精选由 `data/learning-paths.json` 维护，双语专题指南位于 `docs/guides/`；原创需求模板与作者原始提示词明确区分。

- Edit `data/cases.json` and `scripts/catalog.py`, then regenerate the READMEs and galleries. Do not hand-edit generated pages. / 修改数据与生成脚本后重新生成页面，避免下次更新覆盖优化。
- Keep descriptive bilingual titles, concrete summaries, tool names and original source links. The README lists every case with a direct gallery anchor; the gallery includes category navigation. / 使用清晰的双语标题、具体摘要、工具名与原始来源；首页保留全部案例直达链接，图册保留分类导航。
- Preserve stable case IDs so shared links continue to work. Distinguish full prompts from excerpts and source claims from independently reproduced results. / 保持案例 ID 稳定，并区分完整提示词、摘录、作者自述与独立复现结果。
- Share relevant case links in your own project updates where useful. Do not spam communities or buy stars/backlinks. / 在自己的项目更新中按需分享相关案例链接，不刷星、不群发垃圾外链。

```sh
python scripts/catalog.py build
python -m unittest discover -s tests
python scripts/catalog.py validate
python scripts/catalog.py build --check
```

## Verification after publishing / 发布后核验

### Save a private traffic snapshot / 保存私有流量快照

```sh
python scripts/github_repo.py status
python scripts/github_repo.py traffic
```

The script uses `GH_TOKEN`, `GITHUB_TOKEN` or the owner's existing Git Credential Manager login. Tokens remain in memory and are sent only to GitHub's API; redirects are refused. An unavailable login or missing permissions fails explicitly. Traffic snapshots are saved under `.local/traffic/`, which is Git-ignored. Do not publish them by default. / 脚本使用环境变量或仓库所有者现有的 Git 凭据登录，凭据仅在内存中用于 GitHub API，拒绝重定向。缺少登录或权限时明确报错；快照保存在被 Git 忽略的本地目录，不默认公开。

The first snapshot was captured on 2026-09-07 after the metadata update. It is a starting baseline, not a pre-change measurement or proof of SEO impact. No recurring job is configured. Run weekly and preserve the raw daily series. Consecutive 14-day snapshots overlap: do not sum their totals or daily unique visitors into a period-wide unique count. Referrer data excludes search engines and GitHub itself. Zero values are the API's current report, not proof that nobody has visited; data updates can lag. / 首份快照在元数据更新后采集，只是起始基线，不能作为修改前数据或 SEO 效果证明。当前未配置定时任务；建议每周执行并保留每日明细。14 天窗口会重叠，不能把快照总量直接相加，也不能把每日独立访客相加当作周期独立访客。来源数据不包含搜索引擎与 GitHub 本身；零值仅表示 API 当前返回值，更新可能有延迟。

To deliberately reapply About settings, run `python scripts/github_repo.py apply-metadata`. It merges existing topics and refuses to exceed GitHub's 20-topic limit. This command changes live GitHub settings. / 如需重新应用简介和主题，执行该命令；它会合并已有主题，超过 20 个时拒绝修改。此命令会更改线上设置。

### Review the published pages / 核验发布页面

1. Confirm the default branch displays the updated English README and the Chinese link opens correctly. Check several case and category links. / 确认默认分支展示新首页，中文切换及案例、分类跳转正常。
2. Confirm the description and topics in About. These are GitHub settings and do not change when README files are pushed. / 单独确认 About 简介和 Topics，推送 README 不会修改这些配置。
3. Record GitHub Insights → Traffic views, unique visitors, referring sites and popular content before and after the update. GitHub repository traffic covers the past 14 days, so record snapshots regularly. / 记录修改前后的访问、独立访客、来源和热门内容；GitHub 流量窗口为最近 14 天，需定期留存。
4. Periodically check GitHub repository search for `gpt-6-astra` and relevant topics. Search-engine `site:` queries can provide a rough discovery check, but are not a complete index report. / 定期检查 GitHub 关键词与主题搜索；搜索引擎 `site:` 查询只能辅助观察，不是完整收录报告。

Improved wording and links help people and crawlers understand the collection; they do not guarantee ranking or a particular audience size. GitHub controls repository-page HTML metadata and robots rules. Adding a `robots.txt`, sitemap, meta tags or JSON-LD to this repository does not configure github.com pages. / 文案与链接优化有助于理解内容，但不能保证排名或覆盖人数。仓库页面的 HTML 元数据与爬虫规则由 GitHub 控制，向仓库添加 robots.txt、sitemap、meta 标签或 JSON-LD 不会配置 github.com 页面。

## References / 参考

- [GitHub: classify repositories with topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [GitHub: view repository traffic](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)
- [Google Search: SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
