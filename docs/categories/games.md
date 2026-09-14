# 🎮 GPT-6 Astra — Games & simulations

[English](games.md) · [简体中文](games.zh-CN.md) · [Home](../../README.md) · [Full gallery](../gallery.md)

Playable worlds, game prototypes and interactive simulations.

**17 cases**

Prompt labels describe how much text is shown here. For excerpts, follow the original prompt link for the complete text.

<a id="cases"></a>

## Choose a case

- [Breakwater mecha battle game](#breakwater-mecha-game) · **Prompt excerpt**
- [Beach crab shard adventure](#beach-crab-adventure) · **Prompt excerpt**
- [Windhaven coastal fantasy adventure](#windhaven-unity-adventure) · **Full prompt**
- [Komorebi: River Run](#komorebi-river-run) · **Full prompt**
- [Voidrunner anti-gravity combat racer](#voidrunner-combat-racer) · **Full prompt**
- [A Sonic-style Godot vertical slice](#sonic-godot-vertical-slice) · **Prompt excerpt**
- [A browser-native car-football arena](#rocket-league-threejs) · **Prompt excerpt**
- [A Ghost of Tsushima-style playable world](#ghost-of-tsushima-game) · **Full prompt**
- [Little Acre pocket-world builder](#little-acre-world-builder) · **Full prompt**
- [A single-file canyon driving game](#single-file-canyon-racer) · **Full prompt**
- [Dream Loop isometric fantasy demo](#dream-loop-isometric-demo) · **Full prompt**
- [A workbench robo-cat with a diegetic battery HUD](#workbench-robo-cat) · **Prompt excerpt**
- [A 16-pose isometric knight sprite sheet](#isometric-knight-sprites) · **Full prompt**
- [A one-prompt surreal climbing game](#surreal-french-climber) · **Full prompt**
- [A living agent-based beehive](#living-beehive-simulation) · **Full prompt**
- [A playable game reconstructed from a mobile ad](#video-to-mobile-ad-game) · **Full prompt**
- [PaperRoute, a finished seven-day delivery game](#paperroute-full-game) · **Prompt excerpt**

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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


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

[Back to case list](#cases)


<a id="living-beehive-simulation"></a>

### A living agent-based beehive

**Full prompt** · [Original prompt](https://x.com/free_ai_guides/status/2099272059687932201)

[![Side-by-side living beehive simulations with bees, comb growth and honey storage](https://pbs.twimg.com/amplify_video_thumb/2099271943795179520/img/Y-I_Y6c1fsFvGUzL.jpg)](https://x.com/free_ai_guides/status/2099272047465800037)

Independent bee agents forage, return and build a hexagonal comb cell by cell while honey storage and the hive’s visible structure evolve without user input.

**Creator**: [@free_ai_guides](https://x.com/free_ai_guides/status/2099272047465800037) · 2026-09-14<br>
**Tools & techniques**: Agent-based simulation, Emergent behavior, Single-file HTML

**How it works**

Define the agents, construction rule, forage loop and autonomous growth, then leave the style, camera and ambient behavior to Astra inside a single self-contained HTML deliverable.

**What to know**

This is an emergent visual simulation, not a biological model of real colony behavior; the source presents Astra beside another model for comparison.

**Prompt**

```text
Build a living beehive simulation. Bees must act as independent agents that construct hexagonal comb cell by cell, leave to forage, return, and fill cells with honey so the hive visibly grows and changes over time without any input. How it is shown, what the bees and hive look like, and what else happens in the scene are your decisions. Everything about the design is your decision: style, colors, mood, environment, camera, level of detail, and any extra touches. Do not ask me any questions, make every choice yourself and build the most impressive version you can in a single attempt. Technical requirements: one single self-contained HTML file, no external models, images, sounds, or asset URLs of any kind (a JavaScript library from a CDN is fine). It must start running on its own the moment it loads, with no clicks needed, and run smoothly with no console errors.
```

↗ [Read the original prompt](https://x.com/free_ai_guides/status/2099272059687932201) · [Watch the demo](https://x.com/free_ai_guides/status/2099272047465800037)

[Back to case list](#cases)


<a id="video-to-mobile-ad-game"></a>

### A playable game reconstructed from a mobile ad

**Full prompt** · [Original prompt](https://x.com/noclipepe/status/2098870292336595276)

[![A mobile-ad game beside Astra’s playable reconstruction with gates, squads and zombies](https://pbs.twimg.com/amplify_video_thumb/2098544563514392576/img/pRXiVB43Pkub7Q7g.jpg)](https://x.com/noclipepe/status/2098545145381605431)

Astra studies a short gameplay clip and rebuilds its hidden rules as a browser game with upgrade gates, squad growth, destructible walls, enemy health, auto-shooting and a boss loop.

**Creator**: [@noclipepe](https://x.com/noclipepe/status/2098545145381605431) · 2026-09-12<br>
**Tools & techniques**: Video-to-game, Browser game, Gameplay inference

**How it works**

Upload the gameplay clip as the primary reference and ask Astra to infer controls, camera, movement, progression, combat, scoring and end states before implementing the complete playable loop.

**What to know**

The prompt depends on the uploaded reference clip, and inferred rules can diverge from the original game. The public post demonstrates the generated loop but does not link a source repository.

**Prompt**

```text
Use the uploaded gameplay video as the primary reference. Rebuild the game shown in the video as a polished, fully playable browser game. Do not just copy the visuals. First, infer the hidden gameplay system behind the footage:

- player controls
- camera behavior
- movement rules
- interactions
- progression
- upgrades
- enemy behavior
- collisions
- scoring
- win and fail conditions
- UI feedback
- pacing

Reconstruct any rules that are not explicitly shown but must exist for the gameplay in the video to make sense. Match the feel and structure of the reference as closely as possible while keeping the game stable, responsive, and actually fun to play. Do not ask questions. Make the necessary design decisions yourself. Build the complete playable experience in one shot.
```

↗ [Read the original prompt](https://x.com/noclipepe/status/2098870292336595276) · [Watch the demo](https://x.com/noclipepe/status/2098545145381605431)

[Back to case list](#cases)


<a id="paperroute-full-game"></a>

### PaperRoute, a finished seven-day delivery game

**Prompt excerpt** · [Original prompt](https://x.com/builtbysketch/status/2098773631249854478)

[![PaperRoute’s illustrated 3D paper-delivery game and newspaper-style interface](https://pbs.twimg.com/amplify_video_thumb/2098775794281828352/img/Hoy8EuS5JEPOFpLO.jpg)](https://x.com/builtbysketch/status/2098777028078211283)

Astra helps turn a paper-delivery concept into a hosted browser game with a deterministic riding loop, authored Blender assets, characters, weather, mobile controls, a newspaper-style website and leaderboard.

**Creator**: [@builtbysketch](https://x.com/builtbysketch/status/2098777028078211283) · 2026-09-12<br>
**Tools & techniques**: Three.js, Blender, Long-horizon build

**How it works**

Start from a concise game brief and a perspective reference, make the mechanics playable before applying art direction, then run engine and visual work as separate streams with Blender Python, review renders, isolated branches and repeated browser checks.

**What to know**

The published article provides the brief excerpt and an extensive build runbook. The finished result accumulated 90 commits, 39 tracked hours and many iterative prompts, so it should be read as a long-horizon workflow rather than a one-shot generation.

**Prompt**

> A week of deliveries from Monday to Sunday, subscribers and non-subscribers, dogs, cars, the diagonal camera. I also wanted it to be a native iOS build. As well as web.

Opening excerpt; the author’s complete prompt is linked below.

↗ [Read the original prompt](https://x.com/builtbysketch/status/2098773631249854478) · [Watch the demo](https://x.com/builtbysketch/status/2098777028078211283)

[Back to case list](#cases)

## Other categories

- [🧩 Apps & websites](apps.md)
- [✨ Design & creative work](design.md)
- [🏛️ 3D & spatial creation](3d.md)
- [🎬 Video & storytelling](video.md)
- [🖱️ Computer use & automation](automation.md)
- [🛠️ Engineering & prototyping](engineering.md)
