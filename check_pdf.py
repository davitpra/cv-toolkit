#!/usr/bin/env python3
"""Cheap text-only layout check for a generated PDF, so the PDF doesn't have
to be rendered to images and looked at every time.

Usage:
    python3 check_pdf.py <file.pdf> [max_pages]

Prints the page count and flags:
  - more pages than max_pages
  - lines that hold a single short word (a wrapped paragraph's lonely last word)
  - the last lines of each page that is not the last one (to spot a header
    left alone at the bottom)
Exit code 1 if anything is flagged.
"""
import re
import subprocess
import sys


def main():
    pdf = sys.argv[1]
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else None
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    pages = int(re.search(r'Pages:\s+(\d+)', info).group(1))
    text = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    page_texts = text.split('\f')

    flags = []
    if max_pages and pages > max_pages:
        flags.append(f'{pages} pages, limit is {max_pages}')

    for n, pt in enumerate(page_texts[:pages], 1):
        lines = [l.rstrip() for l in pt.splitlines()]
        for i, l in enumerate(lines):
            s = l.strip().lstrip('●•').strip()
            prev = lines[i - 1].strip() if i else ''
            # one short word on its own line, right after a long line: a wrapped widow
            if s and len(s.split()) == 1 and len(s) < 15 and len(prev) > 60:
                flags.append(f'p{n}: single word on its own line: "{s}" (after "...{prev[-40:]}")')
        if n < pages:
            tail = [l.strip() for l in lines if l.strip()][-2:]
            print(f'p{n} ends with: ' + ' / '.join(t[:70] for t in tail))

    print(f'pages: {pages}')
    for f in flags:
        print('FLAG ' + f)
    print('OK' if not flags else f'{len(flags)} flag(s)')
    sys.exit(1 if flags else 0)


if __name__ == '__main__':
    main()
