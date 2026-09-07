# GPT-6 Astra interactive websites and Three.js examples: writing a clear brief

[简体中文](web-3d.zh-CN.md) · [Home](../../README.md) · [Full gallery](../gallery.md)

This guide is editorial analysis of the collected cases. The recommendations and sample brief below are original, untested project writing, not the creators' prompts or a guarantee of results.

## Choose the deliverable first

| Goal | Reference case | Brief structure to study | Evidence limit |
| --- | --- | --- | --- |
| A webpage with a 3D centerpiece | [Interactive peacock](../gallery.md#interactive-peacock) | Specify palette, mouse and keyboard input, feather motion and touch behavior separately | Only an opening prompt excerpt is stored; consult the full source |
| An explorable 3D scene | [Living playroom](../gallery.md#playroom-threejs) | Separate room, toys and character actions; define orbit and zoom | Prompt excerpt only; the record names Three.js and Vite |
| An explanatory interactive model | [V8 engine visualization](../gallery.md#v8-engine-visualizer) | Decide what readers should understand before choosing cutaways, controls and labels | The complete short prompt is stored, but no rendering stack or engineering-accuracy target is specified |

## Turn appearance into observable behavior

The peacock brief connects visual direction with interaction; the playroom brief separates scene objects from their actions. Our recommendation is to write an object–input–feedback table before polishing the art direction. For example, dragging rotates the model, releasing stops it, and reset restores the initial view. This is easier to check than a request for an immersive experience alone.

The V8 case illustrates another distinction: a detailed visualization is not evidence of correct mechanical relationships. For educational use, list the facts and reference materials that need checking, and mark unverified mechanisms as illustrative. Do not infer engineering accuracy from a demo image.

## Original brief template: an interactive exhibit

Adapt the placeholders. This is not quoted from a collected creator.

```text
Goal: build an interactive webpage about [original exhibit/topic] for [audience].
Deliver source code, startup instructions, a dependency list and known limitations.
Start with one main object and a simple background using [provided assets/procedural shapes].
Support drag to rotate, wheel to zoom and a reset-view button, with touch equivalents.
Selecting a part should reveal its name and a short explanation in [language].
On narrow screens, place the explanation below the scene; controls must not cover the object.
List external dependencies and asset sources. Label unverified explanations as illustrative.
Run the startup instructions, then check rotation, zoom, selection and reset separately.
Record failures and fixes. Do not report checks as passed unless they were executed.
```

## First-run check order

1. Start from a fresh directory using the supplied instructions. Resolve missing entry points, assets, dependencies and runtime errors first.
2. Check each input against its expected response, including returning to a usable state after reset.
3. Narrow the window, then test a real touch device. Record touch as untested if no device was used.
4. Refine color, lighting and detail afterwards. Record the device and observed behavior rather than inferring performance from a video.

For a failed check, give concrete feedback: `Steps: […]. Expected: […]. Actual: […]. Logs: […]. Fix this issue first, explain the change and rerun the check.` Remove credentials and personal data before sharing logs.

## Next steps and sources

- For goals and failure rules, read the [game prompt guide](game-prompts.md).
- To document an actual run, use the [reproduction record requirements](../reproduction/README.md).
- Case facts refer to the catalog's linked [peacock post](https://x.com/lepadphone/status/2096147245775331419), [playroom post](https://x.com/zhengli/status/2096048421543272893) and [V8 post](https://x.com/DilumSanjaya/status/2096280244663775423). This guide does not independently verify their performance or capability claims.
