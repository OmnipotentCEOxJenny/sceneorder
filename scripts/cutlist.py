#!/usr/bin/env python3
"""CutList timecode and cut-list checker (standard library only).
Usage: python3 scripts/cutlist.py CUTS.csv [--fps 24] [--target 00:01:00:00]
CUTS.csv columns: clip,in,out,note   (timecodes HH:MM:SS:FF; frames count from 0 to fps-1)
Prints a numbered cut list with each cut's duration and where it lands on the timeline,
the total runtime, and problems: bad timecodes, frames >= fps, out not after in,
and the difference from a target runtime. Non-drop-frame timecode only.
Exit 0 = no problems, 1 = problems found, 2 = usage error."""
import csv, re, sys

def tc_to_frames(tc, fps):
    m = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2}):(\d{2})", tc.strip())
    if not m: raise ValueError(f"bad timecode {tc!r} (use HH:MM:SS:FF)")
    h, mi, s, f = map(int, m.groups())
    if mi > 59 or s > 59: raise ValueError(f"minutes and seconds must be 00-59 in {tc!r}")
    if f >= fps: raise ValueError(f"frame {f} is not valid at {fps} fps in {tc!r} (frames go 00-{fps-1:02d})")
    return ((h * 60 + mi) * 60 + s) * fps + f

def frames_to_tc(n, fps):
    f = n % fps; s = n // fps
    return f"{s // 3600:02d}:{s // 60 % 60:02d}:{s % 60:02d}:{f:02d}"

def build(rows, fps):
    cuts, problems, at = [], [], 0
    for i, r in enumerate(rows, 1):
        try:
            a, b = tc_to_frames(r["in"], fps), tc_to_frames(r["out"], fps)
        except ValueError as e:
            problems.append(f"cut {i} ({r['clip']}): {e}"); continue
        if b <= a:
            problems.append(f"cut {i} ({r['clip']}): out {r['out']} is not after in {r['in']}"); continue
        cuts.append(dict(n=i, clip=r["clip"], src_in=r["in"], src_out=r["out"], dur=b - a, rec_in=at, rec_out=at + b - a, note=r.get("note", "")))
        at += b - a
    return cuts, at, problems

def main(argv):
    if len(argv) < 2: print(__doc__); return 2
    fps = int(argv[argv.index("--fps") + 1]) if "--fps" in argv else 24
    rows = list(csv.DictReader(open(argv[1], encoding="utf-8")))
    cuts, total, problems = build(rows, fps)
    print(f"Cut list ({fps} fps, non-drop-frame)")
    print("| # | Clip | Source in | Source out | Duration | Timeline in | Timeline out | Note |")
    print("|---|---|---|---|---|---|---|---|")
    for c in cuts:
        print(f"| {c['n']} | {c['clip']} | {c['src_in']} | {c['src_out']} | {frames_to_tc(c['dur'], fps)} | {frames_to_tc(c['rec_in'], fps)} | {frames_to_tc(c['rec_out'], fps)} | {c['note']} |")
    print(f"Total runtime: {frames_to_tc(total, fps)} ({total} frames)")
    if "--target" in argv:
        tgt = tc_to_frames(argv[argv.index("--target") + 1], fps); diff = total - tgt
        print(f"Target {frames_to_tc(tgt, fps)}: " + ("on target" if diff == 0 else f"{'over' if diff > 0 else 'under'} by {frames_to_tc(abs(diff), fps)}"))
        if diff: problems.append(f"runtime differs from target by {abs(diff)} frames")
    for p in problems: print("PROBLEM:", p)
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
