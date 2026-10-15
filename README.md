# cv-toolkit (David Prado)

Builds David's tailored CVs and cover letters as .docx + PDF from small
markdown files, with his exact Word templates. Nothing here needs to be read
into a chat's context: clone, write the markdown, run one command.

The content rules (what to tailor, what never to add, delivery rules) live in
the "Aplicaciones Tech" Claude project, in `cv/cv-structure.md`. The master CV
content is `cv/master-cv.md` in that project.

## Usage

```bash
git clone --depth 1 https://github.com/davitpra/cv-toolkit && cd cv-toolkit
./make.sh cv tailored.md "Company" [max_pages]   # default max 2
./make.sh cl letter.md "Company"                 # default max 1
```

Outputs go to `out/` (git-ignored):
- `Resume - David Prado - <Company>.pdf` (deliver only this; the .docx is an intermediate file)
- `Cover Letter - David Prado - <Company>.docx` and `.pdf` (deliver both)

Each run prints a short report:
1. `check_pdf.py`: page count, lines holding a single word, and the last lines of
   every page but the last (to spot a header left at the bottom). Text only,
   so the PDF doesn't need to be rendered and looked at. Only render a page
   (`pdftoppm -r 60 -png`) when the report flags something you can't judge.
2. `detect_summary.py`: the li-human detector. CV: SLOP DENSITY and FINGERPRINT
   only (2 "curly quote" from the typographic apostrophes in the summary are
   expected). Cover letter: every check plus the verdict; iterate until PASS.

To fix a flag, edit the one line in the markdown and rerun. Don't rewrite the
whole file.

## Files

| File | What it is |
|---|---|
| `make.sh` | build → PDF → check → detector, one command |
| `build_cv.py` | CV markdown → .docx with the master CV's exact styles |
| `build_coverletter.py` | letter markdown → .docx from the Word cover letter template |
| `check_pdf.py` | text-only layout check |
| `detect_summary.py` | runs li-human `detect.py` and summarizes it |
| `templates/cv-template.docx` | master CV ("Resume - David Prado Master EN NUEVO.docx"): page setup, styles, bullets, contact line |
| `templates/coverletter-template.docx` | Word cover letter template (Arial, embedded fonts removed) |

## CV markdown format (what `build_cv.py` parses)

```
# DAVID PRADO                                → name
Title: Senior Frontend Developer             → title line
Contact: ...                                 → copied verbatim from the template (text here is ignored)
## PROFESSIONAL SUMMARY                      → section heading
Plain line                                   → body paragraph (supports **bold**)
**Core stack:** TypeScript, ...              → skill line (body paragraph with bold label)
### Role title | Mar 2024 – Present          → role/education header; date after the LAST " | "
Company | City, Country                      → first plain line after ### = meta line
Plain line                                   → body paragraph (e.g. Independent intro)
#### Project · Client | Aug 2026 – Present   → indented project header
- Bullet text with **metrics**               → bullet (indented if under ####)
**Stack:** Next.js · React                   → body line (indented if under ####)
```
- One paragraph per line; blank lines are ignored.
- A `###` or `##` ends the current `####` project block.
- Typographic apostrophes in the summary (I’m, I’ve), en dashes in dates, "·" and "|" separators.
- `&` and other characters are escaped automatically.

Visual spec (built in, never change it to make things fit): Letter, margins
0.53" top/bottom and 0.75" left/right, Arial; name 19pt, title 12pt, contact
10pt, centered; section headings 12pt bold uppercase; role headers 10.5pt bold
with the date right-aligned; project headers 10pt bold indented; body and
bullets 10pt with "●" bullets.

## Cover letter markdown format (what `build_coverletter.py` parses)

```
Role: Senior Full-Stack Developer
Date: October 15, 2026          (optional, defaults to today)
Greeting: Hi Sarah,
---
First paragraph.

Second paragraph.
```
- Title becomes `David Prado – <Role>`. Header lines (email, phone, address,
  LinkedIn, davitprado.com) and the sign-off (Best regards, David Prado, phone,
  email) are kept from the template.
- Body paragraphs are separated by blank lines; each one is cloned from the
  template's body paragraph style. Keep the letter to one page.
- Never mention the Civil Engineering degree.
