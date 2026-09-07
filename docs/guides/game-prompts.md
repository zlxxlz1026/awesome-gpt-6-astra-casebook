# GPT-6 Astra game prompts: from the core loop to a testable deliverable

[简体中文](game-prompts.zh-CN.md) · [Home](../../README.md) · [Game examples](../gallery.md#games)

This guide analyzes the creators' material already recorded in the catalog. Its analysis, templates and acceptance suggestions are original project writing and have not been tested. Creator demos are not independent reproductions by this project.

## Three cases, three prompt priorities

| Case | Recorded emphasis | Transferable lesson | Evidence limit |
| --- | --- | --- | --- |
| [Komorebi: River Run](../gallery.md#komorebi-river-run) | A short prompt names kayaking, left/right paddling, obstacle avoidance and an art direction | Specify the repeated player action before the visual style | The author's praise for art and music does not establish complete water simulation; the author also notes insufficient turbulence |
| [Single-file canyon racer](../gallery.md#single-file-canyon-racer) | 3D driving and one HTML file | Make delivery format an observable requirement | A single file does not imply offline operation; the author reports a packaging fix and the record has no playable link |
| [Little Acre](../gallery.md#little-acre-world-builder) | A broad goal leaves building, driving, day/night and export to the model | Open goals can solicit design options | The same prompt does not guarantee the same features; the record includes allowance usage and a lag report |

## A suggested first version

Starting from Komorebi's left/right input structure, limit a first version to one route, two inputs, one collision rule and a restart button. Check that loop before adding audio, decoration or more levels. For an open goal like Little Acre, choose one complete behavior from the proposed features, such as placing an object, saving and restoring it after reopening. A list of creative possibilities is not yet an acceptance specification.

For more complex physics, study the [car-football case](../gallery.md#rocket-league-threejs), whose recorded brief covers the vehicle, ball, arena, camera and match loop. An initial attempt could focus on one vehicle and one ball. This is our editorial suggestion, not the creator's original plan or a proven shortcut.

## Original prompt template: a single-file obstacle game

This is an untested template, not a collected creator's prompt. Choose a network policy before using it.

```text
Create an original browser obstacle-avoidance game. The first screen should be playable.
Core loop: move left/right to avoid obstacles, show a result on collision, allow restart.
Build one route first. Display controls, current score and pause state clearly.
Deliver one HTML file and explain how to open it.
Network policy: [allow CDNs and list dependencies / require offline operation with all necessary content included].
Use original procedural assets, not characters from existing commercial games.
Keep speed, obstacle density and collision bounds in clearly adjustable parameters.
Check start, left/right input, collision, pause, resume and restart.
Report checks actually performed, failures and limitations. Do not invent test results.
```

## Acceptance checks: leave outcomes blank until executed

| Check | Passing condition | Evidence to record |
| --- | --- | --- |
| Open the deliverable | The documented startup reaches a playable scene | Startup method, browser version and logs |
| Input | Left/right input produces the intended motion without stuck keys | Which keyboard or touch controls were actually tested |
| Collision and result | Collision follows the rule and scoring matches the result | A normal run and a boundary case |
| Pause and resume | Game state stops advancing while paused and continues afterwards | State screenshots or recording |
| Restart | Previous-round state clears and another complete round works | Actions from at least two rounds |
| Packaging | Startup works in a clean directory; offline claims survive disconnected startup | External requests, missing resources and actual network state |

A recording establishes only the visible sequence. It does not replace input, restart or offline checks. Even a complete prompt does not supply missing code, assets or environment details.

## Keep the iteration history

Record the initial prompt, follow-ups, actual elapsed time, model label and settings, environment and failures. Record costs only when backed by billing or usage evidence; a creator's allowance percentage is not your fixed cost. Use the [reproduction record requirements](../reproduction/README.md) to distinguish playing an existing artifact from generating and reproducing it.

Sources: [Komorebi](https://x.com/ItsmeAjayKV/status/2096244208533455049), [canyon racer](https://x.com/IamRicardoML/status/2096069303523033434), [Little Acre](https://x.com/ManasJoshi76254/status/2096061253307490583). Facts above come from existing catalog records; the original posts were not reverified in this pass.

Continue with the [interactive web and Three.js brief guide](web-3d.md).
