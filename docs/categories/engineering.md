# 🛠️ GPT-6 Astra — Engineering & prototyping

[English](engineering.md) · [简体中文](engineering.zh-CN.md) · [Home](../../README.md) · [Full gallery](../gallery.md)

Engineering workflows, physical prototypes and production-ready systems.

**2 cases**

Prompt labels describe how much text is shown here. For excerpts, follow the original prompt link for the complete text.

<a id="cases"></a>

## Choose a case

- [A buildable Microduck robot prototype](#microduck-robot-prototype) · **Full prompt**
- [Hands-off segmentation model training](#microduck-segmentation-training) · **Full prompt**

<a id="microduck-robot-prototype"></a>

### A buildable Microduck robot prototype

**Full prompt** · [Original prompt](https://x.com/DeRonin_/status/2096567918859354155)

[![Robot prototyper showing printable Microduck components](https://pbs.twimg.com/amplify_video_thumb/2096567835569053696/img/HRjmvb9ZAkTklImX?format=webp&name=medium)](https://x.com/DeRonin_/status/2096567918859354155)

A robot-prototyping app turns a tiny brief into printable parts, movement-clearance checks, motor calculations, a priced bill of materials and assembly instructions.

**Creator**: [@DeRonin_](https://x.com/DeRonin_/status/2096567918859354155) · 2026-09-06<br>
**Tools & techniques**: Robotics, 3D printing, Bill of materials

**How it works**

Start with the desired robot, then iterate from concept geometry through mechanical checks, sourcing and build documentation until every part is ready for fabrication.

**What to know**

Although the author highlights the opening one-line prompt, the finished workflow took about 45 minutes and five prompts; physical assembly is proposed rather than demonstrated.

**Prompt**

```text
prototype me a full Microduck
```

↗ [Read the original prompt](https://x.com/DeRonin_/status/2096567918859354155) · [Watch the demo](https://x.com/DeRonin_/status/2096567918859354155)

[Back to case list](#cases)


<a id="microduck-segmentation-training"></a>

### Hands-off segmentation model training

**Full prompt** · [Original prompt](https://x.com/LearnOpenCV/status/2097123587920634003)

[![Side-by-side Microduck instance-segmentation model predictions](https://pbs.twimg.com/amplify_video_thumb/2097122679845449728/img/g0gMKyOCYKoBvXSM.jpg)](https://x.com/LearnOpenCV/status/2097122818815299892)

Astra gathers public Microduck media, builds a provenance-aware dataset, produces two competing mask sets and trains two RF-DETR-Seg-M models without human-supplied labels.

**Creator**: [@LearnOpenCV](https://x.com/LearnOpenCV/status/2097122818815299892) · 2026-09-08<br>
**Tools & techniques**: Computer vision, Roboflow, RF-DETR, SAM3

**How it works**

Give Astra a signed-in Roboflow account, the public asset source, a model target and held-out evaluation requirements. The author reports both cloud training runs were ready in about 93 minutes.

**What to know**

The run used a Roboflow account with 50 credits. The comparison held out complete video groups and froze both datasets before evaluation.

**Prompt**

```text
Get all images and videos of microducks from here pollen-robotics.com/microduck/. Generate masks and train RF-DETR-Seg-M using Roboflow.com. I will be flying in a few hours. I want to make sure the training run is set up and running even after I close this laptop in 6 hours. Leave a couple of interesting videos out for showing the final results. We can do two runs. One with SAM3 and one with masks you produce.
```

↗ [Read the original prompt](https://x.com/LearnOpenCV/status/2097123587920634003) · [Watch the demo](https://x.com/LearnOpenCV/status/2097122818815299892)

[Back to case list](#cases)

## Other categories

- [🧩 Apps & websites](apps.md)
- [✨ Design & creative work](design.md)
- [🏛️ 3D & spatial creation](3d.md)
- [🎬 Video & storytelling](video.md)
- [🖱️ Computer use & automation](automation.md)
- [🎮 Games & simulations](games.md)
