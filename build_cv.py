#!/usr/bin/env python3
"""Build a tailored CV (.docx) from a CV markdown file, using David's master
CV .docx as the template so fonts, spacing, tabs, indents and bullets match
exactly.

Usage:
    python3 build_cv.py <cv.md> <template.docx> <out.docx>

The markdown format is described in README.md (same format as master-cv.md).
Normally you don't call this directly: use ./make.sh cv ...
"""
import re
import sys
import zipfile
from xml.sax.saxutils import escape

FONT = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial" />'
TABS = '<w:tabs><w:tab w:val="right" w:pos="10080" /></w:tabs>'
BODY_SPACING = '<w:spacing w:after="30" w:line="236" w:lineRule="auto" />'


def rpr(size, bold=False):
    b = '<w:b w:val="1" /><w:bCs w:val="1" />' if bold else ''
    return f'<w:rPr>{FONT}{b}<w:sz w:val="{size}" /><w:szCs w:val="{size}" /><w:lang w:val="en-US" /></w:rPr>'


def run(text, size=20, bold=False):
    return f'<w:r>{rpr(size, bold)}<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def inline(text, size=20):
    """Render text with **bold** segments as runs."""
    out = []
    for i, part in enumerate(re.split(r'\*\*(.+?)\*\*', text)):
        if part:
            out.append(run(part, size, bold=(i % 2 == 1)))
    return ''.join(out)


def para(ppr, runs):
    return f'<w:p><w:pPr>{ppr}</w:pPr>{runs}</w:p>'


def p_name(text):
    return para('<w:spacing w:after="40" /><w:jc w:val="center" />', run(text, 38, True))


def p_title(text):
    return para('<w:spacing w:after="30" w:line="236" w:lineRule="auto" /><w:jc w:val="center" />',
                run(text, 24, True))


def p_section(text):
    return para('<w:spacing w:before="160" w:after="60" />', run(text, 24, True))


def p_header(left, right, indented):
    # Job / education header (H3) or project header (H4): bold left, date right-aligned by tab.
    if indented:
        ppr = f'<w:keepNext w:val="1" />{TABS}<w:spacing w:before="110" w:after="10" /><w:ind w:left="200" />'
        size = 20
    else:
        ppr = f'<w:keepNext w:val="1" />{TABS}<w:spacing w:before="90" w:after="10" />'
        size = 21
    runs = run(left, size, True)
    if right:
        runs += f'<w:r>{rpr(20)}<w:tab /></w:r>' + run(right)
    return para(ppr, runs)


def p_meta(text):
    # "Company | Location" line right under an H3 header.
    return para(f'<w:keepNext w:val="1" />{BODY_SPACING}', inline(text))


def p_body(text, indented):
    ind = '<w:ind w:left="200" />' if indented else ''
    return para(BODY_SPACING + ind, inline(text))


def p_bullet(text, indented):
    ind = '<w:ind w:left="560" w:hanging="220" />' if indented else ''
    ppr = ('<w:pStyle w:val="ListParagraph" /><w:numPr><w:ilvl w:val="0" /><w:numId w:val="2" /></w:numPr>'
           + BODY_SPACING + ind + '<w:rPr />')
    return para(ppr, inline(text))


def split_date(s):
    if ' | ' in s:
        left, right = s.rsplit(' | ', 1)
        return left.strip(), right.strip()
    return s.strip(), ''


def build(md_text, template_xml):
    # Contact paragraph is copied verbatim from the template (keeps the mailto hyperlink).
    paras = re.findall(r'<w:p[ >].*?</w:p>', template_xml, re.S)
    contact = next(p for p in paras if 'davitprado@outlook.com' in p)

    out = []
    in_project = False      # inside an H4 block -> indented bullets/body
    after_h3 = False        # next plain line is the meta line
    for raw in md_text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith('#### '):
            out.append(p_header(*split_date(line[5:]), indented=True))
            in_project, after_h3 = True, False
        elif line.startswith('### '):
            out.append(p_header(*split_date(line[4:]), indented=False))
            in_project, after_h3 = False, True
        elif line.startswith('## '):
            out.append(p_section(line[3:].strip().upper()))
            in_project, after_h3 = False, False
        elif line.startswith('# '):
            out.append(p_name(line[2:].strip()))
        elif line.startswith('Title:'):
            out.append(p_title(line[6:].strip()))
        elif line.startswith('Contact:'):
            # Opt-in: a Contact line without "London" drops the template's "London, ON | " prefix.
            out.append(contact if 'London' in line else contact.replace('London, ON | ', ''))
        elif line.startswith('- '):
            out.append(p_bullet(line[2:].strip(), in_project))
            after_h3 = False
        elif after_h3:
            out.append(p_meta(line.strip()))
            after_h3 = False
        else:
            out.append(p_body(line.strip(), in_project))

    head = template_xml[:template_xml.index('<w:body>') + len('<w:body>')]
    sect = re.findall(r'<w:sectPr>.*?</w:sectPr>', template_xml, re.S)[-1]
    return head + ''.join(out) + sect + '</w:body></w:document>'


def main():
    md_path, tpl_path, out_path = sys.argv[1:4]
    md_text = open(md_path, encoding='utf-8').read()
    with zipfile.ZipFile(tpl_path) as zin:
        template_xml = zin.read('word/document.xml').decode('utf-8-sig')
        new_xml = build(md_text, template_xml)
        with zipfile.ZipFile(out_path, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = new_xml.encode('utf-8') if item.filename == 'word/document.xml' else zin.read(item.filename)
                zout.writestr(item, data)
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
