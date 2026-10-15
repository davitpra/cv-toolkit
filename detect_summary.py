#!/usr/bin/env python3
"""Run the li-human detector on a draft and print a short summary.

Usage:
    python3 detect_summary.py <cv|cl> <file.md>

CV: only SLOP DENSITY and FINGERPRINT (voice/burstiness don't apply to a CV;
typographic apostrophes in the summary are expected and count as "curly quote").
Cover letter: every check plus the verdict.
"""
import glob
import json
import subprocess
import sys

kind, path = sys.argv[1:3]
candidates = glob.glob('/mnt/skills/plugins/li-human/detect.py') + \
    glob.glob('/root/.claude/skills/synced/*/li-human/detect.py')
if not candidates:
    print('li-human detect.py not found; skipped')
    sys.exit(0)

res = subprocess.run([sys.executable, '-I', candidates[0], '--json', path], capture_output=True, text=True)
d = json.loads(res.stdout)
keep = ['SLOP DENSITY', 'FINGERPRINT'] if kind == 'cv' else list(d['checks'])
for k in keep:
    c = d['checks'][k]
    print(f'{k}: {c["score"]:.0f} ({c["detail"]})')
if kind == 'cl':
    print(f'human score {d["human_score"]:.0f}: {d["verdict"]}')
