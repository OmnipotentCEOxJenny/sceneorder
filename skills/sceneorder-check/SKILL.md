---
name: sceneorder-check
description: Check a cut list's timecodes, durations and total runtime, and the edit's story and pacing. Use when a user asks to check timecodes, a cut list or a video's running time.
---

Follow `rules/scope.mdc`. Answer in the user's language.

1. Check each timecode: format HH:MM:SS:FF, minutes and seconds 00-59, frames below the frame rate (00-23 at 24 fps).
2. Check each out point is after its in point.
3. Check the total runtime against the target and say how much to cut or add.
4. Check the story: does the first cut say what this is, does each cutaway cover something, is there a clear ending?
5. If Python is available, run `python3 scripts/sceneorder.py FILE.csv --fps N --target TC`. It handles non-drop-frame timecode only.
6. Report problems with the exact fix.
