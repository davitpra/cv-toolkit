#!/usr/bin/env python3
"""ATS check for a generated CV PDF: readable text + keyword coverage.

Usage:
    python3 check_ats.py <cv.pdf> <keywords.txt> [min_coverage_percent]

keywords.txt is written by Claude from the job posting (one term per line,
aliases separated by "|", exactly as the posting spells them):

    # required        <- must-haves from the posting that the master CV supports
    Node.js | NodeJS
    PostgreSQL | Postgres
    # preferred       <- nice-to-haves (reported, never block)
    Docker
    # gaps            <- required by the posting but NOT in master-cv.md (never add them)
    Kubernetes

Checks:
  1. Text layer: the PDF yields real text, standard headings, contact data in
     the body, no garbled characters.
  2. Coverage of "required" terms (gaps excluded from the denominator). Fails
     (exit 1) under min_coverage_percent (default 80). Always lists the terms
     that are missing, and the required terms that appear only in the skills
     list (no experience bullet gives them context).
"""
import re
import subprocess
import sys

HEADINGS = ['PROFESSIONAL SUMMARY', 'TECHNICAL SKILLS', 'PROFESSIONAL EXPERIENCE', 'EDUCATION']


def parse_keywords(path):
    groups = {'required': [], 'preferred': [], 'gaps': []}
    cur = None
    for raw in open(path, encoding='utf-8'):
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#'):
            name = line.lstrip('#').strip().lower().split()[0] if line.lstrip('#').strip() else ''
            cur = name if name in groups else None
            continue
        if cur:
            groups[cur].append([a.strip() for a in line.split('|') if a.strip()])
    return groups


def find(term, text):
    pat = r'(?<![a-z0-9])' + re.escape(term.lower()) + r'(?![a-z0-9])'
    return re.search(pat, text) is not None


def hit(aliases, text):
    return next((a for a in aliases if find(a, text)), None)


def split_sections(text):
    """Return {'summary','skills','experience','other'} text blocks by heading."""
    up = text
    marks = []
    for h, key in [('PROFESSIONAL SUMMARY', 'summary'), ('TECHNICAL SKILLS', 'skills'),
                   ('PROFESSIONAL EXPERIENCE', 'experience'), ('EDUCATION', 'other')]:
        i = up.find(h)
        if i >= 0:
            marks.append((i, key))
    marks.sort()
    out = {'summary': '', 'skills': '', 'experience': '', 'other': ''}
    for n, (i, key) in enumerate(marks):
        j = marks[n + 1][0] if n + 1 < len(marks) else len(up)
        out[key] += up[i:j]
    out['head'] = up[:marks[0][0]] if marks else ''
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    pdf, kwfile = sys.argv[1], sys.argv[2]
    minimum = float(sys.argv[3]) if len(sys.argv) > 3 else 80.0

    raw = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    flags = []

    # 1. text layer
    if len(raw.strip()) < 500:
        flags.append('almost no extractable text: the PDF may be an image')
    for h in HEADINGS:
        if h not in raw:
            flags.append(f'standard heading not found in the text: {h}')
    if not re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', raw):
        flags.append('no email found in the body text (contact must not live only in a header/footer)')
    if not re.search(r'\d{3}[\s.)-]*\d{3}[\s.-]*\d{4}', raw):
        flags.append('no phone number found in the body text')
    if '(cid:' in raw or '�' in raw:
        flags.append('garbled characters in the extracted text (font encoding problem)')
    odd = sorted({c for c in raw if ord(c) > 127 and c not in '●·–—’‘“”•|é'})
    if odd:
        flags.append('unusual characters an ATS may drop: ' + ' '.join(odd))

    # 2. keyword coverage
    kw = parse_keywords(kwfile)
    text = re.sub(r'\s+', ' ', raw.lower())
    secs = split_sections(re.sub(r'\s+', ' ', raw))
    secs = {k: v.lower() for k, v in secs.items()}

    req = kw['required']
    found, missing, skills_only = [], [], []
    for aliases in req:
        a = hit(aliases, text)
        if a:
            found.append(aliases[0])
            in_exp = any(find(x, secs['experience']) for x in aliases)
            in_sum = any(find(x, secs['summary']) for x in aliases)
            if not in_exp and not in_sum:
                skills_only.append(aliases[0])
        else:
            missing.append(' | '.join(aliases))
    pct = 100.0 * len(found) / len(req) if req else 100.0

    pref_missing = [' | '.join(a) for a in kw['preferred'] if not hit(a, text)]
    pref_found = len(kw['preferred']) - len(pref_missing)

    print(f'ATS text layer: {"OK" if not flags else str(len(flags)) + " flag(s)"}')
    for f in flags:
        print('  FLAG ' + f)
    print(f'Required keywords: {len(found)}/{len(req)} = {pct:.0f}% (minimum {minimum:.0f}%)')
    print('  NOT COVERED: ' + (', '.join(missing) if missing else 'none'))
    if skills_only:
        print('  only in the skills list (no summary/experience context): ' + ', '.join(skills_only))
    if kw['preferred']:
        print(f'Preferred keywords: {pref_found}/{len(kw["preferred"])}')
        if pref_missing:
            print('  not covered: ' + ', '.join(pref_missing))
    if kw['gaps']:
        print('Gaps (posting asks, master CV does not support; not added): '
              + ', '.join(' | '.join(a) for a in kw['gaps']))

    ok = not flags and pct >= minimum
    print('ATS OK' if ok else 'ATS FAIL')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
