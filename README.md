# Academic AI Writing Skills Suite

A dual-skill toolkit for autonomous AI agents, researchers, and scholars. Combines forensic anti-detection stylometry, robust anti-plagiarism synthesis (< 4% similarity), automated document data extraction (PDF and Word), and publication-grade `.docx` generation with **native, editable Word equations (OMML)**.

Compatible with **Antigravity IDE**, **Claude Code**, **Cursor**, **ChatGPT**, **Windsurf**, and **Codex CLI**.

---

## Included Agent Skills

```
academic-ai-writing-skills/
├── skills/
│   ├── authentic-academic-writer/
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── academic_referee_audit.md
│   │       ├── anti_plagiarism_synthesis.md
│   │       ├── banned_lexicon.md
│   │       ├── burstiness_syntax.md
│   │       ├── methodology_precision_guide.md
│   │       ├── pg_thesis_guide.md
│   │       └── tool_integration_pipeline.md
│   │
│   └── academic-doc-extractor-docx/
│       ├── SKILL.md
│       ├── scripts/
│       │   ├── extract_document.py
│       │   ├── generate_academic_docx.py
│       │   └── MML2OMML.XSL
│       └── references/
│           ├── extraction_protocols.md
│           └── omml_equation_guide.md
```

---

## 1. Skill: `authentic-academic-writer`

### What It Does
Operationalizes empirical forensic stylometry, detection research (Weber-Wulff 2023, Liang 2023, Cabanac 2021), and postgraduate academic standards (Science, Engineering & Technology thesis guidelines) to eliminate machine-generation fingerprints, enforce mathematical/empirical rigor, and keep Turnitin/iThenticate plagiarism similarity strictly below 4%.

### Core Features
* **Postgraduate Thesis & Dissertation Engine:** Full chapter-by-chapter drafting and revision protocols (Chapters 1.0 through 6.0: Introduction, Literature Review, Methodology, Results, Discussion, Conclusion & Recommendations) adhering to institutional guidelines (e.g., JOSTUM PG Thesis Guideline 4th Edition - Section B1 ASET).
* **Autonomous Academic Tool Integration:** Orchestrates `academic-mcp` (paper search & full PDF intake), `fasttrack-literature` (topic debate mapping & Crossref reference verification), `consensus` (evidence consensus search), and real-time literature discovery.
* **Top-Tier Peer Referee Pre-Flight Audit:** Simulates adversarial review (*Nature, Econometrica, JASA, NeurIPS*) across theoretical tightness, baseline fairness, data leakage guards, and claim calibration.
* **Methodology Precision Framework:** Enforces strict five-layer mathematical/statistical specification (parameters, identifying assumptions, Neyman-orthogonal score estimators, asymptotic distributions, and rate transparency) eliminating vague hand-waving.
* **Zero Inline Bolding (`**word**`):** Eliminates mid-sentence bolding habits that give away LLM output. Bolding is restricted strictly to section headers.
* **Zero Em Dashes (`—` or `--`):** Eliminates the excessive em dashes that LLMs generate at 300%–500% the human rate.
* **Zero Bullet-Point Laundry Lists:** Replaces fragmented bullet-point prose with flowing, continuous academic paragraphs.
* **The Nine-Lever Humanization Framework:**
  1. *Perplexity Injection:* Domain-specific technical nouns; zero generic top-token verbs.
  2. *Burstiness Enforcement:* Jagged sentence distribution mixing 4–8 word assertions with 35–50+ word periodic clauses (standard deviation > 10 words; longest sentence exceeds shortest by 20+ words).
  3. *Hedge Surgery:* Excises institutional softening (*it is important to note that*, *tends to*, *often*).
  4. *Structural Flattening:* Eliminates boilerplate essay arcs, tricolons (rule-of-three symmetry), and micro-recaps.
  5. *Specificity Anchoring:* Replaces generic claims with exact numbers, sample sizes, and empirical parameters.
  6. *Authentic Academic Voice:* Authoritative scholarly tone with decisive epistemic positioning.
  7. *Organic Transitions:* Replaces *Furthermore*, *Moreover*, and *Additionally* with causal links.
  8. *Punctuation Normalization:* Straight quotes; clean semicolons; zero mid-sentence announcement colons.
  9. *RLHF Voice Strip:* Eliminates compulsive balanced neutrality and patronizing explanations.
* **Anti-Plagiarism Matrix (< 4% Target):** Enforces atomic concept extraction and multi-source synthesis (weaving 2–3 sources per paragraph) to prevent sequential sentence patchwriting.

---

## 2. Skill: `academic-doc-extractor-docx`

### What It Does
Extracts structural and quantitative research data from PDFs and Word documents for literature reviews, and compiles academic drafts into clean Microsoft Word (`.docx`) files with **native, editable equations**.

### Core Features
* **Multi-Format Ingestion (PDF & DOCX):**
  * Parses metadata (authors, title, dates, DOIs), section hierarchies, tables, and candidate formulas.
  * Powered by `PyMuPDF` (`fitz`) and `python-docx`.
* **Native Editable Equations (OMML):**
  * Converts LaTeX formulas (both display `$$...$$` and inline `$...$`) into native **Office Math Markup Language (OMML)** (`<m:oMath>` / `<m:oMathPara>`).
  * Uses `latex2mathml` and Microsoft's official `MML2OMML.XSL` XSLT stylesheet via `lxml`.
  * **100% Interactive:** When opened in Microsoft Word, clicking any formula opens Word’s built-in **Equation Editor** for direct editing.
* **Clean Academic Formatting:**
  * Standard 1.0-inch margins, Times New Roman 12pt body typography, 1.15 line spacing, 6pt after, formatted headings, and shaded tables.

---

## Quickstart & CLI Usage

### Prerequisites
```bash
pip install python-docx pymupdf lxml latex2mathml
```

### Document Extraction
```bash
# Print a structured human-readable breakdown of a PDF
python skills/academic-doc-extractor-docx/scripts/extract_document.py "paper.pdf"

# Export structured JSON (sections, tables, detected formulas)
python skills/academic-doc-extractor-docx/scripts/extract_document.py "paper.pdf" --json --output "extracted_notes.json"

# Extract from a Word document
python skills/academic-doc-extractor-docx/scripts/extract_document.py "manuscript.docx" --output "summary.md"
```

### DOCX Generation with Native Equations
```bash
# Compile any academic Markdown draft with LaTeX into a clean .docx
python skills/academic-doc-extractor-docx/scripts/generate_academic_docx.py "draft.md" "manuscript.docx"
```

---

## Installation Across AI Environments

### Antigravity IDE / Agent Systems
Clone directly into your workspace's `.agents/skills` or your global config `~/.gemini/config/skills`:
```bash
# Workspace installation
git clone https://github.com/Timoyaj/academic-ai-writing-skills.git .agents/skills/academic-ai-writing-skills
```

### Claude Code
Install using the skills command:
```bash
claude-code skills add https://github.com/Timoyaj/academic-ai-writing-skills
```

### Cursor & Windsurf
Add the skill paths to `.cursorrules` or `.windsurfrules`:
```
Follow skills in skills/authentic-academic-writer/SKILL.md and skills/academic-doc-extractor-docx/SKILL.md
```

---

## Empirical Research Foundations

This suite synthesizes findings from key academic integrity and forensic stylometry literature:
* **Weber-Wulff, D., et al. (2023).** Testing of detection tools for AI-generated text. *International Journal for Educational Integrity*, 19(26).
* **Liang, W., et al. (2023).** GPT detectors are biased against non-native English writers. *Patterns*, 4(7), 100779.
* **Cabanac, G., Labbé, C., & Magazinov, A. (2021).** Tortured phrases: A dubious footprint of illicit text spinning in scientific publications. *Bulletin of the ASIS&T*.
* **Sadasivan, V. S., et al. (2023).** Can AI-Generated Text be Reliably Detected? *arXiv:2303.11156*.

---

## License

MIT License. Developed for open academic research and ethical scholarly writing.
