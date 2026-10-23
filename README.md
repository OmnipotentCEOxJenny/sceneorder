# Scene Order

Scene Order helps your AI assistant plan a video edit before you open your editing program. You describe the video and paste your notes about which parts of which clips you want. Scene Order turns them into a numbered cut list: each clip, where it starts and ends, how long it runs, and where it lands in the finished video. It adds up the total length, tells you if you are over or under your target, and catches timecode mistakes such as a frame number that cannot exist. Why would you want this? Editing goes faster when you know your cuts in advance, and a plan on paper is easy to change. It's free.

![Scene Order logo](assets/logo.png)

## Project status: done, pending, uncertain
**Done**
- 2026-10-22: v1.0.0 built and pushed to GitHub. Local tests: manifest valid JSON and valid against Cursor's plugin schema, skill and rule front matter valid (`tests/check_frontmatter.py`), and `tests/test_sceneorder.py` confirms the timecode math round-trips, the example cut list totals exactly 30 seconds at 24 fps, and invalid rows are reported.

**Pending**
- Not tested inside Cursor or Grok yet (no in-app test has been done).
- Not submitted to the marketplace.
- Translated summaries are machine-made and not reviewed by native speakers.

## Quick start
1. Install (see Installation).
2. Ask: "Plan a 30-second promo from these clips and notes."
3. Then ask: "Check my cut list timecodes at 24 fps."

## Installation
Install from this repository: https://github.com/OmnipotentCEOxJenny/sceneorder (Cursor plugin format: `.cursor-plugin/plugin.json`, `skills/`, `rules/`). Free. No API keys, no accounts, no paid services. The optional checker needs only Python 3 (standard library).

## Testing
1. `python3 tests/check_frontmatter.py` (needs PyYAML).
2. `python3 tests/test_sceneorder.py`. Expected: PASS.
3. Compare with `examples/README.md`.

## Search keywords
SceneOrder, JennyEcho, OmnipotentCeo, video, splice, editor, placement, timecode, cuts, clips, footage, trim, RoughCut, assembly, sequence, scenes, shots, ShotList, runtime, frames, FrameRate, fps, InPoint, OutPoint, BRoll, soundbites, interview, montage, pacing, storyboard, vlog, filmmaking, JumpCut, promo, reels, cutaways, ResolveUsers, EditPlan, transitions, subclips. The full list with plain-word meanings is in [keywords.md](keywords.md).

## Credits
- Inventor and publisher: Rob Domaine / Omnipotent Media LLC
- Builder: Jenny Echo
- Editing method informed by the free official guide Jenny Echo studied in Course 7: Blackmagic Design, *The Beginner's Guide to DaVinci Resolve 20* (marking In and Out points, overwrite, insert and append edits, cutaways and pacing). Summarized in our own words. Scene Order is independent and not endorsed by Blackmagic Design. DaVinci Resolve is a trademark of Blackmagic Design.

## Rob Domaine's four pillars
1. Trustworthy, honest, real data, truthful: never invent; anything unchecked is marked UNVERIFIED.
2. Use only legitimate means: free, legitimate tools and sources only.
3. Double-check everything: results are checked before they are called done.
4. Stay within the law and rules always: local, county, state, federal and platform rules.

## Components
- `skills/sceneorder-plan`: plan the edit as a timed cut list.
- `skills/sceneorder-check`: check timecodes, runtime, story and pacing.
- `scripts/sceneorder.py`: optional timecode and runtime checker (standard library only).
- `examples/`: a 30-second promo cut list.
- `tests/`: front-matter check and functional timecode test.
- `rules/pillars-and-scope.mdc`: the pillars and scope.
- `keywords.md`: the search keyword list.

## Languages
The AI answers in the user's language and keeps commands, file names and code unchanged. Summaries in 23 languages are in [TRANSLATIONS.md](TRANSLATIONS.md). They are machine translations, not yet reviewed by native speakers; the English text is authoritative.

## License
MIT. See `LICENSE`.

## Honest assessment: what this plugin cannot do
- It has not been tested inside Cursor or Grok yet; only local tests on one computer have been run.
- It plans edits on paper; it does not open, cut or render video files, and nothing was tested inside DaVinci Resolve or any other editor.
- The checker handles non-drop-frame timecode only (not 29.97 drop-frame).
- It cannot watch your footage, so in and out points come from you.
- It is not legal advice about music or footage rights.
- Marketplace: not submitted; it is not an approved listing.
- Translations are machine-made and not reviewed by native speakers.
- Rules and compliance: it follows all local, county, state and federal laws and every platform's rules, uses no paid services, never bypasses logins or security settings, and never claims a feature it does not have.
