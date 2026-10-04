# Autonomous Tool Orchestration & Multi-Connector Pipeline

This guide specifies how `/authentic-academic-writer` programmatically invokes and coordinates external MCP servers, academic databases, online search tools, document extractors, and visualization engines to achieve an automated, end-to-end scholarly workflow.

```
┌────────────────────────────────────────────────────────────────────────┐
│                   SCHOLARLY WORKFLOW ENGINE PIPELINE                   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
[1. Live Discovery]        [2. Deep Full-Text Read]     [3. Debate & Gap Map]
- academic-mcp:paper_search - academic-mcp:paper_read   - fasttrack:map_topic_debate
- fasttrack:search_papers  - read_url_content           - fasttrack:check_gap_saturation
- consensus:search         - doc-extractor-docx         - fasttrack:run_duplication_test
- search_web (2024-2026)
    │                               │                               │
    └───────────────────────────────┼───────────────────────────────┘
                                    │
    ┌───────────────────────────────┴───────────────────────────────┐
    ▼                                                               ▼
[4. Mechanical Verification]                    [5. Visualization & Formatting]
- fasttrack:verify_reference                    - visualization:render_chart
- Crossref DOI resolution                       - academic-doc-extractor-docx
- 10-year recency audit (>= 70%)                - Native OMML equation formatting
- 100% bidirectional sync                       - JOSTUM ASET layout (4.0 cm margin)
```

---

## 1. Tool Directory & Connection Interface

### 1.1 Academic MCP Server (`academic-mcp`)
Invoked via `call_mcp_tool(ServerName="academic-mcp", ToolName=..., Arguments=...)`:
* **`paper_search`**: Searches across multiple academic engines simultaneously (`arxiv`, `pubmed`, `pmc`, `biorxiv`, `medrxiv`, `google_scholar`, `iacr`, `semantic`, `crossref`, `core`).
  ```json
  {
    "query_list": [
      {
        "searcher": "crossref",
        "query": "survey-weighted debiased machine learning complex sampling",
        "max_results": 10,
        "kwargs": {"filter": "from-pub-date:2020"}
      },
      {
        "searcher": "arxiv",
        "query": "Neyman orthogonality stratified cluster cross-fitting",
        "max_results": 5
      }
    ]
  }
  ```
* **`paper_read`**: Reads, parses, and extracts clean markdown/text and tabular data directly from open-access academic PDFs across arXiv, PubMed, PMC, bioRxiv, medRxiv, and CrossRef.
  ```json
  {
    "searcher": "arxiv",
    "paper_id": "2203.04567"
  }
  ```
  *(For Crossref DOIs: `{"searcher": "crossref", "paper_id": "10.1080/01621459.2023.2185523"}`)*

---

### 1.2 FastTrack Literature Server (`fasttrack-literature`)
Invoked via `call_mcp_tool(ServerName="fasttrack-literature", ToolName=..., Arguments=...)`:
* **`search_papers`**: High-velocity search across 250M+ scholarly records (OpenAlex), returning title, publication year, open access status, citation count, and landing URL.
  ```json
  {
    "query": "double machine learning survey weights stratified sampling",
    "limit": 10
  }
  ```
* **`get_paper`**: Fetches detailed metadata, complete abstract, author affiliations, and citation context for a given work ID or DOI.
  ```json
  {
    "paper_id": "https://openalex.org/W312849201"
  }
  ```
* **`verify_reference`**: Audits a citation string or DOI against Crossref to confirm whether it is officially registered. Settles online-first vs print publication dates, verifies author lists, volume, issue, and page numbers.
  ```json
  {
    "citation": "Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W. and Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal, 21(1), pp.C1-C68."
  }
  ```
* **`map_topic_debate`**: Returns recent papers clustering on a research topic within a specific window (e.g., 3 years) alongside their shared reference core (co-citation ancestors). Essential for executing the Two-Stage Contradiction Resolution Protocol.
  ```json
  {
    "topic": "debiased machine learning complex survey weights",
    "window_years": 3,
    "limit": 15
  }
  ```
* **`check_gap_saturation`**: Analyzes the publication trajectory over time for a candidate gap statement. Discovers whether a research problem is active, saturated, or open.
  ```json
  {
    "gap_statement": "integration of survey weights into Neyman orthogonal scores under two-phase cluster sampling",
    "window_years": 10
  }
  ```
* **`run_duplication_test`**: Assesses whether a proposed methodology or review duplicates existing published works.

---

### 1.3 Consensus Server (`consensus`)
Invoked via `call_mcp_tool(ServerName="consensus", ToolName="search", Arguments=...)`:
* **`search`**: Synthesizes scientific consensus across peer-reviewed publications. Returns consensus meter, study methodology classifications (e.g., RCT, observational, simulation), sample sizes, and empirical takeaway bullets.
  ```json
  {
    "query": "does ignoring sample weights in machine learning induce bias in clustered surveys",
    "limit": 10
  }
  ```

---

### 1.4 Live Web Search & Content Ingestion Tools
* **`search_web`**: Real-time web search for the latest 2024–2026 preprints, official government statistical releases (e.g., NBS Nigeria, US Census Bureau, FAO), and institutional guidelines.
  ```json
  {
    "query": "Survey weighted machine learning finite population correction 2024 2025 2026"
  }
  ```
* **`read_url_content`**: Directly fetches HTML/web content from paper URLs, publisher pages, or online appendices and converts it cleanly to markdown without browser overhead.
  ```json
  {
    "Url": "https://arxiv.org/abs/2402.12345"
  }
  ```

---

### 1.5 Document Packaging & Data Visualization Tools
* **`academic-doc-extractor-docx`**:
  * Extracts tables, equations, and text from incoming docx/pdf research files.
  * Formats final thesis chapters into native Word `.docx` documents adhering strictly to the **JOSTUM PG Thesis Guideline (ASET 4th Edition)**:
    - Left margin: 4.0 cm; Right, Top, Bottom: 2.5 cm.
    - Times New Roman 12/14 pt; Double line spacing.
    - Native, editable OMML mathematical equations.
    - Separate-page visual layout following prose sections.
* **`visualization` (`render_chart`)**:
  * Generates high-resolution empirical charts (Monte Carlo relative bias, MSE curves, coverage rate comparisons) to be converted into figures for Chapter 4.0.

---

## 2. End-to-End Orchestrated Thesis Workflow

### Workflow A: Drafting Chapter 1.0 (Introduction & Research Gap)
1. **Gap Validation:** Call `fasttrack-literature:check_gap_saturation` with the candidate problem statement to verify the gap is viable and active.
2. **Duplication Audit:** Call `fasttrack-literature:run_duplication_test` to confirm the proposed investigation does not duplicate an existing published thesis or article.
3. **Institutional Real-Time Grounding:** Call `search_web` to retrieve the latest socio-economic, agricultural, or demographic statistics (e.g., poverty indices, crop yield deficits, health survey frequencies) justifying the research.
4. **Drafting:** Synthesize Background, Statement of Problem, Broad Aim, Numbered Specific Objectives, and Scope into dense, high-velocity prose strictly capped at **3 pages**.

### Workflow B: Drafting Chapter 2.0 (Literature Review)
1. **Comprehensive Search:** Call `academic-mcp:paper_search` across `crossref`, `semantic`, and `arxiv` to retrieve 15–20 relevant papers published between 2016 and 2026.
2. **Consensus & Contradiction Mapping:**
   - Call `fasttrack-literature:map_topic_debate` on the core theoretical debate.
   - Call `consensus:search` to identify points of scientific agreement and empirical divergence.
3. **Deep Reading:** Call `academic-mcp:paper_read` or `read_url_content` on key papers to extract exact sample sizes ($N$), estimators, and empirical findings into atomic notes.
4. **Thematic Synthesis:** Structure the chapter thematically around the specific operational objectives from Chapter 1.0 using the **3:1 multi-source synthesis rule** and two-stage contradiction resolution.
5. **Recency Audit:** Verify that at least **70% of citations** fall within the last 10 years.

### Workflow C: Drafting Chapter 3.0 (Materials & Methods)
1. **GPS & Location Grounding:** Call `search_web` if verifying exact geographic coordinates, agro-ecological zones, or administrative boundaries for research stations (e.g., JOSTUM Teaching and Research Farm).
2. **Statistical Package Sync:** Call `search_web` or inspect project code to confirm active package versions (e.g., `R version 4.4.1`, `Python 3.11`, `scikit-learn 1.4`).
3. **Protocol Formulation:** Detail materials, experimental layout (RCBD, CRD, Split-Plot, Stratified Clustered), mathematical models, and estimation algorithms for complete independent verification.

### Workflow D: Drafting Chapter 4.0 (Results) & Visualization
1. **Data Ingestion:** Read input data tables or simulation CSVs (e.g., `SW_DML_Final_Results_Table.csv`).
2. **Prose-First Drafting:** Write complete narrative paragraphs explaining trends, percentage differences, relative bias, mean squared error, and confidence interval coverage.
3. **Visual Generation:**
   - Invoke `visualization:render_chart` for visual figures.
   - Format tables with clean booktabs styling and 10 pt font allowance.
4. **Separate-Page Sequencing:** Structure markdown/docx output so tables and figures appear sequentially on **separate pages** immediately following prose explanations.

### Workflow E: Drafting Chapter 5.0 (Discussion)
1. **Published Literature Cross-Examination:** Call `fasttrack-literature:search_papers` or `consensus:search` to retrieve comparative benchmarks for observed empirical metrics.
2. **Inductive/Deductive Synthesis:** Contrast observed findings against the hypotheses established in Chapter 1.0 and works cited in Chapter 2.0.
3. **Taxonomic & Nomenclature Check:** Ensure all biological species follow italicized binomial nomenclature (*Genus species*).

### Workflow F: Reference Verification (`cite-check`)
1. **Extract References:** Extract all inline citation anchors `(Author, Year)` and the complete bibliography.
2. **Mechanical Crossref Verification:** Run each entry through `fasttrack-literature:verify_reference`.
3. **Automated Audit Gate:**
   - Confirm 0 phantom citations.
   - Confirm 100% bidirectional sync (text $\leftrightarrow$ bibliography).
   - Confirm $\ge 70\%$ of references are within the last 10 years (2016–2026).
   - Strip any leaked LLM tracking parameters (`utm_source`, `referrer`).
