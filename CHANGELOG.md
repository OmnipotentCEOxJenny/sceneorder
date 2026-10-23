# Changelog

## 1.0.2 (2026-10-23)
- README keyword line: first keyword now reads SceneOrder, matching the manifest (it read "Scene Order"). No behavior changes.
- Local tests re-run and passed. Not tested in-app. Not submitted to the marketplace.

## 1.0.1 (2026-10-22)
- Renamed from CutList to Scene Order (display name Scene Order, manifest and repo `sceneorder`, skills `sceneorder-plan` and `sceneorder-check`, script `scripts/sceneorder.py`, test `tests/test_sceneorder.py`). The old name is the name of the paid woodworking software CutList Plus (trademark risk). Version 1.0.0 was released under the former name CutList. "Cut list" stays as the plain video-editing term for a timed list of cuts.
- Keywords: 40, with SceneOrder, JennyEcho and OmnipotentCeo. Logo artwork unchanged.
- No behavior changes.

## 1.0.0 (2026-10-22)
- First version: skills `sceneorder-plan` and `sceneorder-check`, rule `pillars-and-scope.mdc`, optional checker `scripts/sceneorder.py`, 30-second promo example, plain-language README.
- Informed by Course 7 (The Beginner's Guide to DaVinci Resolve 20).
- Tests: `tests/check_frontmatter.py` and `tests/test_sceneorder.py`.
- 40 search keywords (single words lowercase, joined words PascalCase, no hyphens, Scene Order-specific, per Rob's keyword rules) in the manifest plus `keywords.md`; 23 machine-translated summaries (not native-reviewed).
- Local tests only; not tested in-app. Not submitted to the marketplace.
