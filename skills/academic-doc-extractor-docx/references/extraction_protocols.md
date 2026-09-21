# Document Extraction Protocols for Academic Literature Review

This guide outlines the systematic methodology for extracting empirical facts, statistical parameters, and theoretical equations from research papers (PDF and Word `.docx`) to support literature reviews without patchwriting or plagiarism.

---

## 1. The Atomic Extraction Matrix

When reading raw PDF or Word files, never copy-paste narrative sentences into the literature review notes. Instead, extract information into an atomic matrix:

| Paper ID | Study Metadata | Target Cohort & Design | Quantitative Findings | Core Equation / Theoretical Model | Limitations & Boundary Conditions |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Paper A | Author(s), Year, Journal, DOI | Sample size $N$, sampling phases, stratification criteria | Effect size, $p$-value, confidence intervals | Key structural equation in LaTeX | Excluded groups, model misspecification risk |

### Information Extraction Checklist:
1. **Bibliographic Authenticity:** Extract the exact DOI and confirmed author names.
2. **Identification Strategy:** Is the design observational, experimental, or quasi-experimental (e.g., two-phase stratified clustered sampling)?
3. **Primary Estimators:** Did the authors use IPW, AIPW, TMLE, or Double Machine Learning?
4. **Parameter Estimates:** Extract raw numbers ($N=1,420$, $\beta = -0.18$, $p = 0.012$) rather than the author's prose description ("mortality dropped significantly").

---

## 2. Handling Complex PDF Layouts

Scientific PDFs frequently present technical extraction challenges:
* **Multi-Column Formatting:** `extract_document.py` reads page blocks to preserve natural column reading order rather than interleaving lines across adjacent columns.
* **Mathematical Notation:** In PDFs, mathematical symbols often render as disjoint characters or private Unicode glyphs. When extracting formulas, cross-reference the raw text blocks with the article's equation numbers and re-encode expressions into clean LaTeX.
* **Embedded Tables:** PyMuPDF's `find_tables()` isolates tabular borders and cell boundaries, extracting headers and cell rows directly.

---

## 3. Transitioning from Extraction to Synthesis

Once atomic notes are extracted:
1. Close the original source document.
2. Do not attempt to summarize Paper A in one block.
3. Group findings by **thematic dimension** (e.g., all papers discussing cluster-level cross-fitting vs all papers discussing survey-weighted loss functions).
4. Draft the literature review by synthesizing at least 2–3 sources per paragraph, following the `authentic-academic-writer` principles.
