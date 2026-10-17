#!/usr/bin/env python3
"""Build a cover letter (.docx) from a small markdown file, using David's
Word cover letter template. Header lines (email, phone, address, LinkedIn,
davitprado.com) and the sign-off are kept exactly as in the template.

Usage:
    python3 build_coverletter.py <letter.md> <template.docx> <out.docx>

letter.md format:

    Role: Senior Full-Stack Developer
    Date: October 15, 2026          (optional, defaults to today)
    Greeting: Hi Sarah,
    ---
    First paragraph.

    Second paragraph.

Body paragraphs are separated by blank lines. Normally you don't call this
directly: use ./make.sh cl ...
"""
import datetime
import re
import sys
import zipfile
from xml.sax.saxutils import escape

PARA_RE = re.compile(r'<w:p[ >].*?</w:p>', re.S)
RUN_RE = re.compile(r'<w:r[ >].*?</w:r>', re.S)


def parse(md):
    head, _, body = md.partition('\n---')
    fields = {}
    for line in head.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fields[k.strip().lower()] = v.strip()
    paras = [' '.join(p.split()) for p in re.split(r'\n\s*\n', body) if p.strip()]
    if 'role' not in fields or 'greeting' not in fields or not paras:
        sys.exit('letter.md needs Role:, Greeting:, a --- line and at least one paragraph')
    if not fields.get('date'):
        d = datetime.date.today()
        fields['date'] = f'{d.strftime("%B")} {d.day}, {d.year}'
    return fields, paras


def set_text(p, text):
    """Keep the paragraph properties and the first run's formatting; replace all runs with one."""
    runs = RUN_RE.findall(p)
    rpr = re.search(r'<w:rPr>.*?</w:rPr>', runs[0], re.S)
    new_run = f'<w:r>{rpr.group(0) if rpr else ""}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    start = p.index(runs[0])
    end = p.rindex(runs[-1]) + len(runs[-1])
    return p[:start] + new_run + p[end:]


ADDRESS_SUFFIX = ' | 1440 Beaverbrook London,Ontario N6H 5W6'


def build(fields, paras, xml):
    # Opt-in: "Address: none" in letter.md leaves the street address out of the header.
    if fields.get('address', '').lower() == 'none':
        xml = xml.replace(ADDRESS_SUFFIX, '')
    ps = PARA_RE.findall(xml)
    text = [''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p)) for p in ps]

    def find(pred, what):
        for i, t in enumerate(text):
            if pred(t):
                return i
        sys.exit(f'template: could not find the {what} paragraph')

    i_title = find(lambda t: t.startswith('David Prado –'), 'title')
    i_date = find(lambda t: re.match(r'^[A-Z][a-z]+ \d', t.strip()), 'date')
    i_greet = find(lambda t: t.strip().startswith('Hi '), 'greeting')
    i_sign = find(lambda t: t.strip().startswith('Best regards'), 'sign-off')
    body_idx = [i for i in range(i_greet + 1, i_sign) if text[i].strip()]

    new = list(ps)
    new[i_title] = set_text(ps[i_title], f'David Prado – {fields["role"]}')
    new[i_date] = set_text(ps[i_date], fields['date'])
    new[i_greet] = set_text(ps[i_greet], fields['greeting'])
    proto = ps[body_idx[0]]
    body_xml = ''.join(set_text(proto, t) for t in paras)
    for j, i in enumerate(body_idx):
        new[i] = body_xml if j == 0 else ''

    out, pos = [], 0
    for old, rep in zip(ps, new):
        k = xml.index(old, pos)
        out.append(xml[pos:k])
        out.append(rep)
        pos = k + len(old)
    out.append(xml[pos:])
    return ''.join(out)


def main():
    md_path, tpl_path, out_path = sys.argv[1:4]
    fields, paras = parse(open(md_path, encoding='utf-8').read())
    with zipfile.ZipFile(tpl_path) as zin:
        xml = zin.read('word/document.xml').decode('utf-8')
        new_xml = build(fields, paras, xml)
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = new_xml.encode('utf-8') if item.filename == 'word/document.xml' else zin.read(item.filename)
                zout.writestr(item, data)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
