#!/usr/bin/env python3
"""Functional test: timecode math round-trips, the example cut list totals 00:00:30:00 at 24 fps,
and bad rows (frame 24 at 24 fps, out before in) are reported."""
import pathlib, sys, csv, io
root = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root / "scripts"))
import cutlist as c
ok = c.tc_to_frames("00:00:01:00", 24) == 24 and c.frames_to_tc(c.tc_to_frames("01:02:03:04", 30), 30) == "01:02:03:04"
rows = list(csv.DictReader(open(root / "examples/promo-cuts.csv", encoding="utf-8")))
cuts, total, probs = c.build(rows, 24)
print("example total:", c.frames_to_tc(total, 24), "problems:", probs)
ok &= c.frames_to_tc(total, 24) == "00:00:30:00" and not probs and cuts[1]["rec_in"] == cuts[0]["dur"]
bad = list(csv.DictReader(io.StringIO("clip,in,out,note\nA,00:00:01:24,00:00:02:00,x\nB,00:00:05:00,00:00:04:00,y\n")))
_, _, probs = c.build(bad, 24)
print("bad rows:", probs)
ok &= len(probs) == 2 and "not valid at 24 fps" in probs[0] and "not after" in probs[1]
print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
