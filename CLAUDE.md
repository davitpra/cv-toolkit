# cv-toolkit

Read README.md for usage and the markdown formats. Short version:

- `./make.sh cv tailored.md "Company" [max_pages]` and `./make.sh cl letter.md "Company"`.
- Don't read the docx or pdf skills and don't open `word/document.xml`: the scripts handle the format.
- Trust the text report from `check_pdf.py`; render a page to PNG only when a flag needs a visual check.
- Fix problems by editing single lines of the markdown (Edit), then rerun `make.sh`.
- CV: deliver only the PDF. Cover letter: deliver the .docx and the PDF.
- Never add or mention the Civil Engineering degree.
