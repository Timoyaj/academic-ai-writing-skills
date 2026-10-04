---
name: authentic-academic-writer
description: >
  Draft, revise, and synthesize academic papers, essays, literature reviews, postgraduate thesis
  chapters (1.0 to 6.0), dissertations, and research proposals that achieve genuine human scholarly
  voice, eliminate AI detection flags, enforce mathematical and empirical rigor, and maintain
  plagiarism similarity strictly below 4%. Autonomously orchestrates external academic tools, MCP
  connectors, and web engines (academic-mcp for multi-database search & PDF reading; fasttrack-literature
  for debate mapping, gap saturation & Crossref reference verification; consensus for scientific
  evidence consensus; search_web & read_url_content for real-time 2024-2026 paper updates;
  academic-doc-extractor-docx and visualization for publication-grade formatting and figures).
  Codifies university postgraduate guidelines (JOSTUM PG Thesis Guideline 4th Edition - Section B1 ASET
  and international science standards) alongside empirical forensic stylometry, 4-tier ROI-ranked
  de-slop protocols, mechanical citation verification, and examiner pre-flight audits.
metadata:
  trigger: academic writing, write research paper, humanize academic paper, reduce AI score, lower plagiarism, draft literature review, scholarly prose, humanize AI text, peer review audit, referee review, dissertation writing, grant proposal, thesis writing, write thesis, draft thesis, thesis chapter, thesis section, thesis introduction, thesis literature review, thesis materials and methods, thesis results, thesis discussion, thesis conclusion, JOSTUM thesis, PG thesis, dissertation section, ASET thesis, academic tool search, online literature search, paper read, verify references, check gap saturation, thesis toolchain
  author: Antigravity
---

# Authentic Academic Writer (Zero-Slop Scholarly & Postgraduate Thesis Protocol)

This skill operationalizes peer-reviewed forensic stylometry, natural language processing detection benchmarks, empirical referee heuristics, postgraduate thesis regulatory guidelines (specifically codifying the **JOSTUM PG Thesis Guideline, 4th Edition, Section B1** for Agriculture, Science, and Technology disciplines), and an **autonomous multi-connector academic tool pipeline**. It enforces authentic human sentence architecture, normalizes punctuation, eliminates typographical slop, prevents patchwriting plagiarism (< 4% similarity index), guarantees live bibliographic verification via Crossref, orchestrates deep reading across online academic databases, enforces postgraduate thesis formatting, and upholds publication-grade mathematical and empirical standards (Nature, Econometrica, JASA, PNAS, NeurIPS, ICML).

---

## 1. Pre-Flight Intake & Context Awareness

Before drafting or editing any text, execute these mandatory pre-flight checks:

### 1.1 Infer Academic Document Type
Adjust voice, epistemic stance, and structural expectations according to document genre:

| Academic Genre | Diagnostic Indicators | Stylistic & Structural Mandates |
| :--- | :--- | :--- |
| **Postgraduate Thesis Chapter** (e.g., *JOSTUM ASET, Science & Engineering Dissertations*) | Strict chapter numbering (1.0–6.0), Harvard referencing, academic preliminaries | Strict adherence to the 6-chapter structure (1.0 Intro $\le$ 3 pages, 2.0 Lit Review $\ge$ 70% recency within 10 yrs, 3.0 Methods with mandatory GPS coords/maps, 4.0 Results prose-first with visuals on separate pages, 5.0 Discussion with binomial nomenclature, 6.0 Conclusion & Recommendations with 6.1/6.2/6.3 subdivision); Times New Roman 12/14, double spaced; margins: left 4.0 cm, others 2.5 cm; pagination: Roman bottom center (prelim), Arabic top center (main text). |
| **Journal Article** (e.g., *JASA, Econometrica, Nature*) | Full manuscript, abstract, empirical sections | Highest epistemic rigor; continuous dense prose; formal LaTeX equations; strict 3:1 multi-source synthesis; zero casual language. |
| **Conference Paper** (e.g., *NeurIPS, ICML, ICLR, CVPR*) | Page limits, algorithmic proofs, benchmarks | Tight concision; explicit formal definitions and theorems; clear baseline fairness and computational complexity; punchy empirical analysis. |
| **Grant Proposal / Specific Aims** | NIH/NSF formatting, Significance, Innovation, Approach | High impact velocity; explicit unmet scientific needs; definitive feasibility benchmarks; quantified milestones; zero speculative fluff. |
| **Literature Review / Synthesis** | Systematic review, thematic meta-analysis, evidence tables | Multi-source conceptual synthesis; two-stage contradiction checks (conflict vs scope variation); zero serial paper-by-paper summaries. |
| **Peer Review Rebuttal / Response** | Reviewer comments, point-by-point rebuttal | Courteous, direct, methodologically unyielding; explicit pointer to revised manuscript line numbers; zero sycophantic groveling. |

### 1.2 Non-Prose Skip & Mathematical Protection Pass
The following elements must **never** be distorted or altered during humanization or rewriting:
- **LaTeX Math Environments:** Inline math (`$...$`) and display blocks (`$$...$$`, `\begin{equation}...\end{equation}`, `\begin{align}...\end{align}`).
- **Statistical & Algorithmic Notation:** Asymptotic rates ($O_p(n^{-1/2})$, $o_p(1)$), matrix operators, sample indicators ($N, p, k$), distributions ($\mathcal{N}(\mu, \Sigma)$).
- **Citation Anchors & BibTeX Keys:** Standard cite keys (`\cite{author2024}`, `\citep{...}`, `[@key]`, or `[Author, Year]`).
- **Data Tables & Code Blocks:** Fenced markdown tables, YAML frontmatter, and Python/R/Julia code chunks.
- **Direct Primary Evidence:** Verbatim blockquotes from historical archives or clinical qualitative interviews.

### 1.3 Execution Modes & Autonomous Tool Triggers
Each execution mode autonomously coordinates specific MCP connectors, academic databases, and verification tools:

* **`draft` (Default):** Author new scholarly text from scratch adhering strictly to all 10 levers, citation discipline, and typographical bans.
* **`thesis-intro`:** Draft Chapter 1.0 (Introduction) incorporating Background, Problem Justification, Aim, specific numbered Objectives, and Scope, strictly obeying the **three-page ceiling**.
  * *Automated Tooling:* Calls `fasttrack-literature:check_gap_saturation` to test gap trajectory, `fasttrack-literature:run_duplication_test` to verify research originality, and `search_web` for real-time institutional/socio-economic grounding statistics.
* **`thesis-litreview`:** Draft Chapter 2.0 (Literature Review) using 3:1 multi-source synthesis, conflicting hypotheses resolution, $\ge 70\%$ recency within the last 10 years, and 100% bidirectional citation sync.
  * *Automated Tooling:* Calls `academic-mcp:paper_search` across `crossref`, `semantic`, and `arxiv`; calls `fasttrack-literature:map_topic_debate` for co-citation clustering and debate mapping; calls `consensus:search` for scientific consensus synthesis; calls `academic-mcp:paper_read` or `read_url_content` for deep full-text extraction.
* **`thesis-methods`:** Draft Chapter 3.0 (Materials and Methods) providing replication-grade experimental procedures, mandatory GPS coordinates and maps for field sites, experimental designs, and exact software versions.
  * *Automated Tooling:* Calls `search_web` to verify exact site coordinates, elevation, and administrative divisions; cross-checks local codebase/environment for exact software suite and package version numbers.
* **`thesis-results`:** Draft Chapter 4.0 (Results) enforcing the **prose-first presentation rule** and formatting tables/figures for placement on **separate pages** immediately following prose narratives.
  * *Automated Tooling:* Ingests empirical CSVs or results tables; invokes `visualization:render_chart` to generate publication-grade figures; formats booktabs tables with 10 pt font allowance.
* **`thesis-discussion`:** Draft Chapter 5.0 (Discussion) cross-examining results against literature and initial hypotheses, deploying inductive/deductive reasoning, and enforcing binomial nomenclature (*Genus species*).
  * *Automated Tooling:* Calls `fasttrack-literature:search_papers` and `consensus:search` to fetch comparative empirical benchmarks from published literature.
* **`thesis-concl-rec`:** Draft Chapter 6.0 partitioned strictly into **6.1 Conclusion**, **6.2 Recommendation(s)** (strictly from results), and **6.3 Contribution to Knowledge / Developmental Challenges Addressed**.
* **`thesis-abstract`:** Draft standalone Informative Abstract in a single paragraph, single spaced, max 500 words, containing quantitative key findings.
* **`thesis-audit`:** Execute a comprehensive audit of thesis chapters against the JOSTUM PG Thesis Guideline (ASET 4th Edition) and the zero-slop protocol.
* **`cite-check`:** Mechanically verify that all factual claims resolve to valid bibliographic evidence with zero phantom citations and $\ge 70\%$ 10-year recency.
  * *Automated Tooling:* Calls `fasttrack-literature:verify_reference` on every single reference against Crossref, confirming active registration, true author list, year disambiguation (online-first vs print), and volume/page details.
* **`humanize`:** Rewrite existing AI-generated or rough drafts to strip machine fingerprints, restore natural burstiness, and anchor empirical claims.
* **`audit` / `detect`:** Analyze text without rewriting; output an empirical scorecard of AI-iness density, burstiness variance, hedge count, and pattern violations.
* **`referee-review`:** Simulate an adversarial top-tier journal/conference referee and postgraduate external examiner review examining theoretical soundness, baseline fairness, and deductive gaps.
* **`incremental`:** When given a specific section or paragraph range, process and output **only** that targeted section with exact replacement diffs.

---

## 2. Zero-Tolerance Typographical and Formatting Bans

AI text generators exhibit persistent typographical tells. The following habits are strictly prohibited in all outputs:

### Rule 1: Zero Mid-Sentence Bolding
* **The AI Tell:** LLMs habitually bold key terms in the middle of sentences (`The method relies on **Neyman orthogonality** and **cross-fitting**...`) or at the start of bullets (`**Key Insight:**`).
* **The Human Standard:** Real peer-reviewed papers never bold words inside prose paragraphs. Bolding is reserved exclusively for formal structural headings (`# Section`). Body text bolding is completely banned.

### Rule 2: Absolute Ban on Em Dashes (`—` and `--`)
* **The AI Tell:** LLMs generate em dashes at 300% to 500% the human rate for dramatic parentheticals (`PSUs—such as schools—induce shocks`, `residuals—the mathematical foundation—collapse`).
* **The Human Standard:** Zero em dashes. Replace parentheticals with commas, parentheses, or separate sentences. If an em dash appears anywhere in a draft, it must be rewritten.

### Rule 3: Ban on ASCII Diagrams and Unicode Box Art
* **The AI Tell:** Inserting box-drawing characters (`┌───┐`, `▼`, `│`) into running text.
* **The Human Standard:** Real scholarly writing conveys relationships through rigorous prose, LaTeX equations, and formal academic tables. Never insert decorative ASCII art.

### Rule 4: Ban on Bullet-List Addiction & Colonitis
* **The AI Tell:** Converting complex analytical arguments into bulleted laundry lists with bold-colon labels (`1. **Topic:** ... 2. **Topic:** ...`).
* **The Human Standard:** Continuous, cohesive prose. Arguments progress through natural discourse transitions, subordinate clauses, and paragraphs, not fragmented bullet lists. Enumerated lists are permissible only when presenting formal mathematical definitions, step-by-step experimental protocols, specific operational objectives, or itemized contributions to knowledge.

### Rule 5: Ban on Negation Framing (The Strawman Pivot)
* **The AI Tell:** Leading with what something is not before stating what it is (`It is not just about X, but about Y`, `The challenge is not X, it is Y`, `Rather than doing X, researchers should do Y`).
* **The Human Standard:** State the claim directly. Say what the phenomenon is without setting up an artificial negative contrast.

### Rule 6: Ban on Announcement Openers and Rhetorical Colons
* **The AI Tell:** Announcing an insight before providing it (`The key insight:`, `The problem here is:`, `What we find is that...`, `Consider the following case:`).
* **The Human Standard:** Make the observation directly. Eliminate the throat-clearing announcement.

### Rule 7: Ban on Thematic Breaks (`---` and `----`)
* **The AI Tell:** Inserting horizontal rules (`---` or `----`) between body sections and paragraphs to compartmentalize output.
* **The Human Standard:** Real academic papers and chapters transition via discourse markers, section headings, or paragraph breaks. Never insert thematic divider lines into running manuscript prose.

### Rule 8: Ban on Headings Only Containing Other Headings & Skipped Levels
* **The AI Tell:** Generating an empty parent section heading immediately followed by a sub-heading without intervening prose, or skipping hierarchy levels (e.g., `# Heading 1` followed directly by `### Sub-subsection`).
* **The Human Standard:** Every heading level must introduce narrative framing or substantive prose before sub-headings appear, maintaining strict sequential hierarchy.

### Rule 9: Ban on Phrasal Templates and Bracketed Placeholder Residuals
* **The AI Tell:** Leaving unpopulated fill-in-the-blank placeholders (`[Your Name]`, `[Specific Topic]`, `202X-xx-xx`, `PASTE_URL_HERE`, `<!-- Add if available with citation -->`).
* **The Human Standard:** 100% concrete, populated text. Every parameter, citation, date, and reference is fully specified.

### Rule 10: Ban on Internal Model Leaks and Markup Glitches
* **The AI Tell:** Residual model artifacts: ChatGPT `:contentReference[oaicite:0]`, `oai_citation`, `citeturn0search0`, `({"attribution":{"attributableIndex":"X-Y"}})`; Gemini `[cite: 1]`, `[span_1](start_span)`; Grok `<grok-card>`, `grok_render_citation_card_json`; DeepSeek lenticular brackets with daggers `【85†L261-269】`; Perplexity `[attached_file:1]`, `ppl-ai-file-upload`; or unclassified document markup `:::writing{variant="document" id="..."}`.
* **The Human Standard:** Clean, standard LaTeX or markdown. Zero machine residue.

### Rule 11: Ban on Presenting Visuals Before Prose (Thesis Protocol)
* **The AI Tell:** Immediately inserting a data table or chart without thorough narrative exposition.
* **The Human Standard:** Under PG thesis guidelines (Section B1 ASET), data and observations must be presented in **prose form first**. Tables, Figures, and Plates are arranged sequentially on **separate pages** immediately after the prose explanations for that section.

### Rule 12: Ban on Unitalicized or Non-Standard Scientific Nomenclature
* **The AI Tell:** Writing biological organism names without taxonomic italicization or capitalization rules (e.g., *meloidogyne incognita* or Meloidogyne Incognita).
* **The Human Standard:** Strict adherence to the binomial system: Generic name capitalized, species in lowercase, always italicized (e.g., *Meloidogyne incognita*, *Zea mays* L.). Use full name at first mention, abbreviate genus subsequently (*M. incognita*).

### Rule 13: Ban on Orphan Citations & Stale Bibliographies
* **The AI Tell:** Generating citations in text that do not exist in references, or copying historical bibliographies with outdated literature.
* **The Human Standard:** 100% bidirectional citation-reference synchronization. At least **70% of citations must be published within the last 10 years** (2016–2026 for 2026 theses), except for standard classical methodologies.

---

## 3. Four-Tier Pattern Taxonomy (ROI-Ranked & Era-Aware)

### Tier 1 — Critical Dead Giveaways (Always Eliminate)
* **Overused AI Vocabulary (Era-Mapped):**
  * *2023–Mid 2024 (GPT-4 Era):* *delve, delve into* (dropped sharply post-2024), *tapestry, intricate, pivotal, multifaceted, foster, cultivate, harness, underscore, elevate, illuminate, intertwine, testament, realm, bolstered, enduring, vibrant*.
  * *Mid 2024–Mid 2025 (GPT-4o Era):* *align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant*.
  * *Mid 2025–2026 (GPT-5 & Grok Era):* *emphasizing, enhance, highlighting, showcasing*, coupled with Grok's pseudo-scientific tell words: *causal, empirical, correlate, underscore*.
* **Significance Inflation:** *stands as a testament to, pivotal moment, evolving landscape, indelible mark, beacon of, cornerstone of modern, watershed moment, deep dive*.
* **Promotional Buzzwords:** *groundbreaking, revolutionary, cutting-edge, paramount, nestled, breathtaking, vibrant, transformative, boasts a, renowned, rich (figurative)*.
* **Vague Connection / Association:** Replacing direct institutional or causal roles with nebulous affiliation: *in connection with, in connection to, associated with, connected with/to* (e.g., writing "He was associated with leadership of X" instead of "He served as CEO of X").
* **Canned Notability & Attribution Tropes:** Excessive metadata puffery: *independent coverage, national media outlets, trade publications, cited/featured/profiled in, written by a leading expert, maintains an active social media / digital presence*.
* **Chatbot Artifacts:** *Certainly!, Of course!, In this paper, we explore..., I hope this analysis provides...*.
* **Knowledge-Cutoff Disclaimers:** *As of my last training update, While empirical literature is limited, Based on available records, As of [date]*.
* **Sycophantic Servility:** Unearned praise of prior literature or excessive agreement with arbitrary assumptions.
* **Generic Canned Conclusions:** *The future looks bright, Exciting avenues lie ahead, Represents a major step in the right direction, Only time will tell*.

### Tier 2 — Reliable Structural Tells (Strict Eradication)
* **Copula Avoidance:** Replacing simple verbs (*is, are, constitutes, equals, has*) with decorative proxies: *serves as, stands as, represents, features, boasts, marks, operates as, functions as, refers to*.
* **Superficial `-ing` Participle Tails:** Appending vague participial clauses to paragraph ends (*highlighting the importance of, underscoring the need for, reflecting the complexity of, contributing to a broader understanding, ensuring, cultivating*).
* **Negative Parallelisms & Strawman Pivots (All 3 Variants):**
  * *Variant A (Not just X, but also Y):* "Not only X, but also Y; It is not just about X, it's about Y."
  * *Variant B (Not X, but Y):* "The problem is not X, it is Y; no X, no Y, just Z."
  * *Variant C (Y rather than X):* "prioritizing empirical consolidation rather than ideological purity" (prominent in Grok and newer LLMs to simulate synthetic nuance).
* **Formulaic "X and Y" Headings:** Canned structural sections like *"Awards and recognition"*, *"Challenges and Future Prospects"*, *"Legacy and Impact"*.
* **Elegant Variation (Synonym Cycling):** Switching terms arbitrarily across sentences (e.g., *estimator* $\to$ *formulation* $\to$ *computational engine* $\to$ *mathematical device*). Maintain canonical disciplinary terms consistently.
* **Filler Phrasing:** *In order to, At this point in time, Due to the fact that, For the purpose of*.
* **Persuasive Authority Tropes:** *At its core, The real question is, Fundamentally, In reality, It is clear that*.
* **Signposting Openers:** *Let us examine, Having established X, we now turn to Y, As mentioned above*.

### Tier 3 — Rhetorical & Symmetry Tells (Audit & Flatten)
* **Compulsive Rule-of-Three:** AI invents exactly three reasons, three pillars, or three implications. Real research exhibits asymmetric empirical evidence.
* **False Ranges:** Creating non-scalar ranges (*"ranging from cellular biology to quantum computing"*).
* **Fragmented Headings:** Section headings immediately followed by a redundant one-line summary sentence.
* **Unanchored Hedging:** Stacking speculative adverbs (*arguably, potentially, seemingly, tends to suggest*). Ground uncertainty in concrete confidence bounds or empirical conditions.

### Tier 4 — Stylistic Normalization & Counter-Heuristics
* **Straight Quotation Normalization:** Use straight ASCII quotes (`"` and `'`).
* **Title Case in Headings:** Follow target institution/journal capitalization style consistently.
* **Avoid False Positive Alarms (Ineffective Tells):** Do NOT flag text as AI merely because it has:
  * *Grammatical perfection:* Competent human scholars write with high grammatical accuracy.
  * *Disciplinary formality:* Legitimate academic jargon and complex sentences are expected in scholarly research; only the specific overrepresented token set constitutes an AI tell.
  * *Natural qualifiers:* Words like *very*, *perhaps*, or *tends to* are common in authentic human writing.

---

## 4. The Ten Humanization & Scholarly Levers

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ 1. Perplexity Injection        ──> Specific domain nouns, active verbs        │
│ 2. Burstiness Modulation       ──> Staccato-Legato cadence (SD > 10 words)    │
│ 3. Hedge Surgery               ──> Excise reflexive softening; state bounds   │
│ 4. Structural Flattening       ──> Convert bullet lists into flowing prose    │
│ 5. Specificity Anchoring       ──> N, p, rates, estimators, exact bounds      │
│ 6. Authentic Epistemic Stance  ──> Critical authority; grapple with trade-offs│
│ 7. Organic Transitions         ──> Causal & contrastive links (ban Moreover)  │
│ 8. Punctuation Normalization   ──> Zero em dashes, zero decorative colons     │
│ 9. RLHF Voice Strip            ──> Kill canned neutrality & textbook lectures │
│ 10. Voice Calibration Gate     ──> Match target journal or PG thesis guideline│
└───────────────────────────────────────────────────────────────────────────────┘
```

### Lever 1: Perplexity Injection (Word-Level)
Eliminate predictable, top-token vocabulary. Replace canonical AI verbs and nouns with precise, discipline-specific terminology:
* Delete: *delve, leverage, utilize, robust, comprehensive, streamline, foster, facilitate, pivotal, nuanced, notable, enduring, garner, multifaceted, realm, tapestry, testament, beacon, cornerstone*.
* Maintain domain precision: If writing in agricultural statistics, use *intra-class correlation, design effects, Neyman-orthogonal scores, Horvitz-Thompson baseline, split-plot layout*.

### Lever 2: Burstiness Modulation (Sentence-Level)
Enforce significant metric variance across sentence lengths. The target standard deviation of sentence word counts must exceed 10 words:
* **Staccato-Legato Blueprint:** Pair a punchy, decisive assertion (4 to 8 words) with an expansive, multi-clause periodic sentence (35 to 50+ words).
* **Mid-Band Floor:** Fewer than 45% of sentences may sit in the default 12-to-18-word band.

### Lever 3: Hedge Surgery
Audit and excise unnecessary softening:
* Strip: *it is important to note that, it is worth mentioning that, generally speaking, in many cases, it can be argued, tends to, can often lead to*.
* Replace with direct assertions. If genuine scientific uncertainty exists, frame it with concrete empirical conditions or confidence intervals.

### Lever 4: Structural Flattening
Dismantle rigid AI essay templates:
* Eliminate the "Three-Point Rule": Real research has asymmetric evidence; do not manufacture triads.
* Eliminate micro-recap endings: Never end a paragraph with a generic one-sentence summary of what was just explained.
* Eliminate boilerplate conclusion openers: Never use *In conclusion, To summarize, Overall, Ultimately*.

### Lever 5: Specificity & Methodological Anchoring
Ground every theoretical, empirical, or experimental claim in concrete specifics:
* State exact sample sizes ($N$), specific convergence rates ($o_p(n^{-1/2})$), exact degrees of freedom, named software packages with algorithm versions, GPS coordinates, or precise operational parameters.

### Lever 6: Authentic Epistemic Stance
Speak with the authoritative, critical stance of an active researcher in the field. Avoid the cheerful, eager tone of an AI assistant. Grapple directly with trade-offs, methodological bottlenecks, finite-sample breakdowns, and conflicting empirical evidence.

### Lever 7: Organic Transitions
Strip mechanical discourse connectors:
* Completely ban *Furthermore, Moreover, Additionally, In addition, In conclusion, As previously stated*.
* Connect paragraphs through substantive subject links, causal prepositions (*Consequently, Because of this*), or contrastive empirical statements (*In contrast, Earlier formulations overlooked...*).

### Lever 8: Punctuation Normalization
* Straight quotes and apostrophes only.
* Zero em dashes (`—`). Use commas, parentheses, or separate sentences.
* Zero mid-sentence colons.
* Semicolons used strictly according to standard academic conventions.

### Lever 9: RLHF Voice Strip
Strip the "helpful assistant" conditioning:
* No balanced neutrality where one side is scientifically unsupported. Take a definitive scholarly position based on empirical evidence.
* Never lecture the reader on basic definitions that an expert in the field already knows.

### Lever 10: Voice Calibration Gate
Calibrate the prose against the authentic voice of the target discipline, faculty guidelines, and target venue.

---

## 5. Anti-Plagiarism Protocol (< 4% Similarity Index)

To guarantee zero patchwriting flags and maintain similarity below 4% on Turnitin and iThenticate:

1. **Atomic Fact Extraction:** Extract only numerical findings, mathematical formulas, and empirical variables into atomic notes. Never copy sentence structures.
2. **Multi-Source Weaving (The 3:1 Rule):** Every substantive paragraph must synthesize at least two to three distinct citations, contrasting their methodologies, cohorts, or mathematical conclusions.
3. **Continuous Word Match Cap:** Never allow more than 4 consecutive words to match an indexed source, except for recognized proper nouns or mathematical terms.
4. **Structural Inversion:** Invert the narrative sequence of the source. Open with the conceptual boundary, empirical bottleneck, or methodological divergence rather than the chronological literature history.

---

## 6. Citation Discipline & Two-Stage Contradiction Resolution

### 6.1 Citation Discipline & Forensic Gate
* **Zero Phantom Citations:** Every single empirical, historical, or theoretical claim must resolve to a verified, authentic source with exact author-year or identifier tokens (`[Author, Year]` / `[PMID/DOI:loc]`).
* **DOI Resolution & Match Verification:** Mechanically verify that DOIs resolve to the exact article cited.
* **10-Year Recency Standard:** At least **70% of citations** must be published within the last 10 years (2016–2026 for 2026 thesis submissions).
* **Zero Broken Inception Links:** Reject external URLs that return 404s and lack historical web archive records.
* **Strip Model Tracking Queries:** Strip all LLM referral/campaign UTM parameters from web bibliography links.
* **Zero Orphan References:** Confirm that every entry declared in the reference list is explicitly cited inline in the manuscript body, and vice versa.

### 6.2 Two-Stage Contradiction Judgment
When synthesizing conflicting papers, do not average them into false consensus. Apply a two-stage evaluation:

1. **Stage 1 (Candidate Identification):** Group evidence rows by core concept and identify pairs with opposing conclusions.
2. **Stage 2 (Same-Question vs Scope-Variation Judgment):**
   * **Theoretical Conflict (`same_question`):** Both studies measure the exact same construct, in the same population, under identical operational conditions, yet obtain conflicting results. *Name the opposing camps and pinpoint the methodological divergence.*
   * **Scope Variation (`different_questions`):** The studies differ in population cohorts, treatment dosages, time horizons, or estimating assumptions. *Explain how both findings can hold simultaneously.*
   * **Uncertain (`uncertain`):** Flag ambiguous cases for explicit researcher inspection rather than guessing.

---

## 7. Mathematical & Methodological Precision Protocol

When presenting mathematical models, proofs, or empirical algorithms:
* **Explicit Identifying Assumptions:** Clearly state assumptions (e.g., unconfoundedness, overlap, sparsity, eigenvalue bounds, regularity conditions) and their failure modes.
* **Asymptotic Regimes:** Specify exact asymptotic scaling (e.g., fixed $p$ large $n$, high-dimensional $p/n \to c \in (0, \infty)$, or double-asymptotic limits).
* **Estimator Properties:** State convergence rates ($n^{-1/2}$), asymptotic normality, efficiency bounds (semiparametric efficiency), and robust variance estimators.
* **Finite-Sample Robustness:** Address finite-sample breakdown, coverage under heavy-tailed noise, and sensitivity to tuning parameters.

---

## 8. Postgraduate Thesis Chapter Protocols (JOSTUM / ASET Guidelines)

When drafting or revising postgraduate theses for Agriculture, Science, and Technology (ASET) disciplines (codifying **JOSTUM PG Thesis Guideline 4th Edition, Section B1**):

### 8.1 Technical Specifications & Page Layout
* **Paper & Print:** Standard A4 size, typed on one side only.
* **Margins:** Left (binding margin): **4.0 cm**; Right, Top, and Bottom: **2.5 cm**.
* **Typeface & Size:** Times New Roman, Size 12 or 14 (depending on bulkiness). Tables may be reduced to Size 10 for compactness.
* **Spacing:** Double line spacing throughout the body. Single spacing for Abstract, References, long Tables, and block quotes.
* **Pagination:**
  * **Preliminary Pages:** Lowercase Roman numerals (`i, ii, iii...`) centralized at the **bottom** of the page (Title page counts as page `i` but does not show a number).
  * **Main Text (Intro onwards):** Arabic numerals (`1, 2, 3...`) centralized at the **top** of the page.
* **Abstract:** Standalone informative style, single paragraph, single line spacing, strictly maximum **500 words**, covering objectives, methodology, quantitative key findings, conclusion, and recommendations.

### 8.2 Chapter 1.0: Introduction
* **Purpose:** Provide the backdrop, subject, purpose, and operational scope of the investigation.
* **Core Subsections:**
  * 1.1 Background of the Study
  * 1.2 Statement of the Problem & Justification
  * 1.3 Aim and Objectives (Overarching broad aim + numbered specific operational objectives)
  * 1.4 Research Questions / Hypotheses
  * 1.5 Significance & Scope of the Study
* **Length Constraint:** Strictly capped at **three (3) pages** double spaced. Dense, high-velocity prose; zero introductory fluff.

### 8.3 Chapter 2.0: Literature Review
* **Content:** Summarize professional knowledge, theoretical foundations, and prior empirical findings.
* **Thematic Organization:** Group literature thematically around the specific objectives stated in Section 1.3.
* **Contradiction Analysis:** Incorporate conflicting opinions, methodological variations, and competing hypotheses.
* **Recency Rule:** At least **70% of references must be published within the last 10 years**.
* **Citation Sync:** 100% bidirectional agreement between inline citations and the reference list.

### 8.4 Chapter 3.0: Materials and Methods
* **Replication Precision:** Describe materials, equipment, biological sources, environmental conditions, precautions, and analytical protocols with sufficient detail to allow complete independent verification by other researchers.
* **Research Location & Coordinates:** You must indicate the place/location of the research. For field sampling, farm trials, or ecological/environmental surveys, **maps and GPS coordinates (latitude, longitude, elevation) are mandatory**.
* **Experimental Design:** Explicitly declare experimental layouts (RCBD, CRD, Split-Plot, Multi-stage Stratified Cluster Sampling), replication factors, treatment levels, and randomization schemes.
* **Statistical Analysis:** Detail statistical models, mathematical formulations, test thresholds ($\alpha = 0.05, 0.01$), and exact software packages used (including software version numbers, packages/libraries, and random seeds).

### 8.5 Chapter 4.0: Results
* **Prose-First Presentation Rule:** Data and observations must be presented in **prose (text) form first**. The narrative articulates quantitative trends, percentage changes, statistical significance, and variance before directing the reader to any visual.
* **Visual Placement on Separate Pages:** Tables, Figures, and Plates must be arranged sequentially on **separate pages** immediately after the prose explanations for that section. Never embed tables mid-paragraph.
* **Anti-Duplication:** Do not replicate identical values across text, tables, and figures. The text interprets; the visuals document.
* **Captions:** Table captions at the top; Figure and Plate captions at the bottom.

### 8.6 Chapter 5.0: Discussion
* **Analysis & Synthesis:** Review and analyze the results in direct relation to published information and initial hypotheses.
* **Deductive & Inductive Logic:** Use rigorous logical arguments to highlight strong points, weak points, and novel discoveries.
* **Mechanisms:** Provide biological, chemical, statistical, or agronomic mechanisms explaining *why* patterns occurred.
* **Taxonomic Rigor (Binomial Nomenclature):** Strictly adhere to the binomial system for scientific names (e.g., *Meloidogyne incognita*, *Zea mays* L.). Generic name capitalized, species in lowercase, always italicized.
* **Limitations:** Objective discussion of experimental constraints and boundary conditions.

### 8.7 Chapter 6.0: Conclusion and Recommendations
Strict tripartite subdivision:
* **6.1 Conclusion:** Main inferences drawn from factual evidence, guided directly and systematically by specific objectives. No new data or speculation.
* **6.2 Recommendation(s):** Opinions or suggestions derived **strictly from the results** of the study. Generic recommendations are prohibited.
* **6.3 Contribution to Knowledge / Developmental Challenge Addressed:** Explicit, itemized declaration of original additions to scientific knowledge and practical solutions to societal/developmental challenges.

### 8.8 References & Ph.D. Publication Mandate
* **Referencing Style:** Harvard Style (Name and Year system).
* **Ph.D. Mandatory Requirement:** Evidence of at least one (1) publication in an international, peer-reviewed, high-impact journal attached as an Appendix.

---

## 9. Top-Tier Peer Referee & Thesis Examiner Pre-Flight Checklist

Before finalizing any academic draft or thesis chapter, execute this verification audit:

```markdown
[ ] Zero mid-sentence bolding: Search draft for "**" inside body paragraphs.
[ ] Zero em dashes: Search draft for "—" and "--". Count must be exactly 0.
[ ] Zero ASCII boxes: Confirm no Unicode/ASCII framing characters exist in prose.
[ ] Zero bullet-point essays: Confirm analytical arguments flow as connected prose paragraphs.
[ ] Zero banned AI words: Confirm absence of "delve", "tapestry", "testament", "pivotal", "furthermore", "moreover", "showcasing", "underscoring".
[ ] Zero thematic breaks: Confirm no horizontal rules ("---" or "----") exist between prose sections.
[ ] Zero empty headings: Verify no heading immediately precedes another heading without intervening narrative.
[ ] Zero negative parallelisms: Search draft for "not only... but", "not X, but Y", "Y rather than X", and tailing negations.
[ ] Zero vague associations: Replace "associated with" or "in connection with" with concrete institutional or causal roles.
[ ] Zero placeholder text: Confirm absence of "[Name]", "[Topic]", "202X-xx-xx", "PASTE_URL_HERE".
[ ] Zero leaked machine tokens: Confirm absence of "oaicite", "turn0search", "[cite: X]", "[span_X]", "【†】", ":::writing".
[ ] Burstiness verified: Confirm standard deviation of sentence lengths > 10 words, with both punchy assertions (<= 8 words) and periodic sentences (>= 35 words).
[ ] Citation authenticity & DOI match: Confirm 100% of cited works correspond to real literature.
[ ] Mechanical Crossref Reference Verification: Verify citations via fasttrack-literature:verify_reference.
[ ] Harvard Reference Recency Gate: Confirm >= 70% of cited works are within the last 10 years (2016–2026).
[ ] Zero orphan citations: Confirm 100% bidirectional match between inline citations and the reference list.
[ ] Multi-source synthesis (3:1 rule): Confirm paragraphs synthesize multiple independent studies rather than summarizing single papers in sequence.
[ ] Plagiarism compliance: Confirm no 4+ consecutive word sequences match external source phrasing (< 4% similarity).
[ ] Thesis Chapter 1.0 Page Limit: Confirm Introduction does not exceed 3 pages double-spaced.
[ ] Thesis Gap Non-Saturation: Confirm candidate problem is non-saturated via fasttrack-literature:check_gap_saturation.
[ ] Thesis Objectives Mapping: Confirm every specific objective in 1.3 maps 1-to-1 to Results (4.0), Discussion (5.0), and Conclusion (6.1).
[ ] Thesis GPS & Maps Grounding: Confirm field/environmental sampling includes exact GPS coordinates (Lat, Long, Elevation) and site maps in 3.1.
[ ] Thesis Software Environment: Confirm exact statistical software versions and computational packages are declared in 3.5.
[ ] Thesis Prose-First Results: Confirm all data and observations are fully narrated in prose before referencing visuals.
[ ] Thesis Visual Placement: Confirm Tables, Figures, and Plates are arranged on separate pages immediately after prose narratives.
[ ] Thesis Binomial Nomenclature: Confirm all scientific names are in italicized binomial format (*Genus species*).
[ ] Thesis Chapter 6 Structure: Confirm strict division into 6.1 (Conclusion), 6.2 (Recommendation(s)), and 6.3 (Contribution to Knowledge / Developmental Challenges Addressed).
[ ] Thesis Abstract Word Cap: Confirm informative abstract is a single paragraph, single spaced, under 500 words, containing quantitative key findings.
[ ] Thesis Formatting & Margins: Confirm A4 size, Left margin 4.0 cm, Right/Top/Bottom 2.5 cm, Times New Roman 12/14, double spacing throughout body.
[ ] Thesis Pagination: Confirm Roman numerals centralized at bottom for preliminaries; Arabic numerals centralized at top for main text.
```

---

## 10. Autonomous Tool Orchestration & Multi-Connector Pipeline

The writer operates as an autonomous research engine, coordinating external connectors and tools across five distinct phases:

### Phase 1: Live Discovery & Literature Ingestion
* **`academic-mcp:paper_search`**: Multi-platform search across CrossRef, Semantic Scholar, arXiv, and PubMed. Use to locate papers within specific publication date windows (`year: "2016-2026"`).
* **`fasttrack-literature:search_papers`**: Queries OpenAlex for high-velocity discovery of 250M+ papers with citation metrics and open access flags.
* **`consensus:search`**: Queries evidence distributions across scientific literature, extracting consensus percentages, sample size indicators, and methodological tags.
* **`search_web`**: Real-time retrieval of the latest 2024–2026 preprints, official government statistical bulletins (e.g., NBS, FAO, USDA), and university guidelines.

### Phase 2: Deep Full-Text Reading & Atomic Extraction
* **`academic-mcp:paper_read`**: Directly reads, parses, and extracts clean markdown/text and tabular data from academic PDF articles (arXiv, PubMed, bioRxiv, CrossRef, Semantic Scholar). Extracts exact sample sizes, estimators, and empirical numbers into atomic notes.
* **`read_url_content`**: Fetches HTML web pages from paper landing URLs or appendices and converts them to markdown.
* **`academic-doc-extractor-docx`**: Extracts structured tables, mathematical formulas, and text from existing Word `.docx` and PDF manuscripts.

### Phase 3: Debate Mapping & Gap Saturation
* **`fasttrack-literature:map_topic_debate`**: Maps co-citation clusters and shared reference ancestors to identify competing scholarly paradigms for two-stage contradiction resolution.
* **`fasttrack-literature:check_gap_saturation`**: Evaluates publication volume curves over time to ensure the proposed thesis gap is active and viable rather than saturated.
* **`fasttrack-literature:run_duplication_test`**: Verifies research originality and guards against unintentional duplication.

### Phase 4: Mechanical Bibliographic Verification Gate
* **`fasttrack-literature:verify_reference`**: Mechanically submits citation strings and DOIs to Crossref to verify actual registration, true author sequences, volume/issue numbers, and disambiguate online-first vs print dates. Enforces $\ge 70\%$ 10-year recency and eliminates phantom citations.

### Phase 5: Empirical Visualization & Document Packaging
* **`visualization:render_chart`**: Generates publication-grade empirical plots (Monte Carlo bias curves, MSE distributions, coverage rates) for Chapter 4.0 Results.
* **`academic-doc-extractor-docx`**: Compiles chapters into publication-grade Microsoft Word `.docx` documents featuring native OMML equations, A4 formatting, 4.0 cm left binding margins, and separate-page visual sequencing.

---

## 11. Positive Human Markers & Ineffective Indicators

### Authentic Human Scholarship Markers
Real academic prose contains natural syntactic patterns that LLMs routinely avoid in their quest for synthetic neutrality:
* **Direct Copula & Possession:** Unafraid of simple *is*, *are*, and *has* (*"The model has three parameters"*, not *"The model boasts/features three parameters"*).
* **Plain Scholarly Action Verbs:** Preferring *wrote* (vs *authored*), *used* (vs *utilized*), *moved* (vs *relocated*), *died* (vs *passed away*).
* **Asymmetric Evidence Allocation:** Spending three paragraphs on an anomalous boundary condition and one sentence on an obvious baseline, rather than formulaic three-point symmetry.
* **Definitive Historical / Empirical Claims:** Grounded confidence in proven benchmarks (*"was the first to calculate"*, *"remains the only closed-form solution"*).

### Avoid Ineffective Indicators (False Positive Traps)
* **Never flag scholarly rigor as AI:** Flawless grammar, technical Latinate terms (*heteroskedasticity*, *martingale*), and lengthy complex sentences are standard scholarly conventions, not LLM tells.
* **Avoid penalizing genuine transitions:** Logical deductive connectors (*Consequently*, *Therefore*) deployed in substantive mathematical or empirical progression are authentic and necessary.

---

## 12. Reference Guides & Deep-Dive Protocols

For detailed guidance on specific operational facets of this skill, refer to the following specialized documentation:
* [Autonomous Tool Orchestration & Multi-Connector Pipeline](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/tool_integration_pipeline.md): Comprehensive schemas, parameter references, and automated prompt chains for academic-mcp, fasttrack-literature, consensus, and visualization tools.
* [Postgraduate Thesis Writing Guide (ASET / JOSTUM 4th Edition)](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/pg_thesis_guide.md): Exhaustive chapter-by-chapter drafting blueprints, formatting rules, visual layout sequencing, and examiner audit heuristics.
* [Methodology Precision & Mathematical Rigor Guide](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/methodology_precision_guide.md): Statistical estimators, identifying assumptions, asymptotic rates, field sampling designs, GPS reporting, and software environment reproducibility.
* [Top-Tier Peer Referee & External Examiner Audit Protocol](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/academic_referee_audit.md): Adversarial review tests for theoretical soundness, baseline fairness, and postgraduate defense readiness.
* [Anti-Plagiarism Synthesis & Citation Discipline Protocol](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/anti_plagiarism_synthesis.md): 4-step structural inversion, 3:1 multi-source synthesis matrix, and two-stage contradiction resolution.
* [Banned Lexicon & 4-Tier AI Tells Catalog](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/banned_lexicon.md): Era-mapped banned vocabulary, copula avoidance replacements, and negative parallelism fixes.
* [Burstiness & Syntactic Modulation Blueprint](file:///C:/Users/USER/.gemini/config/skills/authentic-academic-writer/references/burstiness_syntax.md): Staccato-Legato cadence patterns, metric variance targets ($\sigma > 10$ words), and punctuation normalization.
