---
name: academic-doc-extractor-docx
description: >
  Extract research data, methodologies, structured tables, and mathematical formulas from
  PDF and Word (.docx) documents for literature reviews. Generate clean, publication-grade
  Microsoft Word (.docx) output featuring native, editable OMML equations and formulas.
metadata:
  trigger: extract document, extract pdf, extract docx, convert to docx with equations, generate docx, editable equations, literature review extraction
  author: Antigravity
---

# Academic Document Extractor & Clean DOCX Generator

This skill provides an automated pipeline to ingest scientific documents (PDF, Word `.docx`), extract structural and quantitative data for literature synthesis without patchwriting, and compile publication-grade Microsoft Word (`.docx`) documents with **native, editable equations** using Office Math Markup Language (OMML).

---

## 1. Core Capabilities

1. **Document Data Extraction (PDF & MS Word):**
   * Parses text, structured tables, section headings, metadata (author, title, date), and mathematical formulas from `.pdf` and `.docx` files.
   * Isolates quantitative parameters (sample size $N$, $p$-values, effect sizes, operational metrics) to support literature synthesis while avoiding verbatim text duplication (similarity index $< 4\%$).
2. **Native Editable Equation Generation (`.docx`):**
   * Converts display (`$$...$$`) and inline (`$...$`) LaTeX mathematical formulas directly into native Microsoft Word **Office Math Markup Language (OMML)** elements (`<m:oMath>` / `<m:oMathPara>`).
   * When opened in Word, every formula is **100% interactive and editable** using Word's built-in Equation Editor (unlike raster images or non-editable MathType snapshots).
3. **Clean Academic Formatting:**
   * Standard academic layout: 1.0-inch margins, Times New Roman 12pt body font, 1.15 line spacing, 6pt space after, and standardized heading styles (Heading 1/2/3).
   * Complies with the `authentic-academic-writer` guidelines: zero mid-sentence bolding, zero em-dashes, zero ASCII box art, and flowing paragraphs.

---

## 2. Extraction Protocol (PDF & DOCX)

To extract structured literature review data from an input paper:

```bash
# Extract structured overview and print readable summary
python scripts/extract_document.py "path/to/paper.pdf"

# Extract to structured JSON for data pipeline processing
python scripts/extract_document.py "path/to/paper.pdf" --json --output "extracted_data.json"

# Extract from Word (.docx) file
python scripts/extract_document.py "path/to/manuscript.docx" --output "extracted_summary.md"
```

### Extracted Data Structure:
* `metadata`: Title, author, page count, file type.
* `sections`: Section headings and extracted body text.
* `tables`: Extracted tabular rows and headers.
* `formulas`: Detected algebraic and LaTeX equation strings.

---

## 3. Generating Clean DOCX with Native Editable Equations

To generate a polished Microsoft Word `.docx` file from an academic markdown draft:

```bash
python scripts/generate_academic_docx.py "input_draft.md" "output_manuscript.docx"
```

### Formula Syntax Rules for Native OMML Output:
* **Display Equations (Centered):**
  Wrap formulas in double dollar signs on their own lines:
  ```latex
  $$\psi^*(W_i; \theta_0, \eta_0) = \frac{R_i}{\pi_{2i|1}} \psi(W_i; \theta_0, \eta_0) - \left( \frac{R_i - \pi_{2i|1}}{\pi_{2i|1}} \right) \mathbb{E}[\psi(W_i; \theta_0, \eta_0) \mid W_{1i}]$$
  ```
* **Inline Formulas:**
  Wrap symbols and variables in single dollar signs within text:
  ```latex
  When nuisance estimators achieve convergence rates faster than $n^{-1/4}$ under design-weighted norms...
  ```
* **Conversion Engine:**
  The compilation script leverages `latex2mathml` to generate MathML, transforms it via the bundled Microsoft `MML2OMML.XSL` stylesheet using `lxml`, and embeds the resulting XML elements directly into the Word document tree.

---

## 4. Synthesis Workflow for Literature Reviews

When conducting a literature review on user documents:

```
[User Document: PDF / DOCX]
             │
             ▼
[Step 1: Extract Data]
  • Run extract_document.py
  • Extract core hypotheses, sample sizes, models, and findings as atomic notes.
             │
             ▼
[Step 2: Synthesize Literature]
  • Apply authentic-academic-writer protocol (anti-plagiarism, concept extraction).
  • Zero mid-sentence bolding, zero em-dashes, jagged burstiness.
             │
             ▼
[Step 3: Compile to DOCX]
  • Run generate_academic_docx.py
  • Produces .docx with native, interactive Word Equation Editor formulas.
```

---

## 5. Script Directory Map

* `scripts/extract_document.py`: PDF and Word document extraction utility.
* `scripts/generate_academic_docx.py`: Markdown-to-DOCX compiler with native OMML equation support.
* `scripts/MML2OMML.XSL`: Microsoft Office MathML-to-OMML XSLT stylesheet.
