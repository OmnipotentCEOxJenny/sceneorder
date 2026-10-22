# Worked example: a 30-second promo cut list

`promo-cuts.csv` plans a 30-second promo in the style of the interview-and-cutaway rough cut taught in Lessons 1-3 of the free DaVinci Resolve Beginner's Guide (clip names are illustrative). Run:

```
$ python3 scripts/cutlist.py examples/promo-cuts.csv --fps 24 --target 00:00:30:00
Cut list (24 fps, non-drop-frame)
| # | Clip | Source in | Source out | Duration | Timeline in | Timeline out | Note |
|---|---|---|---|---|---|---|---|
| 1 | INTERVIEW 1 | 00:00:01:00 | 00:00:09:00 | 00:00:08:00 | 00:00:00:00 | 00:00:08:00 | opening soundbite: who we are |
| 2 | STORE 2 | 00:00:02:12 | 00:00:06:12 | 00:00:04:00 | 00:00:08:00 | 00:00:12:00 | cutaway over the soundbite end |
| 3 | INTERVIEW 1 | 00:00:14:00 | 00:00:22:00 | 00:00:08:00 | 00:00:12:00 | 00:00:20:00 | second soundbite |
| 4 | MOUNTAIN WIDE | 00:00:00:00 | 00:00:06:00 | 00:00:06:00 | 00:00:20:00 | 00:00:26:00 | closing shot under music |
| 5 | LOGO | 00:00:00:00 | 00:00:04:00 | 00:00:04:00 | 00:00:26:00 | 00:00:30:00 | end card |
Total runtime: 00:00:30:00 (720 frames)
Target 00:00:30:00: on target
```

This is a plan on paper. It was not performed in DaVinci Resolve: Resolve does not run on the Linux computer this was built on.
