# Awesome GPT-6 Astra

[English](README.md) | [简体中文](README.zh-CN.md)

A curated collection of concrete GPT-6 Astra use cases from X, with methods, tools and limitations to help you turn inspiration into practice.

**5 cases · 10 tracked sources · X sources only**

Source review and reproduction are tracked separately; see each case’s status and limitations. Undisclosed prompts are not invented.

## Categories

| Category | Cases |
| --- | ---: |
| Apps & websites | 0 |
| [Design & creative work](#design) | 1 |
| [3D & spatial creation](#3d) | 2 |
| [Computer use & automation](#automation) | 1 |
| [Data & visual analysis](#data) | 1 |
| Research & learning | 0 |
| Software engineering | 0 |
| Games & simulations | 0 |

Empty categories are collection priorities.

<a id="design"></a>

## Design & creative work

### Figma design from brand identity to pages

The author describes using Astra with Figma for brand identity and page design, accompanied by a video.

- Source: [@issui_ikeda](https://x.com/issui_ikeda/status/2096467418575147367) · 2026-09-06
- Method: Use Figma as the working design environment; exact connection method and prompting are not disclosed in the post.
- Tools: Figma
- Limitations: Read through X’s English translation of the Japanese original; the BI interpretation and implementation details need further confirmation.
- Model evidence: author-stated · Reproduction: not-tested
- Prompt: Not disclosed

<a id="3d"></a>

## 3D & spatial creation

### Interactive Sydney from maps and photos

The author reports building an interactive Sydney scene with zoom, orbit and lighting controls from maps and real photos.

- Source: [@rionaifantasy](https://x.com/rionaifantasy/status/2096460180401889613) · 2026-09-06
- Method: Combine geographic references and photos with Blender and Three.js; the author reports one conversation.
- Tools: Blender, Three.js
- Limitations: Scope and geographic accuracy were not independently checked; full prompt, source files and cost are not provided in this post.
- Model evidence: author-stated · Reproduction: not-tested
- Prompt: Not disclosed

### Buildable brick models and Blender renders

The author reports designing real brick models in Bricklink Studio and rendering a 4K video in Blender; the post links to parts lists.

- Source: [@dkundel](https://x.com/dkundel/status/2096297005924729240) · 2026-09-06
- Method: Design with discrete brick parts first, then render the models in Blender.
- Tools: Bricklink Studio, Blender
- Limitations: Linked parts lists and physical buildability have not been independently checked; the exact prompt is not supplied.
- Model evidence: author-stated · Reproduction: not-tested
- Prompt: Not disclosed

<a id="automation"></a>

## Computer use & automation

### Drawing through mouse operations

The author demonstrates a drawing and states that Astra produced it through computer-use mouse operations.

- Source: [@keitowebai](https://x.com/keitowebai/status/2096124169406775325) · 2026-09-05
- Method: Ask the agent to draw through the application UI; the post does not name the drawing application.
- Tools: Not disclosed
- Limitations: Read through X’s English translation of the Japanese original; exact prompt, input assets and application are not disclosed.
- Model evidence: author-stated · Reproduction: not-tested
- Prompt: Not disclosed

<a id="data"></a>

## Data & visual analysis

### Basketball team recognition in visual labeling

The author reports distinguishing Celtics and Knicks players in home and away settings, with a video and a linked detection discussion.

- Source: [@skalskip92](https://x.com/skalskip92/status/2096669615363383449) · 2026-09-07
- Method: Use visual context to identify team membership; the quoted discussion also discusses bounding boxes.
- Tools: Not disclosed
- Limitations: This is an author demonstration, not a benchmark; no dataset, measured accuracy or complete prompt is provided in this post.
- Model evidence: author-stated · Reproduction: not-tested
- Prompt: Not disclosed

## Contributing & maintenance

[贡献指南 / Contributing](CONTRIBUTING.md) · [去重台账 / Source ledger](docs/source-ledger.md) · [维护流程 / Maintenance](docs/MAINTENANCE.md)

The source of truth is [cases.json](data/cases.json) and [sources.json](data/sources.json). The bilingual catalog and ledger are generated; a future website can consume the same data.

## Credits & license

Inspired by the categories, multilingual navigation and structured curation in [awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2). Independently authored; its case database is not copied. Not affiliated with OpenAI.

Original project code and writing are [MIT licensed](LICENSE). Linked posts, prompts and media remain under their authors’ rights and are not relicensed by inclusion.
