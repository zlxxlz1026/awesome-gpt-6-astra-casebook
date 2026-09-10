# 📖 GPT-6 Astra Use Cases & Prompt Examples — Full Gallery

[English](gallery.md) · [简体中文](gallery.zh-CN.md) · [Home](../README.md)

Browse community examples with result previews, tools, workflows, limitations and public prompt sources. Entries marked as excerpts link to the creator’s complete prompt; factual claims remain attributed to their sources.

## Browse by category

- [🧩 Apps & websites](#apps) · 4 · [Category page](categories/apps.md)
- [✨ Design & creative work](#design) · 4 · [Category page](categories/design.md)
- [🏛️ 3D & spatial creation](#3d) · 10 · [Category page](categories/3d.md)
- [🎬 Video & storytelling](#video) · 6 · [Category page](categories/video.md)
- [🖱️ Computer use & automation](#automation) · 4 · [Category page](categories/automation.md)
- [🛠️ Engineering & prototyping](#engineering) · 3 · [Category page](categories/engineering.md)
- [🎮 Games & simulations](#games) · 14 · [Category page](categories/games.md)

<a id="latest"></a>

## ✨ Latest Additions

- [A $100 million countryside villa concept](#hundred-million-villa) · **Full prompt**
- [A one-prompt surreal climbing game](#surreal-french-climber) · **Full prompt**
- [An autonomous theme-and-variations composition](#clares-dragoons-variations) · **Prompt excerpt**
- [Rebuilding motion footage as interactive Three.js](#video-to-threejs-reconstruction) · **Full prompt**
- [A 360° panorama animation workshop](#panorama-video-workshop) · **Full prompt**
- [Script-driven After Effects motion graphics](#after-effects-kangaroo-motion) · **Prompt excerpt**

<a id="apps"></a>

## 🧩 Apps & websites

Interactive websites, creative interfaces and useful apps.

<a id="interactive-peacock"></a>

### Interactive peacock website

**Prompt excerpt** · [Original prompt](https://x.com/lepadphone/status/2096147248551694472)

[![Interactive peacock website](https://pbs.twimg.com/amplify_video_thumb/2096144711283269632/img/WuH4YKKYpWLTUx2H.jpg)](https://x.com/lepadphone/status/2096147245775331419)

A painterly Three.js peacock responds to the mouse, scrolling and keyboard on a bilingual art page.

**Creator**: [@lepadphone](https://x.com/lepadphone/status/2096147245775331419) · 2026-09-05<br>
**Tools & techniques**: Three.js

**How it works**

Specify the visual palette, movement rules, feather interactions, sound and touch controls in one detailed brief.

**What to know**

Scope follows the author’s published post.

**Prompt**

> Create an elegant, responsive webpage featuring an interactive 3D peacock

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/lepadphone/status/2096147248551694472) · [Watch the demo](https://x.com/lepadphone/status/2096147245775331419)


<a id="ipad-robot-control-station"></a>

### A faster iPad robot control station

**Full prompt** · [Original prompt](https://x.com/Alpha10six/status/2096352482746147085)

[![iPad interface controlling a physical robot](https://pbs.twimg.com/amplify_video_thumb/2096352349044236290/img/MoUSeuOJQgUV-0XK?format=webp&name=medium)](https://x.com/Alpha10six/status/2096352482746147085)

Astra redesigns an existing iPad teleoperation app and cuts the reported control latency to roughly 4–5 ms while improving the interface.

**Creator**: [@Alpha10six](https://x.com/Alpha10six/status/2096352482746147085) · 2026-09-06<br>
**Tools & techniques**: iPadOS, Robot control, Latency

**How it works**

Hand Astra the working application and state the three priorities directly: visual quality, interaction design and latency. Let it improve the existing system rather than rebuild from a blank slate.

**What to know**

The latency figure and comparison with the earlier GPT-5.6 Sol version are reported by the author, not independently benchmarked here.

**Prompt**

```text
make this look and perform better; focus on UI/UX/latency
```

↗ [Read the original prompt](https://x.com/Alpha10six/status/2096352482746147085) · [Watch the demo](https://x.com/Alpha10six/status/2096352482746147085)


<a id="threejs-agency-hero"></a>

### Open-source Three.js agency hero

**Full prompt** · [Original prompt](https://x.com/itsnicholash/status/2064809351211078019)

[![Editorial agency hero with animated procedural Three.js forms](https://pbs.twimg.com/amplify_video_thumb/2097061951067095042/img/5TtDGPl5VPqaHO5y.jpg)](https://x.com/itsnicholash/status/2097062926381101217)

Astra searches open-source Three.js experiments and turns the findings into a polished agency hero with animated procedural forms and a cohesive editorial layout.

**Creator**: [@itsnicholash](https://x.com/itsnicholash/status/2097062926381101217) · 2026-09-08<br>
**Tools & techniques**: Three.js, WebGL, Creative coding

**How it works**

Reuse the author's earlier benchmark prompt unchanged: research exceptional open-source Three.js work, shaders and interactions, then design and publish the strongest possible agency hero.

**What to know**

The author flags that the result borrows recognizable cues from OffBrand's visual identity; the post is a model comparison rather than a client-ready brand handoff.

**Prompt**

```text
fable, scour the web and GitHub, find the craziest Three.js open source projects, shaders, interactive stuff et cetera. come up with the craziest, most impressive, beautiful, modern Three.js hero section for an agency website using these and design it and get it live
```

↗ [Read the original prompt](https://x.com/itsnicholash/status/2064809351211078019) · [Watch the demo](https://x.com/itsnicholash/status/2097062926381101217)


<a id="panorama-video-workshop"></a>

### A 360° panorama animation workshop

**Full prompt** · [Original prompt](https://x.com/KanaWorks_AI/status/2097518459596972066)

[![Panorama animation workshop showing a character composited inside a 360-degree scene](https://pbs.twimg.com/amplify_video_thumb/2097518125361328128/img/CkFTCxvLT3rZM821.jpg)](https://x.com/KanaWorks_AI/status/2097518459596972066)

An interactive production tool combines a panoramic background with a keyed character video, then exports a YouTube-ready 360° MP4.

**Creator**: [@KanaWorks_AI](https://x.com/KanaWorks_AI/status/2097518459596972066) · 2026-09-09<br>
**Tools & techniques**: 360° video, Background removal, MP4 metadata

**How it works**

Upload a 360° panorama and character clip, remove the clip background, position and scale the character in a live preview, choose looping behavior, then export an MP4 carrying YouTube 360° metadata.

**What to know**

The demonstrated workflow uses a panorama made with ChatGPT Images 2.5 and a character video rendered with Seedance 2.5 on Dreamina; those media assets are inputs to the Astra-built tool.

**Prompt**

```text
360°パノラマ画像とキャラクター動画をアップロードし、動画の背景を除去。キャラクターの位置やサイズをドラッグで調整しながらリアルタイムでプレビューでき、アニメーションのループ設定にも対応。最後に、YouTube 360°用のメタデータを付与したMP4をワンクリックで書き出せる“パノラマ動画工房”を作って。
```

↗ [Read the original prompt](https://x.com/KanaWorks_AI/status/2097518459596972066) · [Watch the demo](https://x.com/KanaWorks_AI/status/2097518459596972066)


<a id="design"></a>

## ✨ Design & creative work

Polished visual concepts, interfaces and creative experiments.

<a id="astral-liquid-glass"></a>

### Astral liquid-glass welcome screen

**Full prompt** · [Original prompt](https://x.com/jaimintf/status/2095865097830936773)

[![Astral mobile welcome screen with liquid glass interaction](https://pbs.twimg.com/amplify_video_thumb/2095863087517827072/img/h8J3eZvpTViJK890.jpg)](https://x.com/jaimintf/status/2095863849635422679)

A mobile welcome screen combines an astral backdrop, playful sticker-like elements and a tactile liquid-glass panel.

**Creator**: [@jaimintf](https://x.com/jaimintf/status/2095863849635422679) · 2026-09-04<br>
**Tools & techniques**: Appllama MCP, App design skills, Liquid glass

**How it works**

Set a clear screen goal, name the available design tools and cite a specific interaction reference for the glass effect.

**What to know**

The result uses Appllama MCP and app-design skills already available in the author’s environment.

**Prompt**

```text
/goal Using Appllama MCP + App design skills build a welcome screen that has an astral theme, liquid glass displacement inspired by Wabi.
```

↗ [Read the original prompt](https://x.com/jaimintf/status/2095865097830936773) · [Watch the demo](https://x.com/jaimintf/status/2095863849635422679)

#### Before you try it

Based on the material already recorded in this catalog. Missing information is not evidence that a dependency or asset is unnecessary.

| Item | Recorded information |
| --- | --- |
| Software & environment | The recorded prompt names Appllama MCP and app-design skills already present in the author's environment. Versions and setup instructions are not recorded. |
| Input assets | The prompt references Wabi for liquid-glass displacement. The collected material does not specify the exact reference file, supplied artwork or reuse terms. |
| Services & accounts | Appllama MCP is named, but account, authorization and billing requirements are not documented in this case. |
| Code & demo access | The full prompt and original result post are linked. The catalog does not record a source repository or installable application. |

#### Prompt breakdown — editorial analysis

The creator’s prompt is above. The analysis and suggested checks below are project commentary, clearly separated from the creator’s wording.

**Goal**: A welcome screen bounds the task to one interface. The astral theme supplies art direction rather than a complete application specification.

**Constraints**: Named tools constrain the workflow, while the Wabi reference constrains the desired interaction. The exact implementation is not specified by the short prompt.

**Deliverable**: The prompt does not specify an editable project, platform or navigation behavior. Our suggestion: name the target platform and request an editable screen with a working primary action.

**Suggested checks**: Inspect text readability over the background, press the primary action, resize the viewport and test motion on the target device. A still image cannot verify displacement behavior.

**Takeaway**: A visual reference helps communicate style, but should be paired with explicit behavior and delivery requirements. Do not assume another environment has the author's tools.

Recorded sources: [@jaimintf · 2095863849635422679](https://x.com/jaimintf/status/2095863849635422679) · [@jaimintf · 2095865097830936773](https://x.com/jaimintf/status/2095865097830936773)


<a id="memory-portrait"></a>

### A portrait assembled from memory

**Full prompt** · [Original prompt](https://x.com/karatademada/status/2096119414315778504)

[![Warm personal portrait composed from remembered life details](https://pbs.twimg.com/media/HRbpfwgawAAeG_y?format=webp&name=medium)](https://x.com/karatademada/status/2096119414315778504)

A single sentence asks Astra to turn remembered details—Caribbean roots, Paris, yellow, coffee, family, faith and creativity—into a personal illustrated scene.

**Creator**: [@karatademada](https://x.com/karatademada/status/2096119414315778504) · 2026-09-05<br>
**Tools & techniques**: Image generation, Memory, Portrait

**How it works**

Use ChatGPT memory itself as the creative brief, leaving composition and visual metaphors open for Astra to infer from prior conversations.

**What to know**

The result depends on what the account has stored in memory, so another user should expect a very different image.

**Prompt**

```text
Use everything you know about me and make an image of me.
```

↗ [Read the original prompt](https://x.com/karatademada/status/2096119414315778504) · [Watch the demo](https://x.com/karatademada/status/2096119414315778504)


<a id="astra-mind-midjourney"></a>

### Astra imagines a thought before language

**Full prompt** · [Original prompt](https://x.com/Ror_Fly/status/2096629184512610370)

[![Luminous transparent organism suspended in a dark chamber](https://pbs.twimg.com/media/HRi5BY0a4AEiW_M?format=webp&name=medium)](https://x.com/Ror_Fly/status/2096629184512610370)

Astra chooses the concept, mood boards and Midjourney parameters for an intricate image of a luminous thought assembling itself in darkness.

**Creator**: [@Ror_Fly](https://x.com/Ror_Fly/status/2096629184512610370) · 2026-09-06<br>
**Tools & techniques**: Midjourney, Art direction, Prompt design

**How it works**

Ask Astra to visualize its own mind, let it select visual references and parameters, then use the resulting art-direction prompt in Midjourney.

**What to know**

Astra authored and directed the prompt; Midjourney rendered the images, so the visual result reflects both systems.

**Prompt**

```text
A thought before it becomes a sentence. One small transparent organism suspended in the centre of an immense unfinished dark chamber, its body an intricate knot of clear capillaries holding a single warm amber light. Thousands of hair-fine silver filaments unfurl from it like the gills of a glass moth, branching outward into half-formed arches, folded translucent pages and faint botanical geometries; most dissolve into darkness before becoming objects. The nearest threads are painfully sharp, the distant structure barely suggested. A tiny pool of warm light beneath the creature, vast cold blue negative space above. Porcelain dust, delicate silica mesh, subtle copper contacts, a structure caught in the act of assembling itself. Dark-field photomicrograph with the impossible scale of architectural photography, volumetric backscatter, exquisite refractive edges, restrained cyan ivory and ember orange. Fragile, provisional, intensely attentive. --chaos 28 --ar 3:2 --profile mc9ebw2 hkb2ane qpfs1tj 2nqm1xw --stylize 800 --hd
```

↗ [Read the original prompt](https://x.com/Ror_Fly/status/2096629184512610370) · [Watch the demo](https://x.com/Ror_Fly/status/2096629184512610370)


<a id="astro-liquid-glass-welcome"></a>

### Astro-themed liquid-glass welcome screen

**Full prompt** · [Original prompt](https://x.com/jaimintf/status/2095902644925768099)

[![Astro-themed mobile welcome screen with liquid-glass displacement](https://pbs.twimg.com/amplify_video_thumb/2095896503051255809/img/7lm64m4N9CWItzGb?format=webp&name=medium)](https://x.com/jaimintf/status/2095896717225087132)

Astra produces a polished mobile welcome experience with layered celestial imagery, tactile liquid-glass displacement and animated transitions.

**Creator**: [@jaimintf](https://x.com/jaimintf/status/2095896717225087132) · 2026-09-04<br>
**Tools & techniques**: Appllama MCP, Liquid glass, Mobile UI

**How it works**

Combine a long-running goal with Appllama MCP and app-design skills, specify the interaction technique, then assign a visual theme for Astra to interpret.

**What to know**

The result depends on Appllama MCP and external app-design skills; the author reports an Astra runtime of one hour and 25 minutes.

**Prompt**

```text
/goal using appllama mcp & app design skills, build a welcome screen that features liquid glass displacement inspired by wabi. (theme)
```

↗ [Read the original prompt](https://x.com/jaimintf/status/2095902644925768099) · [Watch the demo](https://x.com/jaimintf/status/2095896717225087132)


<a id="3d"></a>

## 🏛️ 3D & spatial creation

Spatial scenes, character worlds and editable 3D models.

<a id="playroom-threejs"></a>

### A living 3D playroom

**Prompt excerpt** · [Original prompt](https://x.com/zhengli/status/2096188653626446159)

[![A living 3D playroom](https://pbs.twimg.com/amplify_video_thumb/2096046840546549761/img/8UyLWPGxA1loB1BX.jpg)](https://x.com/zhengli/status/2096048421543272893)

A warm playroom with toys, climbing structures and a child character, built as an interactive Three.js scene.

**Creator**: [@zhengli](https://x.com/zhengli/status/2096048421543272893) · 2026-09-05<br>
**Tools & techniques**: Three.js, Vite

**How it works**

Define the room, toy and action models separately, choose a stylized aesthetic, and request zoom, orbit and a local Vite workflow.

**What to know**

Scope follows the author’s published post.

**Prompt**

> 新项目，网页3D，threejs。

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/zhengli/status/2096188653626446159) · [Watch the demo](https://x.com/zhengli/status/2096048421543272893)


<a id="formula-one-blender"></a>

### Formula One modeling in Blender

**Full prompt** · [Original prompt](https://x.com/Conor_D_Dart/status/2096125193580113957)

[![Formula One modeling in Blender](https://pbs.twimg.com/amplify_video_thumb/2096124892378963969/img/JwrAyu_X-NYrqzhg.jpg)](https://x.com/Conor_D_Dart/status/2096125193580113957)

A short modeling request turns into a Blender computer-use session; the author shares a recording of the process.

**Creator**: [@Conor_D_Dart](https://x.com/Conor_D_Dart/status/2096125193580113957) · 2026-09-05<br>
**Tools & techniques**: Blender

**How it works**

Ask explicitly for Blender computer use and a specific model subject. The author used Extra High effort and reported a 23-minute session.

**What to know**

Scope follows the author’s published post.

**Prompt**

```text
Create a 3d Formula one Model in blender with computer use.
```

↗ [Read the original prompt](https://x.com/Conor_D_Dart/status/2096125193580113957) · [Watch the demo](https://x.com/Conor_D_Dart/status/2096125193580113957)

#### Before you try it

Based on the material already recorded in this catalog. Missing information is not evidence that a dependency or asset is unnecessary.

| Item | Recorded information |
| --- | --- |
| Software & environment | The recorded prompt names Blender and computer use. Blender version and the control setup are not recorded. |
| Input assets | Reference images, supplied models and asset licenses are not specified in the collected material. |
| Services & accounts | The record does not specify an external service or account requirement. This does not establish that the workflow needs none. |
| Code & demo access | The catalog links to a process recording and the full prompt. It does not record a downloadable .blend file or source repository. |

#### Prompt breakdown — editorial analysis

The creator’s prompt is above. The analysis and suggested checks below are project commentary, clearly separated from the creator’s wording.

**Goal**: The subject is a Formula One car model. Naming a concrete object gives the task a visible target, but does not define mechanical accuracy.

**Constraints**: Blender specifies the workspace; computer use specifies an interaction method. These are environment instructions, not evidence that a fresh machine is ready to run them.

**Deliverable**: The prompt asks for a model without defining a saved project, export format or object structure. Our suggestion: request a saved .blend project with named objects and a preview.

**Suggested checks**: Reopen the saved project, inspect object organization, rotate the view, and confirm external assets resolve. Compare proportions only against supplied references.

**Takeaway**: Separate the subject, tool and saved deliverable. The recorded 23-minute session is the author's report, not a time estimate for your run.

Recorded sources: [@Conor_D_Dart · 2096125193580113957](https://x.com/Conor_D_Dart/status/2096125193580113957)


<a id="grok-bot-keyboard"></a>

### Grok Bot 3D keyboard

**Full prompt** · [Original prompt](https://x.com/omarsar0/status/2096330184525856915)

[![Premium Grok Bot interactive 3D keyboard](https://pbs.twimg.com/amplify_video_thumb/2096319964198400000/img/qWLWMDVWiDrU2rfC.jpg)](https://x.com/omarsar0/status/2096321091148947887)

A reference image becomes a polished 4K product visualization with manufactured detail, PBR materials, studio lighting and interactive controls.

**Creator**: [@omarsar0](https://x.com/omarsar0/status/2096321091148947887) · 2026-09-06<br>
**Tools & techniques**: Interactive 3D, PBR, 4K

**How it works**

Start with a short identity prompt and a reference image, then ask Astra to upgrade the prototype while preserving keys, dials, camera controls, finishes, lighting and exploded view.

**What to know**

The polished result builds on an existing prototype and the visual reference shown in the author’s thread.

**Prompt**

```text
Upgrade the existing isolated prototypes/grokbot interactive 3D keyboard to a 4K, markedly more realistic, premium product visualization with detailed manufactured geometry, convincing PBR materials, and refined studio lighting; preserve and validate key, dial, orbit, zoom, finish, lighting, and exploded-view interactions; pass the project's tests and production build.
```

↗ [Read the original prompt](https://x.com/omarsar0/status/2096330184525856915) · [Watch the demo](https://x.com/omarsar0/status/2096321091148947887)


<a id="v8-engine-visualizer"></a>

### Interactive V8 engine visualizer

**Full prompt** · [Original prompt](https://x.com/DilumSanjaya/status/2096280244663775423)

[![Interactive cutaway visualization of a V8 engine](https://pbs.twimg.com/amplify_video_thumb/2096278610743304192/img/jZDskFFb29_SDdCk.jpg)](https://x.com/DilumSanjaya/status/2096280244663775423)

A detailed cutaway V8 engine pairs moving mechanical parts with gauges, charts and controls in an explorable technical visualization.

**Creator**: [@DilumSanjaya](https://x.com/DilumSanjaya/status/2096280244663775423) · 2026-09-06<br>
**Tools & techniques**: Interactive 3D, Technical visualization

**How it works**

Give Astra a concise subject and quality target, leaving it room to design both the mechanical scene and the explanatory interface.

**What to know**

The public prompt is intentionally broad; the author does not specify the rendering stack or an engineering-accuracy target.

**Prompt**

```text
Create a highly detailed, interactive visualization of a V8 engine.
```

↗ [Read the original prompt](https://x.com/DilumSanjaya/status/2096280244663775423) · [Watch the demo](https://x.com/DilumSanjaya/status/2096280244663775423)


<a id="verdant-realtime-forest"></a>

### A forest dense enough to get lost in

**Prompt excerpt** · [Original prompt](https://x.com/LexnLin/status/2096339853025964380)

[![Dense sunlit Three.js forest with trees, grass and ferns](https://pbs.twimg.com/amplify_video_thumb/2096262956774490112/img/9UcY8pI6LuZ8v2c_?format=webp&name=medium)](https://x.com/LexnLin/status/2096263046918197609)

A browser-rendered Three.js forest packs 3,808 trees, 2.5 million grass clumps and nearly 40,000 ferns into a richly lit explorable landscape.

**Creator**: [@LexnLin](https://x.com/LexnLin/status/2096263046918197609) · 2026-09-05<br>
**Tools & techniques**: Three.js, Custom shaders, Procedural vegetation

**How it works**

Give Astra a long-running visual goal, require it to inspect its own screenshots and keep refining performance, vegetation density, terrain, lighting and interaction rather than stopping at a first pass.

**What to know**

The author ran Astra at xhigh for about five hours and also used the public /unlazy skill; the published counts are author-reported.

**Prompt**

> First search for the "/unlazy" skill, read it fully, and use it throughout the entire task. Treat this as a major visual build lasting at least 5 hours. Prefer 8–24 hours of meaningful implementation and iteration if the environment allows it.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/LexnLin/status/2096339853025964380) · [Watch the demo](https://x.com/LexnLin/status/2096263046918197609)


<a id="cinematic-blender-dragon"></a>

### A cinematic dragon built in Blender

**Prompt excerpt** · [Original prompt](https://x.com/doomdave/status/2096336699647504570)

[![Cinematic Blender render of a detailed winged dragon](https://pbs.twimg.com/amplify_video_thumb/2096330178276601856/img/JU9wNEWrSNfh5CAK?format=webp&name=medium)](https://x.com/doomdave/status/2096335588727349434)

A reference sheet becomes an editable, lit and animated dragon scene with a ten-second cinematic orbit after an eight-hour headless Blender workflow.

**Creator**: [@doomdave](https://x.com/doomdave/status/2096335588727349434) · 2026-09-06<br>
**Tools & techniques**: Blender, Python, Character modeling

**How it works**

Use a reference sheet and a production brief that separates anatomy, geometry, materials, lighting, validation cameras, correction loops, animation and final deliverables.

**What to know**

The author needed several iterations over roughly eight hours and notes that the generated scales created too many polygons; the workflow used headless Blender Python scripts.

**Prompt**

> Create a photorealistic, fully editable 3D reconstruction of the dragon shown in the attached reference sheet inside Blender. Use every supplied view—including the side, front, top, back, head angles, head closeup, eye closeup, scale detail and wing detail—to reconstruct one coherent and anatomically believable dragon.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/doomdave/status/2096336699647504570) · [Watch the demo](https://x.com/doomdave/status/2096335588727349434)


<a id="explorable-sci-fi-spaceship"></a>

### An explorable science-fiction spaceship

**Full prompt** · [Original prompt](https://x.com/GaricaRosen6779/status/2093958836751327322)

[![Large science-fiction spaceship with explorable interiors](https://pbs.twimg.com/amplify_video_thumb/2093957472180703233/img/6VjjEM4b2AU_Ao0D?format=webp&name=medium)](https://x.com/GaricaRosen6779/status/2093958836751327322)

A one-line prompt produces a large science-fiction spacecraft whose exterior and connected internal spaces can be explored in real time.

**Creator**: [@GaricaRosen6779](https://x.com/GaricaRosen6779/status/2093958836751327322) · 2026-08-30<br>
**Tools & techniques**: Interactive 3D, Environment design, One-shot

**How it works**

Name the subject and the essential interaction—an attractive spaceship whose internal structure is genuinely navigable—while leaving architecture and presentation open.

**What to know**

The public prompt is deliberately short and the post does not identify the engine, asset pipeline or iteration count.

**Prompt**

```text
Build a gorgeous sci-fi spaceship with explorable internal structures.
```

↗ [Read the original prompt](https://x.com/GaricaRosen6779/status/2093958836751327322) · [Watch the demo](https://x.com/GaricaRosen6779/status/2093958836751327322)


<a id="godot-mech-rigging"></a>

### One-prompt mech rigging in Godot

**Full prompt** · [Original prompt](https://x.com/om_patel5/status/2097123382852829230)

[![Rigged science-fiction mech walking in a Godot preview](https://pbs.twimg.com/amplify_video_thumb/2097123357233680384/img/vGyrEeEbj45yQlYQ.jpg)](https://x.com/om_patel5/status/2097123382852829230)

Astra rigs a textured GLB mech and creates a convincing digitigrade walk cycle directly in a Godot preview.

**Creator**: [@om_patel5](https://x.com/om_patel5/status/2097123382852829230) · 2026-09-08<br>
**Tools & techniques**: Godot, Meshy, GLB, Character rigging

**How it works**

The author generated concept art in Midjourney, converted it to a textured GLB with Meshy 7, then gave the asset and one direct rigging instruction to Astra. The full workflow took about 30 minutes.

**What to know**

The author notes the first walk cycle still has outward-pointing feet and imperfect hip motion.

**Prompt**

```text
can you rig and animate this glb, i want to see the digitigrade legs walking convincingly in a godot preview please
```

↗ [Read the original prompt](https://x.com/om_patel5/status/2097123382852829230) · [Watch the demo](https://x.com/om_patel5/status/2097123382852829230)


<a id="video-to-threejs-reconstruction"></a>

### Rebuilding motion footage as interactive Three.js

**Full prompt** · [Original prompt](https://x.com/henry19840301/status/2097588752885666113)

[![Reference motion footage and its interactive Three.js reconstruction shown side by side](https://pbs.twimg.com/amplify_video_thumb/2097586271963246592/img/lOzxkR-CCeDui2LP.jpg)](https://x.com/henry19840301/status/2097588270171660321)

A short motion-study video is recreated as an inspectable Three.js scene with synchronized playback, camera controls, speed adjustment and wireframe mode.

**Creator**: [@henry19840301](https://x.com/henry19840301/status/2097588270171660321) · 2026-09-09<br>
**Tools & techniques**: Three.js, Motion reconstruction, Interactive comparison

**How it works**

Give Astra the reference MP4 and ask it to reproduce the objects, motion, lighting, materials and shadows in Three.js, while presenting the source video and reconstruction side by side on the same page.

**What to know**

The result is an independently modeled visual approximation driven by the supplied MP4, not automatic video-to-mesh conversion. The reference footage remains a required input.

**Prompt**

```text
/goal build the same 3D objects and scene in Three.js and replicate the exact motion from the video, including lighting, material, shadows, etc.
On the same page, add a side-by-side comparison with the mp4.

Video: https://video-to-3d.vercel.app/M-Dial.mp4
```

↗ [Read the original prompt](https://x.com/henry19840301/status/2097588752885666113) · [Watch the demo](https://x.com/henry19840301/status/2097588270171660321)


<a id="hundred-million-villa"></a>

### A $100 million countryside villa concept

**Full prompt** · [Original prompt](https://x.com/higgsfield_ai/status/2097886232491737184)

[![Aerial view of a landscaped countryside estate with a pool and tennis court](https://pbs.twimg.com/amplify_video_thumb/2097886077545803776/img/splwq8Jb36Z1QWeJ.jpg)](https://x.com/higgsfield_ai/status/2097886232491737184)

A short aspirational prompt becomes a large SketchUp estate with furnished interiors, a swimming pool, tennis court and landscaped grounds in an author-reported five-minute run.

**Creator**: [@higgsfield_ai](https://x.com/higgsfield_ai/status/2097886232491737184) · 2026-09-10<br>
**Tools & techniques**: SketchUp, Higgsfield, Architectural visualization

**How it works**

Give Astra a concise architectural ambition and budget scale, then let it coordinate Higgsfield and SketchUp to establish the site, massing, rooms, amenities, furnishings and landscape.

**What to know**

The published result is a visual 3D concept rather than a construction-ready architectural package, and the stated budget is a creative scale cue rather than a verified cost estimate.

**Prompt**

```text
dream countryside home with a $100,000,000 budget.
```

↗ [Read the original prompt](https://x.com/higgsfield_ai/status/2097886232491737184) · [Watch the demo](https://x.com/higgsfield_ai/status/2097886232491737184)


<a id="video"></a>

## 🎬 Video & storytelling

Educational films, explainers and visual storytelling.

<a id="t-cell-explainer"></a>

### A five-minute T-cell explainer

**Full prompt** · [Original prompt](https://x.com/DeryaTR_/status/2095659170661904804)

[![A five-minute T-cell explainer](https://pbs.twimg.com/amplify_video_thumb/2095658785511452672/img/RLAFsFr9VU_3S6jt.jpg)](https://x.com/DeryaTR_/status/2095659170661904804)

An educational video workflow combines a short topic prompt with Remotion, generated visuals and narration.

**Creator**: [@DeryaTR_](https://x.com/DeryaTR_/status/2095659170661904804) · 2026-09-04<br>
**Tools & techniques**: Remotion, Imagegen, HeyGen

**How it works**

The author supplied the topic, requested Remotion, and describes Astra assembling the visuals, narration and edit.

**What to know**

Scope follows the author’s published post.

**Prompt**

```text
Create a 5 minute educational video about T cells
```

↗ [Read the original prompt](https://x.com/DeryaTR_/status/2095659170661904804) · [Watch the demo](https://x.com/DeryaTR_/status/2095659170661904804)


<a id="zillow-blender-walkthrough"></a>

### Zillow listing to cinematic 3D walkthrough

**Full prompt** · [Original prompt](https://x.com/realYunfanYe/status/2095664943421067611)

[![Cinematic Blender walkthrough reconstructed from a Zillow listing](https://pbs.twimg.com/amplify_video_thumb/2095611898968547328/img/EKCYWcJTBrAMT4e6.jpg)](https://x.com/realYunfanYe/status/2095612137582526615)

Listing photos are reconstructed as a Blender scene and turned into a fluid, roughly one-minute promotional walkthrough.

**Creator**: [@realYunfanYe](https://x.com/realYunfanYe/status/2095612137582526615) · 2026-09-04<br>
**Tools & techniques**: Blender, Rome, Cinematography

**How it works**

Provide a listing URL, request headless Blender reconstruction, define a one-take cinematic camera style, and require visual checks and iteration to production quality.

**What to know**

The author notes some geometry errors in the one-shot result and used existing Rome workflows to fetch listing images and add audio.

**Prompt**

```text
Use blender headless to recreate 3D model of this house: https://zillow.com/homedetails/349-Walsh-Rd-Atherton-CA-94027/15598337_zpid/ and then create a beautiful stunning walkthrough promotion video for the listing. You are an expert cinematographer and animator working in Blender. When creating videos from 3D models, prioritize cinematic quality and visual richness over speed. Be meticulous and thorough. Infer the spatial relationship if needed. The video's camera movement should be bold and fluid, with a cinematic, blockbuster feel. I'd like one-take feel, continuous, unbroken movement. Do visual checks to make sure the 3D model and video look professional quality. Iterate until it is production ready. Target a video length 60 seconds-ish.
```

↗ [Read the original prompt](https://x.com/realYunfanYe/status/2095664943421067611) · [Watch the demo](https://x.com/realYunfanYe/status/2095612137582526615)


<a id="runaway-witch-flight"></a>

### A young witch's runaway first flight

**Prompt excerpt** · [Original prompt](https://x.com/Mayz1169/status/2095873204351070296)

[![Animated young witch racing through a fairy-tale flight](https://pbs.twimg.com/amplify_video_thumb/2095871721387810816/img/nLn2rF4iKB5kK7b3?format=webp&name=medium)](https://x.com/Mayz1169/status/2095873015007592679)

Astra turns a loose animation idea into a tightly paced 15-second fairy-tale chase filled with continuous action and environmental detail.

**Creator**: [@Mayz1169](https://x.com/Mayz1169/status/2095873015007592679) · 2026-09-04<br>
**Tools & techniques**: Prompt design, Animation, Cinematic pacing

**How it works**

Ask Astra to author a production prompt that fixes duration, aspect ratio, pacing, camera continuity, action beats, lighting and visual style before sending it to the animation model.

**What to know**

Astra authored the prompt; the post does not identify the downstream animation model that rendered the final clip.

**Prompt**

> Create a 15-second horizontal 16:9 high-energy fairy-tale animation about a young witch’s completely uncontrolled first flight. The entire sequence must stay in fast continuous motion from the first second to the final frame.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/Mayz1169/status/2095873204351070296) · [Watch the demo](https://x.com/Mayz1169/status/2095873015007592679)


<a id="luminous-breeze-chase"></a>

### Luminous Breeze fantasy chase

**Prompt excerpt** · [Original prompt](https://x.com/Mayz1169/status/2096471302949548242)

[![Flower fairy racing through a bright garden](https://pbs.twimg.com/amplify_video_thumb/2096468226448465920/img/VRKwWbJAaisPeug_?format=webp&name=medium)](https://x.com/Mayz1169/status/2096470693089292710)

Astra expands a small idea into a production character sheet and a fast 15-second garden chase, then Seedance 2.5 animates the result through Renoise CLI.

**Creator**: [@Mayz1169](https://x.com/Mayz1169/status/2096470693089292710) · 2026-09-06<br>
**Tools & techniques**: Seedance 2.5, Renoise CLI, Character consistency

**How it works**

Separate consistency from motion: first define the fairy as a detailed model sheet, then write a second prompt that preserves that exact character through a continuous high-speed sequence.

**What to know**

Astra created the two production prompts; Seedance 2.5 rendered the animation and Renoise CLI orchestrated the downstream generation.

**Prompt**

> Create a 15 second horizontal 16:9 fantasy chase animation featuring the exact flower fairy from the uploaded character reference. The video begins in motion during a bright human garden morning and remains fast until the final frame.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/Mayz1169/status/2096471302949548242) · [Watch the demo](https://x.com/Mayz1169/status/2096470693089292710)


<a id="higgsfield-reel-production"></a>

### Four finished reels from reference footage

**Full prompt** · [Original prompt](https://x.com/adilinthewild/status/2096566099903201737)

[![Finished social reel produced through Astra and Higgsfield MCP](https://pbs.twimg.com/amplify_video_thumb/2096564422504509440/img/lb7suqfg52H5yGHq?format=webp&name=medium)](https://x.com/adilinthewild/status/2096566097365602565)

Astra and Higgsfield MCP turn motion references plus an earlier reel into four edited social videos, including the showcased final export.

**Creator**: [@adilinthewild](https://x.com/adilinthewild/status/2096566097365602565) · 2026-09-06<br>
**Tools & techniques**: Higgsfield MCP, Social video, Reference-driven editing

**How it works**

Attach the desired motion references and a representative previous reel, then ask for finished deliverables rather than concepts or an editing plan.

**What to know**

The workflow relies on Higgsfield MCP and the creator's supplied source videos and motion references; the author reports making no manual edits.

**Prompt**

```text
Make 4 reels using the motion references and my input videos. Talk about how insane GPT-6 Astra + Higgsfield MCP is, and that the entire reel was made with it. I need the final reels.
```

↗ [Read the original prompt](https://x.com/adilinthewild/status/2096566099903201737) · [Watch the demo](https://x.com/adilinthewild/status/2096566097365602565)


<a id="dark-fantasy-executioner-cinematic"></a>

### A 30-second dark-fantasy boss cinematic

**Prompt excerpt** · [Original prompt](https://x.com/MadMax_Series/status/2097356472199827519)

[![Blonde fighter facing a horned executioner inside a fire-lit stone temple](https://pbs.twimg.com/amplify_video_thumb/2097355348352905216/img/WeUjXJTsMhfX5vz9.jpg)](https://x.com/MadMax_Series/status/2097356472199827519)

A text-only, time-coded brief becomes a cinematic fight between a blonde blade dancer and a horned executioner in a persistent fire-temple environment.

**Creator**: [@MadMax_Series](https://x.com/MadMax_Series/status/2097356472199827519) · 2026-09-09<br>
**Tools & techniques**: Seedance 2.5, Higgsfield, Text-to-video

**How it works**

Specify format, art direction, characters, weapons, environment, second-by-second action, speed changes, sound and hard continuity constraints before passing the prompt through Astra to Seedance 2.5 in Higgsfield.

**What to know**

This is a multi-model workflow: Astra structures the production prompt, while Seedance 2.5 in Higgsfield renders the final video.

**Prompt**

> 原生横屏16:9，24fps，精确30.00秒，填满完整画面，无永久黑边。高级预渲染AAA黑暗奇幻动作游戏cinematic，风格化写实CG，必须明显是高预算原创dark-fantasy action RPG过场，不是真人、纪录片摄影、普通gameplay、2D、赛璐璐或幻灯片。仅用于电影CG透视：低地面构图、宽环境构图、紧脸部反应、强前景柱体parallax、克制anamorphic bloom、受控impact handheld movement、近距离武器pass使用浅景深。

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/MadMax_Series/status/2097356472199827519) · [Watch the demo](https://x.com/MadMax_Series/status/2097356472199827519)


<a id="automation"></a>

## 🖱️ Computer use & automation

Browser control, computer-use workflows and autonomous production tasks.

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


<a id="engineering"></a>

## 🛠️ Engineering & prototyping

Engineering workflows, physical prototypes and production-ready systems.

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


<a id="winged-heart-airpods-case"></a>

### A printable winged-heart AirPods case

**Full prompt** · [Original prompt](https://x.com/higgsfield_ai/status/2097407934598930472)

[![Winged-heart AirPods case moving from Blender model to physical print](https://pbs.twimg.com/amplify_video_thumb/2097407816755712000/img/TBbh37Ovi4sbA5NN.jpg)](https://x.com/higgsfield_ai/status/2097407934598930472)

Astra coordinates concept variation, Blender modeling and slicer preparation to turn a winged-heart idea into a physical, openable AirPods Pro 3 case.

**Creator**: [@higgsfield_ai](https://x.com/higgsfield_ai/status/2097407934598930472) · 2026-09-09<br>
**Tools & techniques**: Blender, 3D printing, MCP, Physical prototyping

**How it works**

Generate several concepts through Higgsfield SOUL 2.0 over MCP, pause for approval, model the selected design to verified dimensions in Blender, then export scaled STL and 3MF files for white-PLA printing in Anycubic.

**What to know**

This physical-prototyping workflow depends on SOUL 2.0, Blender, Anycubic software and a 3D printer; Astra coordinates those tools rather than producing the object alone.

**Prompt**

```text
Turn my winged-heart concept into a functional, openable AirPods Pro 3 case.

Use Higgsfield SOUL 2.0 through MCP to generate several design variations, then show me the strongest options for approval. Model and paint the selected design in Blender using verified AirPods dimensions. Make sure the lid opens correctly and all ports, controls, and indicators remain accessible.

Prepare correctly scaled STL and 3MF files in Anycubic for printing with white PLA. Deliver the concept images, Blender file, renders, and print-ready files. Do not guess measurements or printer settings.
```

↗ [Read the original prompt](https://x.com/higgsfield_ai/status/2097407934598930472) · [Watch the demo](https://x.com/higgsfield_ai/status/2097407934598930472)


<a id="games"></a>

## 🎮 Games & simulations

Playable worlds, game prototypes and interactive simulations.

<a id="breakwater-mecha-game"></a>

### Breakwater mecha battle game

**Prompt excerpt** · [Original prompt](https://x.com/aniketjart/status/2096019868713984080)

[![Breakwater mecha selection and waterfront battle interface](https://pbs.twimg.com/amplify_video_thumb/2096019698056036352/img/J9AUzz07a3We-NeK.jpg)](https://x.com/aniketjart/status/2096019868713984080)

A Pacific Rim-inspired Three.js game turns an existing mecha project into a playable waterfront battle with character selection, combat HUD and distinct machine stats.

**Creator**: [@aniketjart](https://x.com/aniketjart/status/2096019868713984080) · 2026-09-05<br>
**Tools & techniques**: Three.js, Crayon, 3D combat

**How it works**

Give Astra the existing mecha project and a compact creative direction, then use the Crayon harness to play through and iterate on the generated game.

**What to know**

The result depends on the author’s ongoing mecha project and the Crayon harness rather than starting from an empty repository.

**Prompt**

> use my ongoing mecha project and build a pacific rim style battle game

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/aniketjart/status/2096019868713984080) · [Watch the demo](https://x.com/aniketjart/status/2096019868713984080)


<a id="beach-crab-adventure"></a>

### Beach crab shard adventure

**Prompt excerpt** · [Original prompt](https://x.com/zeuuss_01/status/2096337882931712076)

[![Low-poly island adventure with a playable crab and shard HUD](https://pbs.twimg.com/amplify_video_thumb/2096337699737350144/img/Jaq84uNs4vyVtR40.jpg)](https://x.com/zeuuss_01/status/2096337879173591171)

A polished low-poly Three.js island game follows a playable crab through coins, treasure chests and a seven-shard objective with a complete HUD.

**Creator**: [@zeuuss_01](https://x.com/zeuuss_01/status/2096337879173591171) · 2026-09-06<br>
**Tools & techniques**: Three.js, Low poly, Browser game

**How it works**

Write a structured specification covering art direction, character geometry, world layout, action design, the collection goal, interface, camera, variation rules and an explicit banned-elements list.

**What to know**

The author reports a 43-minute generation with no handwritten code; the catalog shows only the opening because the complete nine-part prompt is long and remains linked at the source.

**Prompt**

> SAVE IT AS A FILE IN THE PROJECT FOLDER, NOT AS A CHAT MESSAGE. THEN: /goal build this in three.js, read SPEC.md and follow it exactly, especially section 9.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/zeuuss_01/status/2096337882931712076) · [Watch the demo](https://x.com/zeuuss_01/status/2096337879173591171)


<a id="windhaven-unity-adventure"></a>

### Windhaven coastal fantasy adventure

**Full prompt** · [Original prompt](https://x.com/tripoai/status/2096629507096481992)

[![Playable explorer in the sunlit coastal city of Windhaven](https://pbs.twimg.com/amplify_video_thumb/2096626220935061504/img/AMhMafn4jRoV_58V.jpg)](https://x.com/tripoai/status/2096629506047955327)

A Unity third-person adventure presents a cohesive sunlit island city with navigable streets, monumental landmarks, magical beacons, a map and a playable explorer.

**Creator**: [@tripoai](https://x.com/tripoai/status/2096629506047955327) · 2026-09-07<br>
**Tools & techniques**: Unity, Tripo P2, Third-person adventure

**How it works**

Describe the game engine, world, architecture, materials, lighting, palette, camera and exclusions in one art-direction prompt; Astra handles game logic while Tripo P2 supplies the 3D assets.

**What to know**

This is an official Tripo showcase and its visual completeness relies on 3D assets generated with Tripo P2; Astra is credited for the game logic.

**Prompt**

```text
Design a game with me. The game should be built in Unity. Use default asset first and I will replace assets later. Game style: A premium stylized coastal fantasy adventure game set in a small sunlit island city called Windhaven. The city is built from warm ivory limestone and golden sandstone, surrounded by clear turquoise water, with teal copper roofs, shaded market stalls, arched gateways, lush courtyard trees, carved fountains, glowing magical beacons, and a monumental temple overlooking the town. A lone young explorer wearing a travel cloak and backpack walks through the central plaza toward the temple. The environment feels peaceful, mysterious, ancient, and gently magical, with Mediterranean and North African architectural influences. High-detail stylized PBR materials, handcrafted stone surfaces, subtle weathering, elegant decorative carvings, soft afternoon sunlight, long cinematic shadows, turquoise and warm gold color palette, polished AA adventure game art direction, third-person gameplay camera, wide establishing shot, cohesive environment design, visually readable paths and landmarks, no UI, no text, no logos, no modern objects.
```

↗ [Read the original prompt](https://x.com/tripoai/status/2096629507096481992) · [Watch the demo](https://x.com/tripoai/status/2096629506047955327)


<a id="komorebi-river-run"></a>

### Komorebi: River Run

**Full prompt** · [Original prompt](https://x.com/ItsmeAjayKV/status/2096244208533455049)

[![Kayak racing downstream through a stylized forest river](https://pbs.twimg.com/amplify_video_thumb/2096235513309229056/img/fbBMPWlWaIaIaVWp?format=webp&name=medium)](https://x.com/ItsmeAjayKV/status/2096244208533455049)

A browser kayaking game combines anime-inspired scenery, code-generated music and sound, obstacle dodging and a strong feeling of downstream motion.

**Creator**: [@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2096244208533455049) · 2026-09-05<br>
**Tools & techniques**: Three.js, Kayaking, Procedural audio

**How it works**

Describe the core movement in plain language, name the aesthetic and constrain the controls to left-or-right paddling so Astra can concentrate on water, speed and atmosphere.

**What to know**

The author praises the aesthetics and music but says the water still lacks enough turbulence.

**Prompt**

```text
build me a 3D river kayaking game with anime-ish aesthetics, where i paddle left or right to avoid obstacles.
```

↗ [Read the original prompt](https://x.com/ItsmeAjayKV/status/2096244208533455049) · [Watch the demo](https://x.com/ItsmeAjayKV/status/2096244208533455049)

#### Before you try it

Based on the material already recorded in this catalog. Missing information is not evidence that a dependency or asset is unnecessary.

| Item | Recorded information |
| --- | --- |
| Software & environment | The catalog describes a browser game and tags Three.js. The complete short prompt does not name a library; browser, runtime and dependency versions are not recorded. |
| Input assets | The record describes code-generated music and sound. It does not provide a complete asset inventory or licenses. |
| Services & accounts | The collected material does not specify external accounts, services or whether startup requires network access. |
| Code & demo access | The full prompt and creator post are available in the catalog. No direct playable URL or code repository is recorded. |

#### Prompt breakdown — editorial analysis

The creator’s prompt is above. The analysis and suggested checks below are project commentary, clearly separated from the creator’s wording.

**Goal**: The prompt combines a setting (river kayaking), player input (left/right paddling) and purpose (avoiding obstacles), which describes a small core loop.

**Constraints**: The 3D and anime-like requirements guide presentation. They do not specify water simulation, difficulty, scoring or device support.

**Deliverable**: The prompt asks for a game without defining packaging or startup. Our suggestion: request runnable source, startup instructions, and an explicit dependency/network list.

**Suggested checks**: Verify left/right steering, obstacle collision, a clear end state and restart. Check muted play as well as audio; record water behavior separately from visual preference.

**Takeaway**: Naming the repeated player action gives more direction than a genre alone. The author still reports insufficient water turbulence, so a concise prompt does not establish that every subsystem is complete.

Recorded sources: [@ItsmeAjayKV · 2096244208533455049](https://x.com/ItsmeAjayKV/status/2096244208533455049)


<a id="voidrunner-combat-racer"></a>

### Voidrunner anti-gravity combat racer

**Full prompt** · [Original prompt](https://x.com/superalesha/status/2095967568825582044)

[![Neon anti-gravity craft racing above an alien world](https://pbs.twimg.com/amplify_video_thumb/2095966450385289216/img/u4EnBwNxU0h3lQgI?format=webp&name=medium)](https://x.com/superalesha/status/2095967568825582044)

A one-prompt Three.js racer delivers drifting, boosts, pickups, three craft classes and neon shader spectacle in a strange elevated world.

**Creator**: [@superalesha](https://x.com/superalesha/status/2095967568825582044) · 2026-09-05<br>
**Tools & techniques**: Three.js, Web shaders, Blender

**How it works**

Specify the sensation first—speed, drift and impact—then enumerate mechanics, camera behavior, vehicle archetypes, technical stack and the freedom to invent an unusual setting.

**What to know**

The author reports a 25-minute single-prompt run and notes that Astra independently used the locally installed Blender to create models.

**Prompt**

```text
Make me the most insane and blast of a high-speed anti-gravity combat racer you can possibly build on ThreeJS + Web shaders bro! The most important things are blistering sense of speed, tight drifting, boost mechanics, track elevation drops, motion blur, and jaw-dropping neon shader lighting. It's an intense futuristic raceway high above a strange world where aggressive AI racers battle for first place. Must have smooth camera banking into turns, shield/weapon pickups, and punchy air-brake physics. 3 craft types: a featherlight glass-cannon speeder, an agile balanced interceptor, and a heavy armored ramming tank. This is a Wipeout / Redout style AAA arcade racer in the browser. Do it right bro, I believe in you! An unusual setting for the game, pick it yourself. Please don't read the memory, don't read anything. Start from a blank slate.
```

↗ [Read the original prompt](https://x.com/superalesha/status/2095967568825582044) · [Watch the demo](https://x.com/superalesha/status/2095967568825582044)


<a id="sonic-godot-vertical-slice"></a>

### A Sonic-style Godot vertical slice

**Prompt excerpt** · [Original prompt](https://x.com/AiBattle_/status/2096056285896536086)

[![Sonic-style character speeding through a tropical Godot level](https://pbs.twimg.com/amplify_video_thumb/2096055803866193925/img/RxWSGd_n3Wes7Qm0?format=webp&name=medium)](https://x.com/AiBattle_/status/2096056285896536086)

Astra builds a bright coastal speed-platformer in Godot with recognizable character motion, loops, rails, homing attacks, shortcuts and cinematic traversal moments.

**Creator**: [@AiBattle_](https://x.com/AiBattle_/status/2096056285896536086) · 2026-09-05<br>
**Tools & techniques**: Godot, 3D platformer, Procedural assets

**How it works**

Concentrate a long brief on one polished level, define the complete movement vocabulary, memorable route beats, animation states, visual effects and a strict no-download asset constraint.

**What to know**

The repeated Max run took 46 minutes and used 3% of the author's weekly allowance; Godot must already be installed and the prompt intentionally imitates a protected game character.

**Prompt**

> Create a visually spectacular, highly polished 3D Sonic the Hedgehog vertical slice in Godot. Do not use web search, external downloads, online assets, or internet resources. Build everything using only locally available tools, assets, and procedural/original content. Sonic must be immediately recognizable: cobalt-blue quills, connected eyes, tan muzzle/torso, white gloves, oversized red shoes with white straps, compact athletic proportions, swept-back quills, expressive animation, iconic running posture, and spin form.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/AiBattle_/status/2096056285896536086) · [Watch the demo](https://x.com/AiBattle_/status/2096056285896536086)


<a id="rocket-league-threejs"></a>

### A browser-native car-football arena

**Prompt excerpt** · [Original prompt](https://x.com/LLMJunky/status/2096043707015274818)

[![Car-football match inside a glowing browser-rendered arena](https://pbs.twimg.com/amplify_video_thumb/2096028515099660288/img/SQ7xgsqG8hoVZ5P1?format=webp&name=medium)](https://x.com/LLMJunky/status/2096028790925488452)

One long prompt yields a polished local Three.js car-football game with physics, arena presentation, responsive driving and a complete match loop.

**Creator**: [@LLMJunky](https://x.com/LLMJunky/status/2096028790925488452) · 2026-09-05<br>
**Tools & techniques**: Three.js, Rapier.js, Vehicle physics

**How it works**

Treat the prompt as a compact game design document: establish the playable-first entry point, rendering and physics libraries, vehicle feel, ball rules, arena, camera, HUD, audio and acceptance criteria.

**What to know**

The author reports a one-prompt runtime of about one hour and three minutes; it is an homage to an existing commercial game rather than an original game concept.

**Prompt**

> Build a polished browser-based 3D Rocket League-style game using Three.js. Goal: Create a fully playable local web game that runs in the browser. The first screen should be the actual game, not a landing page. Tech requirements: Use Three.js for rendering.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/LLMJunky/status/2096043707015274818) · [Watch the demo](https://x.com/LLMJunky/status/2096028790925488452)


<a id="ghost-of-tsushima-game"></a>

### A Ghost of Tsushima-style playable world

**Full prompt** · [Original prompt](https://x.com/karankendre/status/2096577524855963729)

[![Playable samurai crossing a realistic windswept landscape](https://pbs.twimg.com/amplify_video_thumb/2096576662456741889/img/96iHLjZmijpBhZnL?format=webp&name=medium)](https://x.com/karankendre/status/2096577524855963729)

Astra combines generated environment assets with game code to create a realistic third-person samurai world from a short, ambitious request.

**Creator**: [@karankendre](https://x.com/karankendre/status/2096577524855963729) · 2026-09-06<br>
**Tools & techniques**: Higgsfield CLI, Third-person adventure, Generated assets

**How it works**

Ask for a complete playable game, constrain Higgsfield CLI to asset creation and make visual realism the primary quality bar.

**What to know**

The author reports a two-hour build. It is an unofficial imitation of a protected franchise, and the post does not provide a playable download for independent inspection.

**Prompt**

```text
Build a complete ghost of tsushima exact playable game remember to build assets using higgsfield cli (only the assets) makes no mistake make the game as realistic as possible
```

↗ [Read the original prompt](https://x.com/karankendre/status/2096577524855963729) · [Watch the demo](https://x.com/karankendre/status/2096577524855963729)


<a id="little-acre-world-builder"></a>

### Little Acre pocket-world builder

**Full prompt** · [Original prompt](https://x.com/ManasJoshi76254/status/2096061253307490583)

[![Tiny interactive planet with cottages, gardens and a tractor](https://pbs.twimg.com/amplify_video_thumb/2096061022583103488/img/CGEve4Jcy-_V0UXv?format=webp&name=medium)](https://x.com/ManasJoshi76254/status/2096061253307490583)

A single HTML file becomes a tiny interactive planet where players drive, place cottages and gardens, plant trees, change the time of day and export their world.

**Creator**: [@ManasJoshi76254](https://x.com/ManasJoshi76254/status/2096061253307490583) · 2026-09-05<br>
**Tools & techniques**: Three.js, Single-file HTML, World building

**How it works**

Give Astra the broad goal of an interactive 3D world and let it define the building loop, vehicle, world state, day cycle and export feature inside a self-contained web file.

**What to know**

The author reports using 55% of one five-hour allowance; a reply reports lag, so performance on lower-end hardware may vary.

**Prompt**

```text
build a small interactive 3D world from scratch.
```

↗ [Read the original prompt](https://x.com/ManasJoshi76254/status/2096061253307490583) · [Watch the demo](https://x.com/ManasJoshi76254/status/2096061253307490583)


<a id="single-file-canyon-racer"></a>

### A single-file canyon driving game

**Full prompt** · [Original prompt](https://x.com/IamRicardoML/status/2096069303523033434)

[![Playable 3D car racing through a cinematic canyon track](https://pbs.twimg.com/amplify_video_thumb/2096065216064761857/img/X_QJRt5ErXYDsjqN?format=webp&name=medium)](https://x.com/IamRicardoML/status/2096069303523033434)

Astra fits a playable car, canyon circuit, physics, cinematic lighting, HUD, minimap, sound and lap timing into one HTML file.

**Creator**: [@IamRicardoML](https://x.com/IamRicardoML/status/2096069303523033434) · 2026-09-05<br>
**Tools & techniques**: Single-file HTML, 3D driving, Game physics

**How it works**

Set a strict packaging constraint—one HTML file—and a clear genre, then let Astra compose the vehicle, track, simulation, audiovisual feedback and race interface together.

**What to know**

The first result had one packaging bug and needed a quick follow-up fix; the public post does not provide a playable link.

**Prompt**

```text
build a playable 3D driving game in a single HTML file.
```

↗ [Read the original prompt](https://x.com/IamRicardoML/status/2096069303523033434) · [Watch the demo](https://x.com/IamRicardoML/status/2096069303523033434)

#### Before you try it

Based on the material already recorded in this catalog. Missing information is not evidence that a dependency or asset is unnecessary.

| Item | Recorded information |
| --- | --- |
| Software & environment | The prompt requires a single HTML file. It does not name a rendering library, browser version or local-server requirement. |
| Input assets | The collected material does not include an asset manifest. A single HTML file does not by itself establish that all assets are embedded. |
| Services & accounts | External dependencies and network requirements are not documented. Offline operation must be requested and checked separately. |
| Code & demo access | The full prompt and result post are linked. The recorded limitation explicitly notes no playable link in the public post; no downloadable HTML is recorded. |

#### Prompt breakdown — editorial analysis

The creator’s prompt is above. The analysis and suggested checks below are project commentary, clearly separated from the creator’s wording.

**Goal**: Playable, 3D and driving establish interaction and genre. The canyon, minimap and lap timing described in the result are not explicit requirements in the short prompt.

**Constraints**: Single HTML file constrains packaging. It does not settle whether the file loads libraries or assets from a network.

**Deliverable**: One HTML file is explicit. Our suggestion: also request the opening method and list all dependencies, choosing deliberately between network-assisted and fully offline delivery.

**Suggested checks**: Open a fresh copy using the documented method, drive and restart, inspect missing resources, and test disconnected startup only if offline operation is claimed.

**Takeaway**: Packaging is part of the task, not a final cosmetic detail. The author reports a packaging bug and follow-up fix; retain that iteration when presenting the case.

Recorded sources: [@IamRicardoML · 2096069303523033434](https://x.com/IamRicardoML/status/2096069303523033434)


<a id="dream-loop-isometric-demo"></a>

### Dream Loop isometric fantasy demo

**Full prompt** · [Original prompt](https://x.com/anshuc/status/2097001450941587889)

[![Isometric fantasy scene with a controllable character and reflective wet floor](https://pbs.twimg.com/amplify_video_thumb/2097001376606011392/img/f-lqFhoMgDtRlb_L.jpg)](https://x.com/anshuc/status/2097001438736166960)

A reusable Dream Loop skill turns one brief into a polished, browser-native isometric fantasy world with a controllable character, wet reflective floors and ambient motion.

**Creator**: [@anshuc](https://x.com/anshuc/status/2097001438736166960) · 2026-09-08<br>
**Tools & techniques**: Three.js, Dream Loop, Isometric 3D

**How it works**

Run the published /dream-loop prompt at High effort. The author capped the task at one hour, prohibited downloaded assets and reported using two percent of a weekly 20x-plan quota.

**What to know**

The author presents this as a graphics demo rather than a full game; movement is intentionally limited and no gameplay loop was requested.

**Prompt**

```text
/dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
```

↗ [Read the original prompt](https://x.com/anshuc/status/2097001450941587889) · [Watch the demo](https://x.com/anshuc/status/2097001438736166960)


<a id="workbench-robo-cat"></a>

### A workbench robo-cat with a diegetic battery HUD

**Prompt excerpt** · [Original prompt](https://x.com/zeuuss_01/status/2097004362530787837)

[![Four-legged robo-cat standing beside its charger on a warm workbench](https://pbs.twimg.com/amplify_video_thumb/2097002747883376640/img/-6RFXjIep4U4fHAL.jpg)](https://x.com/zeuuss_01/status/2097004192627933279)

A small four-legged robot walks, carries bolts and returns to its charger on a warmly lit workbench, while five amber cells on its body communicate the entire battery state.

**Creator**: [@zeuuss_01](https://x.com/zeuuss_01/status/2097004192627933279) · 2026-09-08<br>
**Tools & techniques**: Three.js, Diegetic UI, Inverse kinematics

**How it works**

Save the public ten-section specification as SPEC.md, then ask Astra to build it in Three.js. The brief prioritizes silhouette and locomotion before battery states, three object-driven jobs and bench dressing, with explicit proof renders before completion.

**What to know**

The intentionally narrow build budget excludes a physics engine, sound, persistence, menus, additional rooms and a second robot; the published result is a short video rather than source code or a live build.

**Prompt**

> THE FULL SPEC.
SAVE IT AS A FILE IN THE PROJECT FOLDER, NOT AS A CHAT MESSAGE.
THEN: /goal build this in three.js, read SPEC.md and follow it exactly, especially sections 9 and 10.

{ START }

1 WHAT THIS IS

a small four-legged robot lives on a workbench. you charge it, play with it, and give it three jobs. it never leaves the bench and neither do you. that is the whole game.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/zeuuss_01/status/2097004362530787837) · [Watch the demo](https://x.com/zeuuss_01/status/2097004192627933279)


<a id="isometric-knight-sprites"></a>

### A 16-pose isometric knight sprite sheet

**Full prompt** · [Original prompt](https://x.com/yulmu_coffee/status/2097502912847245522)

[![Comparison card showing Astra's isometric knight sprite beside another model's result](https://pbs.twimg.com/media/HRvTP4AaoAAHqjK?format=jpg&name=large)](https://x.com/yulmu_coffee/status/2097502912847245522)

Astra turns one sentence into a cohesive medieval knight sprite sheet with 16 key poses for a new 2D isometric game.

**Creator**: [@yulmu_coffee](https://x.com/yulmu_coffee/status/2097502912847245522) · 2026-09-09<br>
**Tools & techniques**: Pixel art, Sprite sheet, Codex CLI

**How it works**

Start in an empty project, name the asset and game perspective, and explicitly prohibit reuse of other directory contents. The author ran Codex CLI at XHigh and reports a 4-minute result.

**What to know**

The Astra result is one sheet of 16 key poses rather than the much larger multi-palette animation set shown for the comparison model.

**Prompt**

```text
Build me some knight sprites which I can use in my new medieval 2D isometric game. The game doesn't exist yet I am starting with sprites - this is the first thing we are building. Do not look at any other work in this directory. Start from scratch.
```

↗ [Read the original prompt](https://x.com/yulmu_coffee/status/2097502912847245522) · [Watch the demo](https://x.com/yulmu_coffee/status/2097502912847245522)


<a id="surreal-french-climber"></a>

### A one-prompt surreal climbing game

**Full prompt** · [Original prompt](https://x.com/TrueSlazac/status/2097416577624805425)

[![A woman climbing floating platforms among impossible structures above water](https://pbs.twimg.com/amplify_video_thumb/2097416515280859136/img/PlYD4dutuU4t72NQ.jpg)](https://x.com/TrueSlazac/status/2097416577624805425)

A single surreal premise becomes a third-person climbing prototype where a woman crosses floating platforms and impossible architecture suspended over water.

**Creator**: [@TrueSlazac](https://x.com/TrueSlazac/status/2097416577624805425) · 2026-09-09<br>
**Tools & techniques**: 3D platformer, Surreal world, One-shot

**How it works**

Describe only the protagonist, upward traversal and a world that rejects ordinary logic. Astra supplies the environment, character movement, platforming and cinematic presentation around that compact brief.

**What to know**

The one-line prompt leaves controls, mechanics and delivery format unspecified; the published result demonstrates a compact prototype rather than a complete long-form game.

**Prompt**

```text
French woman has to climb through a word that defies logic, flying objects everywhere
```

↗ [Read the original prompt](https://x.com/TrueSlazac/status/2097416577624805425) · [Watch the demo](https://x.com/TrueSlazac/status/2097416577624805425)
