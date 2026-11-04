#!/usr/bin/env bash
# One command per document: build the .docx, convert to PDF, run the text-only
# layout check and the li-human detector, and print a short summary.
#
#   ./make.sh cv <tailored.md> "<Company>" [max_pages] [keywords.txt]  -> out/Resume - David Prado - <Company>.pdf
#       with keywords.txt (see check_ats.py) it also runs the ATS check, min 80% coverage
#   ./make.sh cl <letter.md>   "<Company>"               -> out/Cover Letter - David Prado - <Company>.docx + .pdf
#
# max_pages defaults to 2 for the CV and 1 for the cover letter.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
kind="${1:?cv or cl}"; src="${2:?markdown file}"; company="${3:?company name}"
OUT="$HERE/out"; mkdir -p "$OUT"

case "$kind" in
  cv) name="Resume - David Prado - $company"; max="${4:-2}"
      python3 "$HERE/build_cv.py" "$src" "$HERE/templates/cv-template.docx" "$OUT/$name.docx" >/dev/null ;;
  cl) name="Cover Letter - David Prado - $company"; max="${4:-1}"
      python3 "$HERE/build_coverletter.py" "$src" "$HERE/templates/coverletter-template.docx" "$OUT/$name.docx" >/dev/null ;;
  *)  echo "first argument must be cv or cl" >&2; exit 2 ;;
esac

soffice --headless --convert-to pdf --outdir "$OUT" "$OUT/$name.docx" >/dev/null 2>&1
echo "built: $OUT/$name.pdf"

python3 "$HERE/check_pdf.py" "$OUT/$name.pdf" "$max" || true

# ATS check (CV only, needs a keywords file written from the posting)
if [ "$kind" = "cv" ] && [ -n "${5:-}" ]; then
  python3 "$HERE/check_ats.py" "$OUT/$name.pdf" "$5" 80 || true
elif [ "$kind" = "cv" ]; then
  echo "ATS check skipped: no keywords file (5th argument)"
fi

# li-human detector, summarized. CV: only slop and fingerprint matter.
python3 "$HERE/detect_summary.py" "$kind" "$src"
