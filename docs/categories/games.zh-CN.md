# 🎮 GPT-6 Astra — 游戏与仿真

[English](games.md) · [简体中文](games.zh-CN.md) · [返回首页](../../README.zh-CN.md) · [完整图册](../gallery.zh-CN.md)

可游玩的世界、游戏原型与交互式仿真。

**13 个案例**

提示词标签表示本页展示的完整度。标为摘录的案例，请访问提示词原帖查看全文。

<a id="cases"></a>

## 选择案例

- [Breakwater 机甲战斗游戏](#breakwater-mecha-game) · **提示词摘录**
- [海岛螃蟹水晶冒险](#beach-crab-adventure) · **提示词摘录**
- [Windhaven 海滨幻想冒险](#windhaven-unity-adventure) · **完整提示词**
- [Komorebi：林隙河流](#komorebi-river-run) · **完整提示词**
- [Voidrunner 反重力战斗竞速](#voidrunner-combat-racer) · **完整提示词**
- [Sonic 风格 Godot 垂直切片](#sonic-godot-vertical-slice) · **提示词摘录**
- [浏览器原生汽车足球竞技场](#rocket-league-threejs) · **提示词摘录**
- [《对马岛之魂》风格可玩世界](#ghost-of-tsushima-game) · **完整提示词**
- [Little Acre 袖珍世界建造器](#little-acre-world-builder) · **完整提示词**
- [单文件峡谷驾驶游戏](#single-file-canyon-racer) · **完整提示词**
- [Dream Loop 等距幻想世界演示](#dream-loop-isometric-demo) · **完整提示词**
- [把电量显示做进机身的工作台机器猫](#workbench-robo-cat) · **提示词摘录**
- [包含 16 个姿势的等距骑士图集](#isometric-knight-sprites) · **完整提示词**

<a id="breakwater-mecha-game"></a>

### Breakwater 机甲战斗游戏

**提示词摘录** · [提示词原帖](https://x.com/aniketjart/status/2096019868713984080)

[![Breakwater 机甲选择与水岸战斗界面](https://pbs.twimg.com/amplify_video_thumb/2096019698056036352/img/J9AUzz07a3We-NeK.jpg)](https://x.com/aniketjart/status/2096019868713984080)

把已有机甲项目扩展成《环太平洋》风格的 Three.js 水岸战斗游戏，包含角色选择、战斗 HUD 和不同机甲属性。

**作者**: [@aniketjart](https://x.com/aniketjart/status/2096019868713984080) · 2026-09-05<br>
**工具与技术**: Three.js, Crayon, 3D combat

**创作方法**

把已有机甲项目和一句紧凑的创作方向交给 Astra，再通过 Crayon harness 实际游玩并迭代生成的游戏。

**值得注意**

成果依赖作者正在开发的机甲项目与 Crayon harness，并非从空白仓库开始。

**提示词**

> use my ongoing mecha project and build a pacific rim style battle game

以上为开头摘录，完整提示词见下方作者原帖。

↗ [查看作者完整提示词](https://x.com/aniketjart/status/2096019868713984080) · [观看演示](https://x.com/aniketjart/status/2096019868713984080)

[返回案例目录](#cases)


<a id="beach-crab-adventure"></a>

### 海岛螃蟹水晶冒险

**提示词摘录** · [提示词原帖](https://x.com/zeuuss_01/status/2096337882931712076)

[![带可操控螃蟹和水晶 HUD 的低多边形海岛冒险](https://pbs.twimg.com/amplify_video_thumb/2096337699737350144/img/Jaq84uNs4vyVtR40.jpg)](https://x.com/zeuuss_01/status/2096337879173591171)

一款完成度很高的低多边形 Three.js 海岛游戏：玩家操控螃蟹收集金币、打开宝箱，并在完整 HUD 指引下寻找七块水晶。

**作者**: [@zeuuss_01](https://x.com/zeuuss_01/status/2096337879173591171) · 2026-09-06<br>
**工具与技术**: Three.js, Low poly, Browser game

**创作方法**

用结构化规格同时约束美术方向、角色几何、世界布局、动作设计、收集目标、界面、镜头、变化规则和明确的禁用元素。

**值得注意**

作者称生成耗时 43 分钟且没有手写代码；由于完整提示词分为九部分且篇幅较长，目录仅展示开头并保留原帖链接。

**提示词**

> SAVE IT AS A FILE IN THE PROJECT FOLDER, NOT AS A CHAT MESSAGE. THEN: /goal build this in three.js, read SPEC.md and follow it exactly, especially section 9.

以上为开头摘录，完整提示词见下方作者原帖。

↗ [查看作者完整提示词](https://x.com/zeuuss_01/status/2096337882931712076) · [观看演示](https://x.com/zeuuss_01/status/2096337879173591171)

[返回案例目录](#cases)


<a id="windhaven-unity-adventure"></a>

### Windhaven 海滨幻想冒险

**完整提示词** · [提示词原帖](https://x.com/tripoai/status/2096629507096481992)

[![阳光海滨城市 Windhaven 中的可操作探险者](https://pbs.twimg.com/amplify_video_thumb/2096626220935061504/img/AMhMafn4jRoV_58V.jpg)](https://x.com/tripoai/status/2096629506047955327)

这款 Unity 第三人称冒险构建了完整的阳光海岛城市，拥有可探索街道、宏伟地标、魔法信标、地图和可操作角色。

**作者**: [@tripoai](https://x.com/tripoai/status/2096629506047955327) · 2026-09-07<br>
**工具与技术**: Unity, Tripo P2, Third-person adventure

**创作方法**

在一条美术指导提示词中明确引擎、世界观、建筑、材质、光照、配色、镜头和排除项；由 Astra 实现游戏逻辑，Tripo P2 提供三维资产。

**值得注意**

这是 Tripo 官方展示，视觉完成度依赖 Tripo P2 生成的三维资产；游戏逻辑部分归功于 Astra。

**提示词**

```text
Design a game with me. The game should be built in Unity. Use default asset first and I will replace assets later. Game style: A premium stylized coastal fantasy adventure game set in a small sunlit island city called Windhaven. The city is built from warm ivory limestone and golden sandstone, surrounded by clear turquoise water, with teal copper roofs, shaded market stalls, arched gateways, lush courtyard trees, carved fountains, glowing magical beacons, and a monumental temple overlooking the town. A lone young explorer wearing a travel cloak and backpack walks through the central plaza toward the temple. The environment feels peaceful, mysterious, ancient, and gently magical, with Mediterranean and North African architectural influences. High-detail stylized PBR materials, handcrafted stone surfaces, subtle weathering, elegant decorative carvings, soft afternoon sunlight, long cinematic shadows, turquoise and warm gold color palette, polished AA adventure game art direction, third-person gameplay camera, wide establishing shot, cohesive environment design, visually readable paths and landmarks, no UI, no text, no logos, no modern objects.
```

↗ [查看作者完整提示词](https://x.com/tripoai/status/2096629507096481992) · [观看演示](https://x.com/tripoai/status/2096629506047955327)

[返回案例目录](#cases)


<a id="komorebi-river-run"></a>

### Komorebi：林隙河流

**完整提示词** · [提示词原帖](https://x.com/ItsmeAjayKV/status/2096244208533455049)

[![皮划艇穿过风格化森林河流顺流竞速](https://pbs.twimg.com/amplify_video_thumb/2096235513309229056/img/fbBMPWlWaIaIaVWp?format=webp&name=medium)](https://x.com/ItsmeAjayKV/status/2096244208533455049)

这款浏览器皮划艇游戏融合动漫风景、代码生成的音乐与音效、障碍躲避和鲜明的顺流速度感。

**作者**: [@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2096244208533455049) · 2026-09-05<br>
**工具与技术**: Three.js, Kayaking, Procedural audio

**创作方法**

用自然语言描述核心运动，指定美术风格，并把操作限制为左右划桨，让 Astra 集中打磨水体、速度感和氛围。

**值得注意**

作者肯定美术和音乐，但也指出水体的湍流感仍不够。

**提示词**

```text
build me a 3D river kayaking game with anime-ish aesthetics, where i paddle left or right to avoid obstacles.
```

↗ [查看作者完整提示词](https://x.com/ItsmeAjayKV/status/2096244208533455049) · [观看演示](https://x.com/ItsmeAjayKV/status/2096244208533455049)

#### 使用前提

依据本目录已收录资料整理；信息未说明，不代表不需要相关依赖或素材。

| 项目 | 已知信息与缺口 |
| --- | --- |
| 软件与环境 | 目录描述为浏览器游戏并标注 Three.js；完整短提示词本身没有指定库，现有资料未记录浏览器、运行环境与依赖版本。 |
| 输入素材 | 资料描述了代码生成的音乐与音效，但未提供完整素材清单与许可信息。 |
| 服务与账号 | 现有资料未说明外部账号、服务或启动时是否需要联网。 |
| 源码与演示入口 | 目录收录完整提示词与作者原帖，未记录直接可玩的地址或代码仓库。 |

#### 提示词拆解 · 项目分析

作者提示词原文见上方。以下拆解和验收建议是项目编辑内容，与作者原文明确区分。

**目标**：原文同时给出场景（河流皮划艇）、输入（左右划桨）和目标（躲避障碍），形成一个较清晰的核心循环。

**约束**：三维与动漫风格限定呈现方向，但没有规定水体模拟、难度、计分和设备支持。

**交付**：原文要求一个游戏，没有约定打包与启动方式。建议补充可运行源码、启动说明，以及依赖和联网需求清单。

**验收建议**：检查左右控制、障碍碰撞、明确的结束状态和重新开始；分别检查静音及有声游玩，并将水体行为与美术偏好分开记录。

**可借鉴之处**：写出玩家反复执行的动作，比只给游戏类型更具体。作者仍指出水体湍流不足，因此短提示词对应的成果不能视为所有子系统都已完善。

所依据的已收录来源：[@ItsmeAjayKV · 2096244208533455049](https://x.com/ItsmeAjayKV/status/2096244208533455049)

[返回案例目录](#cases)


<a id="voidrunner-combat-racer"></a>

### Voidrunner 反重力战斗竞速

**完整提示词** · [提示词原帖](https://x.com/superalesha/status/2095967568825582044)

[![霓虹反重力飞行器在异世界上空竞速](https://pbs.twimg.com/amplify_video_thumb/2095966450385289216/img/u4EnBwNxU0h3lQgI?format=webp&name=medium)](https://x.com/superalesha/status/2095967568825582044)

一个提示词完成的 Three.js 竞速游戏，包含漂移、加速、拾取物、三类飞行器和悬空异世界中的霓虹着色器视觉。

**作者**: [@superalesha](https://x.com/superalesha/status/2095967568825582044) · 2026-09-05<br>
**工具与技术**: Three.js, Web shaders, Blender

**创作方法**

先规定速度、漂移和冲击感，再列出机制、镜头行为、载具类型、技术栈，并允许 Astra 自主设计不寻常的世界。

**值得注意**

作者称单次提示运行约 25 分钟；Astra 还自行发现并使用本机 Blender 制作模型。

**提示词**

```text
Make me the most insane and blast of a high-speed anti-gravity combat racer you can possibly build on ThreeJS + Web shaders bro! The most important things are blistering sense of speed, tight drifting, boost mechanics, track elevation drops, motion blur, and jaw-dropping neon shader lighting. It's an intense futuristic raceway high above a strange world where aggressive AI racers battle for first place. Must have smooth camera banking into turns, shield/weapon pickups, and punchy air-brake physics. 3 craft types: a featherlight glass-cannon speeder, an agile balanced interceptor, and a heavy armored ramming tank. This is a Wipeout / Redout style AAA arcade racer in the browser. Do it right bro, I believe in you! An unusual setting for the game, pick it yourself. Please don't read the memory, don't read anything. Start from a blank slate.
```

↗ [查看作者完整提示词](https://x.com/superalesha/status/2095967568825582044) · [观看演示](https://x.com/superalesha/status/2095967568825582044)

[返回案例目录](#cases)


<a id="sonic-godot-vertical-slice"></a>

### Sonic 风格 Godot 垂直切片

**提示词摘录** · [提示词原帖](https://x.com/AiBattle_/status/2096056285896536086)

[![Sonic 风格角色高速穿越热带 Godot 关卡](https://pbs.twimg.com/amplify_video_thumb/2096055803866193925/img/RxWSGd_n3Wes7Qm0?format=webp&name=medium)](https://x.com/AiBattle_/status/2096056285896536086)

Astra 在 Godot 中构建明亮海岸高速平台游戏，涵盖鲜明角色动作、环道、滑轨、追踪攻击、捷径和电影化移动段落。

**作者**: [@AiBattle_](https://x.com/AiBattle_/status/2096056285896536086) · 2026-09-05<br>
**工具与技术**: Godot, 3D platformer, Procedural assets

**创作方法**

把长提示词聚焦于一个精修关卡，完整定义移动动作、标志性路线节点、动画状态、视觉效果，并严格禁止下载外部资产。

**值得注意**

作者复跑的 Max 任务耗时 46 分钟并消耗其周额度的 3%；需要预先安装 Godot，且提示词刻意模仿受版权保护的游戏角色。

**提示词**

> Create a visually spectacular, highly polished 3D Sonic the Hedgehog vertical slice in Godot. Do not use web search, external downloads, online assets, or internet resources. Build everything using only locally available tools, assets, and procedural/original content. Sonic must be immediately recognizable: cobalt-blue quills, connected eyes, tan muzzle/torso, white gloves, oversized red shoes with white straps, compact athletic proportions, swept-back quills, expressive animation, iconic running posture, and spin form.

以上为开头摘录，完整提示词见下方作者原帖。

↗ [查看作者完整提示词](https://x.com/AiBattle_/status/2096056285896536086) · [观看演示](https://x.com/AiBattle_/status/2096056285896536086)

[返回案例目录](#cases)


<a id="rocket-league-threejs"></a>

### 浏览器原生汽车足球竞技场

**提示词摘录** · [提示词原帖](https://x.com/LLMJunky/status/2096043707015274818)

[![在发光浏览器竞技场中进行的汽车足球比赛](https://pbs.twimg.com/amplify_video_thumb/2096028515099660288/img/SQ7xgsqG8hoVZ5P1?format=webp&name=medium)](https://x.com/LLMJunky/status/2096028790925488452)

一条长提示词生成精致的本地 Three.js 汽车足球游戏，包含物理系统、竞技场呈现、灵敏驾驶和完整比赛循环。

**作者**: [@LLMJunky](https://x.com/LLMJunky/status/2096028790925488452) · 2026-09-05<br>
**工具与技术**: Three.js, Rapier.js, Vehicle physics

**创作方法**

把提示词写成紧凑的游戏设计文档：规定开屏即游玩、渲染与物理库、车辆手感、球体规则、竞技场、镜头、HUD、音效和验收条件。

**值得注意**

作者称单次提示运行约 1 小时 3 分钟；作品致敬现有商业游戏，并非原创玩法概念。

**提示词**

> Build a polished browser-based 3D Rocket League-style game using Three.js. Goal: Create a fully playable local web game that runs in the browser. The first screen should be the actual game, not a landing page. Tech requirements: Use Three.js for rendering.

以上为开头摘录，完整提示词见下方作者原帖。

↗ [查看作者完整提示词](https://x.com/LLMJunky/status/2096043707015274818) · [观看演示](https://x.com/LLMJunky/status/2096028790925488452)

[返回案例目录](#cases)


<a id="ghost-of-tsushima-game"></a>

### 《对马岛之魂》风格可玩世界

**完整提示词** · [提示词原帖](https://x.com/karankendre/status/2096577524855963729)

[![武士角色穿行于写实风吹原野](https://pbs.twimg.com/amplify_video_thumb/2096576662456741889/img/96iHLjZmijpBhZnL?format=webp&name=medium)](https://x.com/karankendre/status/2096577524855963729)

Astra 把生成式环境资产与游戏代码组合起来，从一条简短而大胆的需求构建写实第三人称武士世界。

**作者**: [@karankendre](https://x.com/karankendre/status/2096577524855963729) · 2026-09-06<br>
**工具与技术**: Higgsfield CLI, Third-person adventure, Generated assets

**创作方法**

要求交付完整可玩游戏，把 Higgsfield CLI 限定为资产生成工具，并将视觉写实度设为首要质量标准。

**值得注意**

作者称制作耗时两小时。作品是对受版权保护游戏的非官方模仿，原帖也未提供可供独立检查的试玩下载。

**提示词**

```text
Build a complete ghost of tsushima exact playable game remember to build assets using higgsfield cli (only the assets) makes no mistake make the game as realistic as possible
```

↗ [查看作者完整提示词](https://x.com/karankendre/status/2096577524855963729) · [观看演示](https://x.com/karankendre/status/2096577524855963729)

[返回案例目录](#cases)


<a id="little-acre-world-builder"></a>

### Little Acre 袖珍世界建造器

**完整提示词** · [提示词原帖](https://x.com/ManasJoshi76254/status/2096061253307490583)

[![带房屋、花园和拖拉机的可互动袖珍星球](https://pbs.twimg.com/amplify_video_thumb/2096061022583103488/img/CGEve4Jcy-_V0UXv?format=webp&name=medium)](https://x.com/ManasJoshi76254/status/2096061253307490583)

一个 HTML 文件变成可互动的小行星：玩家能驾驶、放置房屋与花园、种树、切换昼夜并导出自己的世界。

**作者**: [@ManasJoshi76254](https://x.com/ManasJoshi76254/status/2096061253307490583) · 2026-09-05<br>
**工具与技术**: Three.js, Single-file HTML, World building

**创作方法**

给 Astra 一个“可交互三维世界”的宽目标，让它在单文件网页中自行设计建造循环、载具、世界状态、昼夜和导出功能。

**值得注意**

作者称消耗了一个五小时额度的 55%；有回复反馈卡顿，因此低配置设备上的性能可能不同。

**提示词**

```text
build a small interactive 3D world from scratch.
```

↗ [查看作者完整提示词](https://x.com/ManasJoshi76254/status/2096061253307490583) · [观看演示](https://x.com/ManasJoshi76254/status/2096061253307490583)

[返回案例目录](#cases)


<a id="single-file-canyon-racer"></a>

### 单文件峡谷驾驶游戏

**完整提示词** · [提示词原帖](https://x.com/IamRicardoML/status/2096069303523033434)

[![汽车在电影感峡谷赛道中进行 3D 竞速](https://pbs.twimg.com/amplify_video_thumb/2096065216064761857/img/X_QJRt5ErXYDsjqN?format=webp&name=medium)](https://x.com/IamRicardoML/status/2096069303523033434)

Astra 把可驾驶汽车、峡谷赛道、物理、电影感光照、HUD、小地图、音效和圈速计时装进一个 HTML 文件。

**作者**: [@IamRicardoML](https://x.com/IamRicardoML/status/2096069303523033434) · 2026-09-05<br>
**工具与技术**: Single-file HTML, 3D driving, Game physics

**创作方法**

先设定“单个 HTML 文件”的严格交付约束和明确类型，再让 Astra 一体完成车辆、赛道、模拟、视听反馈和比赛界面。

**值得注意**

第一版出现一个打包问题，需要一次快速修复；公开帖子没有提供试玩链接。

**提示词**

```text
build a playable 3D driving game in a single HTML file.
```

↗ [查看作者完整提示词](https://x.com/IamRicardoML/status/2096069303523033434) · [观看演示](https://x.com/IamRicardoML/status/2096069303523033434)

#### 使用前提

依据本目录已收录资料整理；信息未说明，不代表不需要相关依赖或素材。

| 项目 | 已知信息与缺口 |
| --- | --- |
| 软件与环境 | 原文要求单个 HTML 文件，未指定渲染库、浏览器版本或是否需要本地服务器。 |
| 输入素材 | 现有资料没有素材清单；单个 HTML 文件并不能证明所有资源都已内嵌。 |
| 服务与账号 | 现有资料未说明外部依赖和联网要求；离线运行需要单独约定并验证。 |
| 源码与演示入口 | 目录提供完整提示词与成果原帖。已有局限记录明确指出公开帖子没有试玩链接，目录也未记录可下载的 HTML。 |

#### 提示词拆解 · 项目分析

作者提示词原文见上方。以下拆解和验收建议是项目编辑内容，与作者原文明确区分。

**目标**：可玩、三维、驾驶明确交互性质和类型。成果中的峡谷、小地图与圈速计时并不是这条短提示词明确要求的功能。

**约束**：single HTML file 约束的是文件交付形式，没有约定是否从网络加载库或素材。

**交付**：原文明确交付一个 HTML 文件。建议另外要求打开方式和全部依赖，并明确选择允许联网或完全离线。

**验收建议**：用新副本按说明启动，测试驾驶与重开，检查缺失资源；如果宣称离线可用，再验证断网启动。

**可借鉴之处**：打包属于任务本身。作者记录过打包问题和后续修复，展示案例时应保留这次迭代，而不是暗示首轮即完整交付。

所依据的已收录来源：[@IamRicardoML · 2096069303523033434](https://x.com/IamRicardoML/status/2096069303523033434)

[返回案例目录](#cases)


<a id="dream-loop-isometric-demo"></a>

### Dream Loop 等距幻想世界演示

**完整提示词** · [提示词原帖](https://x.com/anshuc/status/2097001450941587889)

[![带可操控角色和湿润反射地面的等距幻想场景](https://pbs.twimg.com/amplify_video_thumb/2097001376606011392/img/f-lqFhoMgDtRlb_L.jpg)](https://x.com/anshuc/status/2097001438736166960)

可复用的 Dream Loop 技能把一份需求变成精致的浏览器等距幻想世界，包含可操控角色、湿润反射地面和环境动态。

**作者**: [@anshuc](https://x.com/anshuc/status/2097001438736166960) · 2026-09-08<br>
**工具与技术**: Three.js, Dream Loop, Isometric 3D

**创作方法**

以 High effort 运行作者公开的 /dream-loop 提示词；任务限定一小时、不下载外部素材，作者称消耗了 20x 套餐周额度的 2%。

**值得注意**

作者明确把它定位为视觉演示而非完整游戏；可移动区域受限，提示词也没有要求玩法循环。

**提示词**

```text
/dream-loop Build me a graphics demo: isometric camera, voxel-ish art style with realistic shading and reflective wet floors, a character in an interesting scene. Fantasy setting (think Elden Ring, Diablo). Three.js in browser, >60fps. Don't download assets. Time limit of 1 hour. Controls: click to move the character, camera lazy-follows; drag to rotate camera; scroll to zoom in/out. No gameplay for now. World should feel alive: motion, animations, subtle environmental behaviors. Area around player should look expansive, but only allow movement in a limited space. No need to confirm the art with me or ask questions, just go!
```

↗ [查看作者完整提示词](https://x.com/anshuc/status/2097001450941587889) · [观看演示](https://x.com/anshuc/status/2097001438736166960)

[返回案例目录](#cases)


<a id="workbench-robo-cat"></a>

### 把电量显示做进机身的工作台机器猫

**提示词摘录** · [提示词原帖](https://x.com/zeuuss_01/status/2097004362530787837)

[![四足机器猫站在暖光工作台的充电座旁](https://pbs.twimg.com/amplify_video_thumb/2097002747883376640/img/-6RFXjIep4U4fHAL.jpg)](https://x.com/zeuuss_01/status/2097004192627933279)

一只四足小机器人在暖光工作台上行走、搬运螺栓并主动回到充电座，机身侧面的五格琥珀色灯就是完整电量界面。

**作者**: [@zeuuss_01](https://x.com/zeuuss_01/status/2097004192627933279) · 2026-09-08<br>
**工具与技术**: Three.js, Diegetic UI, Inverse kinematics

**创作方法**

把作者公开的十节规格保存为 SPEC.md，再让 Astra 用 Three.js 实现。规格明确要求先做好轮廓与步态，再完成电量状态、三种物件驱动任务和工作台陈设，并在交付前用指定画面证明关键状态。

**值得注意**

该规格刻意控制范围，不使用物理引擎、声音、存档、菜单、额外房间或第二只机器人；作者公开的是短视频，没有同时提供源码或在线试玩。

**提示词**

> THE FULL SPEC.
SAVE IT AS A FILE IN THE PROJECT FOLDER, NOT AS A CHAT MESSAGE.
THEN: /goal build this in three.js, read SPEC.md and follow it exactly, especially sections 9 and 10.

{ START }

1 WHAT THIS IS

a small four-legged robot lives on a workbench. you charge it, play with it, and give it three jobs. it never leaves the bench and neither do you. that is the whole game.

以上为开头摘录，完整提示词见下方作者原帖。

↗ [查看作者完整提示词](https://x.com/zeuuss_01/status/2097004362530787837) · [观看演示](https://x.com/zeuuss_01/status/2097004192627933279)

[返回案例目录](#cases)


<a id="isometric-knight-sprites"></a>

### 包含 16 个姿势的等距骑士图集

**完整提示词** · [提示词原帖](https://x.com/yulmu_coffee/status/2097502912847245522)

[![对比卡片展示 Astra 的等距骑士像素素材与另一模型的结果](https://pbs.twimg.com/media/HRvTP4AaoAAHqjK?format=jpg&name=large)](https://x.com/yulmu_coffee/status/2097502912847245522)

Astra 用一句话为全新的 2D 等距游戏生成了一套风格统一、包含 16 个关键姿势的中世纪骑士图集。

**作者**: [@yulmu_coffee](https://x.com/yulmu_coffee/status/2097502912847245522) · 2026-09-09<br>
**工具与技术**: Pixel art, Sprite sheet, Codex CLI

**创作方法**

从空项目开始，明确素材类型与游戏视角，并禁止复用目录里的其他内容；作者使用 Codex CLI 的 XHigh，报告约 4 分钟完成。

**值得注意**

Astra 的结果是一张包含 16 个关键姿势的图集，并非对比模型展示的多配色大规模动画帧集合。

**提示词**

```text
Build me some knight sprites which I can use in my new medieval 2D isometric game. The game doesn't exist yet I am starting with sprites - this is the first thing we are building. Do not look at any other work in this directory. Start from scratch.
```

↗ [查看作者完整提示词](https://x.com/yulmu_coffee/status/2097502912847245522) · [观看演示](https://x.com/yulmu_coffee/status/2097502912847245522)

[返回案例目录](#cases)

## 其他分类

- [🧩 应用与网站](apps.zh-CN.md)
- [✨ 设计与创意](design.zh-CN.md)
- [🏛️ 三维与空间创作](3d.zh-CN.md)
- [🎬 视频与叙事](video.zh-CN.md)
- [🖱️ 电脑操作与自动化](automation.zh-CN.md)
- [🛠️ 工程与原型](engineering.zh-CN.md)
