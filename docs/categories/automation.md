# 🖱️ GPT-6 Astra — Computer use & automation

[English](automation.md) · [简体中文](automation.zh-CN.md) · [Home](../../README.md) · [Full gallery](../gallery.md)

Browser control, computer-use workflows and autonomous production tasks.

**5 cases**

Prompt labels describe how much text is shown here. For excerpts, follow the original prompt link for the complete text.

<a id="cases"></a>

## Choose a case

- [A browser-driven walk through Kyoto](#kyoto-walking-tour) · **Full prompt**
- [A multi-agent operations dashboard](#multi-agent-operations-dashboard) · **Full prompt**
- [Script-driven After Effects motion graphics](#after-effects-kangaroo-motion) · **Prompt excerpt**
- [An autonomous theme-and-variations composition](#clares-dragoons-variations) · **Prompt excerpt**
- [A cinematic boxing color grade in Premiere Pro](#premiere-boxing-color-grade) · **Full prompt**

<a id="kyoto-walking-tour"></a>

### A browser-driven walk through Kyoto

**Full prompt** · [Original prompt](https://x.com/MatthewBerman/status/2095595901784052075)

[![Browser-controlled visual walking tour through Kyoto](https://pbs.twimg.com/amplify_video_thumb/2095563428261924864/img/EEjsPKMM54sdio16?format=webp&name=medium)](https://x.com/MatthewBerman/status/2095595901784052075)

From a four-word request, Astra uses browser control to assemble and present a visual walking tour through Kyoto.

**Creator**: [@MatthewBerman](https://x.com/MatthewBerman/status/2095595901784052075) · 2026-09-04<br>
**Tools & techniques**: Browser control, Travel, Computer use

**How it works**

State the destination and desired experience, then let Astra navigate the browser and compose the tour autonomously.

**What to know**

The public post shows the browser-control demonstration but does not enumerate its intermediate browsing steps or source-selection criteria.

**Prompt**

```text
Create a walking tour through Kyoto.
```

↗ [Read the original prompt](https://x.com/MatthewBerman/status/2095595901784052075) · [Watch the demo](https://x.com/MatthewBerman/status/2095595901784052075)

[Back to case list](#cases)


<a id="multi-agent-operations-dashboard"></a>

### A multi-agent operations dashboard

**Full prompt** · [Original prompt](https://x.com/DeepDive_KR/status/2097480105694318999)

[![Dark multi-agent dashboard with seven active agents and operational controls](https://pbs.twimg.com/amplify_video_thumb/2097478821914243072/img/B02wcISnsZyKZtSa.jpg)](https://x.com/DeepDive_KR/status/2097480105694318999)

Astra builds a polished control center for seven agents, covering task assignment, live activity, run history, pause and retry controls, approvals and scheduled execution.

**Creator**: [@DeepDive_KR](https://x.com/DeepDive_KR/status/2097480105694318999) · 2026-09-09<br>
**Tools & techniques**: Multi-agent, Operations dashboard, Task orchestration

**How it works**

Describe the desired agent lifecycle and dashboard controls in one compact brief. The author used Medium effort and reports that the first build took about 27 minutes.

**What to know**

The author says the dashboard still needs additional work before the agents can perform real production tasks, and that accumulated Codex project context may have influenced the result.

**Prompt**

```text
필요한 모든 에이전트 생성하고, 각 역할에 맞는 하네스 구축하고, 각 에이전트별 작업 상황 및 기록을 볼 수 있고 제어하면서 새로운 업무까지 할당할 수 있고, 에이전트를 즉시 생성도 할 수 있는 관리 대시보드 구축해줘
```

↗ [Read the original prompt](https://x.com/DeepDive_KR/status/2097480105694318999) · [Watch the demo](https://x.com/DeepDive_KR/status/2097480105694318999)

[Back to case list](#cases)


<a id="after-effects-kangaroo-motion"></a>

### Script-driven After Effects motion graphics

**Prompt excerpt** · [Original prompt](https://x.com/Nyto_vd/status/2097499892918997382)

[![Flat-design boxing kangaroo motion graphic made in After Effects](https://pbs.twimg.com/amplify_video_thumb/2097497983826956288/img/slA7YZTPz1cCzWWW.jpg)](https://x.com/Nyto_vd/status/2097499735942893726)

Astra creates an eight-second flat-design motion graphic in After Effects, with a boxing kangaroo, an impact transition and an editable title card.

**Creator**: [@Nyto_vd](https://x.com/Nyto_vd/status/2097499735942893726) · 2026-09-09<br>
**Tools & techniques**: After Effects, Motion graphics, Scripted automation

**How it works**

Define the canvas, frame rate, asset restriction and two scenes in detail. Astra writes the composition script first and executes it inside After Effects instead of driving every edit through the interface.

**What to know**

The published result is a compact eight-second demonstration and relies on the native After Effects features and plug-ins already installed in the author's environment.

**Prompt**

> ありがとう。次は、After Effectsを操作して、フラットデザインの、繊細かつクオリティの高いモーショングラフィックスを制作してほしい。
動画仕様：1920 × 1080、30 fps
制作条件：指示内容にあるオブジェクトは外部素材を使用しない。
AfterEffectsの基本機能およびインストールされているプラグインを使用して制作する。

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/Nyto_vd/status/2097499892918997382) · [Watch the demo](https://x.com/Nyto_vd/status/2097499735942893726)

[Back to case list](#cases)


<a id="clares-dragoons-variations"></a>

### An autonomous theme-and-variations composition

**Prompt excerpt** · [Original prompt](https://x.com/doodlestein/status/2097838353504719199)

[![Piano score and rendered performance for Clare’s Dragoons variations](https://pbs.twimg.com/amplify_video_thumb/2097835787542732805/img/he4y8zVJKFgYbrjx.jpg)](https://x.com/doodlestein/status/2097837264529203426)

Astra turns the traditional Irish song “Clare’s Dragoons” into a complete piano theme and twelve structured variations, producing a score, MIDI and a rendered performance through an inspectable multi-agent workflow.

**Creator**: [@doodlestein](https://x.com/doodlestein/status/2097837264529203426) · 2026-09-10<br>
**Tools & techniques**: Music composition, Codex skills, mtdt

**How it works**

A controller agent delegates the composition to a worker running Astra at xhigh, backed by a 320-skill music library and the mtdt CLI. The worker finds source notation, transcribes it into an internal representation, studies Mozart’s variation procedures, then composes, reviews and revises the score.

**What to know**

The result depends on the author’s closed-source music skill library and mtdt tooling, so the published prompt alone does not reproduce the full workflow. The author also notes that the model evaluates notation rather than listening to the rendered audio.

**Prompt**

> Compose and deliver a complete, attractive solo-piano “Theme and Twelve Variations on Clare’s Dragoons”, using the traditional Irish song with its “Vive La!” refrain. Begin by presenting the complete verse melody and chorus straight, with a newly composed, nicely textured piano accompaniment. Follow that with Variations I–XII, inspired by Mozart’s variation procedures in K.265, his Twelve Variations on “Ah, vous dirai-je, Maman” (Twinkle, Twinkle, Little Star). Make a coherent piece someone would enjoy playing and hearing.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/doodlestein/status/2097838353504719199) · [Watch the demo](https://x.com/doodlestein/status/2097837264529203426)

[Back to case list](#cases)


<a id="premiere-boxing-color-grade"></a>

### A cinematic boxing color grade in Premiere Pro

**Full prompt** · [Original prompt](https://x.com/adilinthewild/status/2098247449026715966)

[![Premiere Pro showing a cool cinematic grade applied to gym footage](https://pbs.twimg.com/amplify_video_thumb/2098246949958991872/img/kmfpMNcXrUkIysVM.jpg)](https://x.com/adilinthewild/status/2098247449026715966)

Astra operates Premiere Pro to reshape ordinary gym footage with a cool, low-key grade that gives the sequence the mood of a boxing-film opening.

**Creator**: [@adilinthewild](https://x.com/adilinthewild/status/2098247449026715966) · 2026-09-11<br>
**Tools & techniques**: Premiere Pro, Color grading, Computer use

**How it works**

Supply the source footage, name Premiere Pro as the editing environment and describe the desired narrative mood; Astra then adjusts the grade inside the professional editor.

**What to know**

The instruction depends on the creator's supplied gym footage, and the cinematic result is a subjective look rather than a neutral color-correction reference.

**Prompt**

```text
Color grade this gym footage in Premiere Pro.
```

↗ [Read the original prompt](https://x.com/adilinthewild/status/2098247449026715966) · [Watch the demo](https://x.com/adilinthewild/status/2098247449026715966)

[Back to case list](#cases)

## Other categories

- [🧩 Apps & websites](apps.md)
- [✨ Design & creative work](design.md)
- [🏛️ 3D & spatial creation](3d.md)
- [🎬 Video & storytelling](video.md)
- [🛠️ Engineering & prototyping](engineering.md)
- [🎮 Games & simulations](games.md)
