# Reproduction records / 复现记录

[English home](../../README.md) · [中文首页](../../README.zh-CN.md)

No independent reproduction report has been completed in this pass. Source review, playing an existing demo and regenerating a work are three different activities. / 本轮尚未完成独立复现报告。核对原帖、试玩现成作品和重新生成作品是三件不同的事。

## Access audit — 2026-09-07 / 入口检查

The source ledger records these three author replies as links to playable builds. Attempts to open the replies with the web retrieval tool failed in this pass; the underlying demo addresses could not be obtained or tested. This is an access limitation, not evidence that the demos are broken. / 台账将以下三条作者回复标为试玩链接来源。本轮网页读取失败，未能取得并测试实际演示地址；这不代表演示本身失效。

| Case / 案例 | Recorded demo-link source / 试玩入口来源 | Access result / 本轮结果 | Next check / 下一步 |
| --- | --- | --- | --- |
| Breakwater | [Author reply / 作者回复](https://x.com/aniketjart/status/2096028593415655666) | Retrieval failed / 读取失败 | Obtain the linked build, then check movement, combat and restart / 获取演示后检查移动、战斗和重开 |
| Beach crab adventure / 海岛螃蟹冒险 | [Author reply / 作者回复](https://x.com/zeuuss_01/status/2096342806948102335) | Retrieval failed / 读取失败 | Obtain the linked build, then check movement and objective progression / 获取演示后检查移动和目标推进 |
| Voidrunner | [Author reply / 作者回复](https://x.com/superalesha/status/2096013278325387402) | HTTP 403 | Obtain the linked build, then check racing input, collision and reset / 获取演示后检查驾驶输入、碰撞和重置 |

## Required report fields / 报告必填项

Use one Markdown file per actual attempt, named `YYYY-MM-DD-case-id.md`. Do not create empty success reports. / 每次真实尝试单独保存，文件名为日期加案例 ID，不创建空的成功报告。

| Field / 字段 | What to record / 记录内容 |
| --- | --- |
| Activity / 活动 | Source review, artifact playtest, or model reproduction / 原帖核对、作品试玩或模型复现 |
| Provenance / 来源 | Case ID, original prompt URL, demo/code URL and revision if available / 案例 ID、原始提示词、演示或代码链接及版本 |
| Environment / 环境 | OS, browser/tool versions, model label and settings actually used / 实际系统、浏览器与工具版本、模型标签与设置 |
| Inputs / 输入 | Exact prompt, follow-ups, supplied assets and dependencies / 实际提示词、后续修改、输入素材与依赖 |
| Procedure / 步骤 | Commands and actions someone else can follow / 他人可执行的命令与操作 |
| Outcome / 结果 | Each acceptance check: passed, failed or not tested, with evidence / 每项检查的通过、失败或未测状态与证据 |
| Iterations / 迭代 | Failed attempts and fixes as well as the final result / 同时保留失败和修复记录 |
| Time and cost / 耗时与成本 | Measured values with evidence, or unknown; no estimates presented as actuals / 有依据的实测值或未知，不把估算当实测 |
| Limits / 限制 | Remaining issues and conditions not tested / 尚存问题及未测条件 |

Only label a run as independently reproduced when the generation process and relevant checks were actually executed and recorded. Keep these reports separate from the curated catalog's source evidence. / 只有实际执行生成过程及相关检查并留下记录后，才能标为独立复现；复现报告与精选目录的来源证据分开维护。
