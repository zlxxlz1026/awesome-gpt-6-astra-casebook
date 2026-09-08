# 🛠️ GPT-6 Astra — 工程与原型

[English](engineering.md) · [简体中文](engineering.zh-CN.md) · [返回首页](../../README.zh-CN.md) · [完整图册](../gallery.zh-CN.md)

工程工作流、实体原型与可投入生产的系统。

**2 个案例**

提示词标签表示本页展示的完整度。标为摘录的案例，请访问提示词原帖查看全文。

<a id="cases"></a>

## 选择案例

- [可落地制作的 Microduck 机器人原型](#microduck-robot-prototype) · **完整提示词**
- [无人值守的分割模型训练流水线](#microduck-segmentation-training) · **完整提示词**

<a id="microduck-robot-prototype"></a>

### 可落地制作的 Microduck 机器人原型

**完整提示词** · [提示词原帖](https://x.com/DeRonin_/status/2096567918859354155)

[![展示可打印 Microduck 零件的机器人原型工具](https://pbs.twimg.com/amplify_video_thumb/2096567835569053696/img/HRjmvb9ZAkTklImX?format=webp&name=medium)](https://x.com/DeRonin_/status/2096567918859354155)

一款机器人原型工具把极短需求转成可打印零件、运动干涉检查、电机计算、含价格的物料清单和装配说明。

**作者**: [@DeRonin_](https://x.com/DeRonin_/status/2096567918859354155) · 2026-09-06<br>
**工具与技术**: Robotics, 3D printing, Bill of materials

**创作方法**

先说明目标机器人，再从概念几何逐步迭代到机械检查、采购和制作文档，直至所有零件可以制造。

**值得注意**

虽然作者强调首条一句话提示词，但完整流程约耗时 45 分钟并用了五轮提示；帖子展示的是可制造方案，并未展示实物装配结果。

**提示词**

```text
prototype me a full Microduck
```

↗ [查看作者完整提示词](https://x.com/DeRonin_/status/2096567918859354155) · [观看演示](https://x.com/DeRonin_/status/2096567918859354155)

[返回案例目录](#cases)


<a id="microduck-segmentation-training"></a>

### 无人值守的分割模型训练流水线

**完整提示词** · [提示词原帖](https://x.com/LearnOpenCV/status/2097123587920634003)

[![两套 Microduck 实例分割模型预测结果对比](https://pbs.twimg.com/amplify_video_thumb/2097122679845449728/img/g0gMKyOCYKoBvXSM.jpg)](https://x.com/LearnOpenCV/status/2097122818815299892)

Astra 收集公开的 Microduck 素材，构建保留来源的数据集，生成两套对照掩码，并在没有人工标注的情况下训练两套 RF-DETR-Seg-M 模型。

**作者**: [@LearnOpenCV](https://x.com/LearnOpenCV/status/2097122818815299892) · 2026-09-08<br>
**工具与技术**: Computer vision, Roboflow, RF-DETR, SAM3

**创作方法**

向 Astra 提供已登录的 Roboflow 账号、公开素材来源、目标模型和留出评估要求；作者报告两次云端训练约 93 分钟完成。

**值得注意**

本次运行使用了含 50 credits 的 Roboflow 账号；对照实验按完整视频组留出，并在评估前冻结两套数据集。

**提示词**

```text
Get all images and videos of microducks from here pollen-robotics.com/microduck/. Generate masks and train RF-DETR-Seg-M using Roboflow.com. I will be flying in a few hours. I want to make sure the training run is set up and running even after I close this laptop in 6 hours. Leave a couple of interesting videos out for showing the final results. We can do two runs. One with SAM3 and one with masks you produce.
```

↗ [查看作者完整提示词](https://x.com/LearnOpenCV/status/2097123587920634003) · [观看演示](https://x.com/LearnOpenCV/status/2097122818815299892)

[返回案例目录](#cases)

## 其他分类

- [🧩 应用与网站](apps.zh-CN.md)
- [✨ 设计与创意](design.zh-CN.md)
- [🏛️ 三维与空间创作](3d.zh-CN.md)
- [🎬 视频与叙事](video.zh-CN.md)
- [🖱️ 电脑操作与自动化](automation.zh-CN.md)
- [🎮 游戏与仿真](games.zh-CN.md)
