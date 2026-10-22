---
name: cutlist-plan
description: Plan a video edit as a timed cut list from the user's notes, with soundbites, cutaways and a target runtime. Use when a user wants to plan an edit, make a rough cut, a shot list, a cut list or fit a video to a length.
---

Follow `rules/pillars-and-scope.mdc`. Answer in the user's language.

1. **Goal and length:** what the video is for, who watches it, and the target runtime (for example 30 seconds).
2. **Story first:** pick the soundbites or main shots that tell the story, in order. Then add cutaways (B-roll) to cover jumps and keep the pace.
3. **Cut list:** for each cut write the clip name, source in and out timecodes (HH:MM:SS:FF), and a short note. Save it as CSV with the columns `clip,in,out,note`.
4. **Check it:** run `python3 scripts/cutlist.py cuts.csv --fps 24 --target 00:00:30:00` (use the project's real frame rate). Fix any problem it reports.
5. **Pacing:** shorten or drop cuts until the runtime matches the target; vary shot length; end on a clear closing shot or end card.
6. **Hand-off:** give the user the cut list table to follow in their editor (for example DaVinci Resolve: mark In and Out in the Source viewer, then overwrite, insert or append to the timeline).
