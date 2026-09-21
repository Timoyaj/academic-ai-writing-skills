# Flagging AI-Generated Content in Academic Writing: A Forensic, Methodological, and Ethical Framework

---

## Executive Summary

The proliferation of Large Language Models (LLMs) across scholarly publishing and higher education has precipitated an integrity crisis. Automated commercial detection tools (e.g., Turnitin, GPTZero, Copyleaks) are marketed as definitive arbiters, yet peer-reviewed evaluations consistently demonstrate that **statistical AI detectors cannot serve as standalone proof of academic dishonesty**. They suffer from unacceptably high false-positive rates, can be defeated by basic paraphrasing, and exhibit severe bias against non-native English speakers.

Reliable academic integrity enforcement requires moving away from reliance on single detection scores toward a **triangulated forensic framework**:
1. **Tier 1 (Irrefutable Artifacts):** Conversational prompt leakages, fabricated/hallucinated citations, impossible temporal claims, and document audit-trail telemetry.
2. **Tier 2 (Corroborative Stylometrics):** "Tortured phrases," hyper-elevated LLM lexical frequencies, uniform sentence cadence (low burstiness), semantic superficiality, and historical baseline divergence.
3. **Tier 3 (Probabilistic Signals):** Perplexity scans and detector percentages—used strictly as **investigative triage filters**, never as evidence.

This report synthesizes empirical computer science literature, publisher guidelines (COPE, ICMJE, Nature), and forensic linguistics to provide an actionable, legally defensible standard operating procedure for journal editors, peer reviewers, and academic integrity boards.

---

## 1. The Physics and Mathematics of AI Text Generation

Understanding how to identify synthetic text requires understanding the generative mechanics of autoregressive transformer models.

### 1.1 Perplexity and Burstiness
LLMs sample tokens based on conditional probability distributions derived from their training corpus. Two foundational metrics define the statistical profile of LLM output:

*   **Perplexity ($\text{PPL}$):** A measurement of how "surprised" a language model is by a sequence of words. Given a sequence $W = (w_1, w_2, \dots, w_N)$:
    $$\text{PPL}(W) = \exp\left( -\frac{1}{N} \sum_{i=1}^{N} \ln P(w_i \mid w_1, \dots, w_{i-1}) \right)$$
    Because LLMs naturally pick high-probability tokens to maintain fluency, **AI-generated text exhibits consistently low perplexity**. Human writing, characterized by idiosyncrasies, rhetorical surprises, and non-standard phrasing, exhibits higher, erratic perplexity.
*   **Burstiness:** The variation in sentence length, structure, and lexical surprise throughout a text.
    *   **Human Writing:** High burstiness. A scholar might write a 45-word periodic sentence explaining a complex causal mechanism, followed immediately by a 6-word punchy claim ("The data refute this entirely.").
    *   **LLM Writing:** Low burstiness. Sentences hover within a uniform window (18–26 words), with balanced clauses, repetitive coordinating conjunctions, and predictable rhythm.

### 1.2 Watermarking (Kirchenbauer et al. & SynthID)
Statistical watermarking partitions a model's vocabulary into "green" and "red" lists based on pseudo-random seeds computed from preceding tokens:
*   During generation, the model is biased toward selecting green-list tokens.
*   A statistical hypothesis test ($z$-score) can verify whether the proportion of green tokens significantly exceeds what would occur by chance.
*   **Limitation in Practice:** Watermarking requires model-level integration at the API inference stage. Open-weight models (Llama, Mistral, DeepSeek) strip watermarks entirely. Furthermore, watermarks are degraded by light paraphrasing, machine translation, or editing by a human.

---

## 2. Why Automated Detectors Fail as Sole Evidence

Empirical literature strongly cautions institutions against using automated detection scores as basis for disciplinary action.

### 2.1 The Weber-Wulff Benchmark (2023)
In a landmark study published in the *International Journal for Educational Integrity*, Weber-Wulff et al. tested 14 commercial and open-source detection tools (including Turnitin and PlagiarismCheck) against human, AI-generated, and mixed-modality academic texts:
*   **Accuracy Deficit:** None of the tested tools achieved an accuracy or reliability threshold acceptable for academic adjudication.
*   **Susceptibility to Obfuscation:** Simple paraphrasing (e.g., passing text through QuillBot or manual word replacement) lowered detection sensitivity dramatically.
*   **Conclusion:** The authors warned universities that using these tools to accuse students creates an unacceptably high probability of unjust penalties.

### 2.2 The Non-Native English Speaker (ESL) Discrimination Hazard
A study by Liang et al. (Stanford University, published in *Patterns*, 2023) tested leading AI detectors on standardized essays written by native U.S. students versus non-native English speakers taking the TOEFL exam:
*   Detectors accurately categorized native English writing.
*   However, **detectors misclassified more than 61% of TOEFL essays as AI-generated**, with some detectors flagging 98% of authentic non-native papers.
*   **The Mechanism:** Non-native academic writers naturally rely on a more constrained vocabulary, predictable transitional signposts, and standard syntactic structures—the exact statistical features that AI detectors associate with low perplexity.
*   **Legal / Compliance Consequence:** Disciplining a scholar based on detector percentages introduces substantial exposure to Title VI / national origin discrimination claims and legal appeals.

### 2.3 Sadasivan’s Impossibility Bound
Sadasivan et al. (2023, *Can AI-Generated Text be Reliably Detected?*) demonstrated mathematically that as language models approach the true human distribution of language, the Area Under the Receiver Operating Characteristic (AUROC) curve of any detector inevitably collapses. Paraphrase attacks fundamentally compromise detector bounds.

---

## 3. The 3-Tier Evidentiary Framework for Academic Flagging

To establish defensible grounds when evaluating suspicious manuscripts or student submissions, integrity committees and editorial boards must apply a tiered framework:

```
┌────────────────────────────────────────────────────────┐
│ TIER 1: Incontestable Forensic Artifacts ("Smoking Guns") │
│  • Verbatim prompt leakage ("Certainly, here is...")   │
│  • Hallucinated DOIs / Frankenstein citations           │
│  • Temporal & empirical impossibilities                │
│  • Document version-history telemetry (instant paste)  │
├────────────────────────────────────────────────────────┤
│ TIER 2: Corroborative Stylometrics (Probative Signs)   │
│  • "Tortured phrases" (Cabanac's PPS lexicon)          │
│  • Overrepresented LLM vocabulary ("delve", "realm")   │
│  • Low burstiness & syntactic flatness                 │
│  • Unbalanced epistemic hedging & empty summaries       │
│  • Severe divergence from author's verified baseline   │
├────────────────────────────────────────────────────────┤
│ TIER 3: Probabilistic / Statistical Screening Only     │
│  • Turnitin / GPTZero / Copyleaks percentages           │
│  • Raw PPL / Burstiness scans                          │
│  * NEVER ADMISSIBLE AS SOLE PROOF OF MISCONDUCT *      │
└────────────────────────────────────────────────────────┘
```

---

### Tier 1: Incontestable Forensic Artifacts (Hard Smoking Guns)

These items provide objective, incontrovertible evidence of unauthorized LLM generation:

#### 1. Chatbot Conversational Residue & Prompt Leakage
Occurs when the submitter copies raw output directly from an LLM interface:
*   *"As an AI language model, I do not have access to real-time data..."*
*   *"Certainly, here is an overview of..."* / *"Certainly, here is an updated literature review..."*
*   *"Regenerate response"* or copy-button artifacts left in the text body or footnotes.
*   *"In conclusion, while the prompt asked to explore..."*
*   *"As of my knowledge cutoff in [Date]..."*

#### 2. Hallucinated and "Frankenstein" Citations
LLMs assemble text probabilistically, not through indexed database lookups. This causes distinct bibliographic distortions:
*   **Non-Existent DOIs:** DOIs with valid prefixes (e.g., `10.1016/...`) that lead to 404 errors on `doi.org`.
*   **Frankenstein Citations:** Combining a real prominent researcher’s name, an actual target journal, and a completely fabricated article title that has never been indexed in PubMed, Scopus, CrossRef, or Web of Science.
*   **Fictitious Pagination and Volumes:** Citing an issue of a journal that does not exist or listing page numbers far beyond the actual page range of that issue.
*   **Citation Drift:** The cited source exists, but its actual subject matter is completely unrelated to the assertion it is cited to support (e.g., citing a pediatric cardiology study to support a claim about quantum computing algorithms).

#### 3. Temporal and Experimental Impossibilities
*   Describing experimental procedures performed on equipment that was not commercially available at the stated time, or claiming to analyze real-world datasets that did not exist prior to the model's knowledge cutoff.
*   Conflating historical chronology or quoting fictional passages from real historical figures.

#### 4. Document Telemetry and Version Control Audits
When Google Docs version history, Word tracked changes, or Overleaf/Git commit logs are examined:
*   **Authentic Process:** Incremental typing (30–80 words/minute), frequent cursor movements, deletions, typo corrections, backspaces, and natural editing pauses over hours/days.
*   **AI Direct Injection:** An entire 2,500-word section appearing in the document within a span of 12 seconds with zero typographical mistakes, zero character-level keystroke telemetry, and no prior drafting history.

---

### Tier 2: Corroborative Linguistic & Stylometric Indicators

Tier 2 signals do not provide immediate standalone proof, but when multiple indicators cluster within a single manuscript, they warrant formal investigation.

#### 1. "Tortured Phrases" (The Guillaume Cabanac Lexicon)
Pioneered by Dr. Guillaume Cabanac (creator of the *Problematic Paper Screener*), tortured phrases occur when text-spinning tools or prompt instructions attempt to evade plagiarism detectors by substituting established domain-specific scientific terms with bizarre synonyms:

| Authentic Scientific Term | "Tortured Phrase" (AI / Spinner) |
| :--- | :--- |
| **Artificial intelligence** | *Counterfeit consciousness* / *Man-made consciousness* |
| **Linear regression** | *Straight relapse* |
| **Random access memory (RAM)** | *Arbitrary access memory* |
| **Big data** | *Colossal information* / *Sizeable data* |
| **Breast cancer** | *Bosom malignancy* / *Thoracic cancer* |
| **Neural network** | *Neuronal organization* |
| **Nucleic acid** | *Nucleic corrosive* |
| **Error rate** | *Blunder rate* |
| **Control group** | *Supervision group* |

#### 2. LLM Vocabulary Clusters (Lexical Overrepresentation)
Corpus linguistics studies analyzing millions of post-2023 PubMed and arXiv preprints (e.g., Gray, 2024) have revealed a statistical explosion of specific vocabulary items:

*   **Verbs & Phrasal Patterns:** *delve, underscore, illuminate, cultivate, foster, encapsulate, harness, facilitate, mirror, champion*.
*   **Nouns & Tropes:** *tapestry, realm, testament (e.g., "stands as a testament to"), interplay, myriad, beacon, cornerstone, paradigm shift*.
*   **Adjectives:** *pivotal, intricate, profound, multifaceted, paramount, vital, compelling, indelible*.
*   **Clustered Transition Sequences:** Overuse of paired transitions (*Moreover... Furthermore... Additionally... In conclusion...*) at the head of every paragraph.

#### 3. Semantic Superficiality and Pseudo-Profundity
*   **High Lexical Density, Zero Empirical Specificity:** The text sounds authoritative and sophisticated, but lacks concrete operational data. For example: *"The chemical solution was appropriately heated under regulated conditions, ensuring optimal stability"* instead of *"The solution was maintained at 37.5 °C in an oil bath for 45 minutes"*.
*   **Compulsive Neutrality & Balanced Hedging:** LLMs trained with RLHF (Reinforcement Learning from Human Feedback) default to non-committal symmetry: *"While some argue X, others maintain Y. Both perspectives offer valuable insights, highlighting the need for a comprehensive and balanced approach."* In original scholarship, an author is expected to take a definitive epistemic stand supported by empirical analysis.

#### 4. Baseline Discrepancy (Stylometric Drift)
*   Comparing the submission to known authentic work by the same author (e.g., past unassisted exams, verified previous papers, oral interview demeanor).
*   Sudden, unexplained shifts in vocabulary register, syntactic complexity, or idiom usage that disappear when the author is asked to write or speak in person.

---

### Tier 3: Statistical & Computational Tools (Triage Only)

*   **Tools:** Turnitin AI Writing Indicator, GPTZero, Copyleaks, Crossref Similarity Check.
*   **Legitimate Role:** Serving as an initial **heuristic trigger** for a human editor or instructor to review the paper's references, data, and drafting history.
*   **Illegitimate Role:** Being cited in a formal academic misconduct allegation as proof of guilt.

---

## 4. Academic Publisher and Professional Society Policies

Major academic governing bodies have established clear normative frameworks regarding AI usage:

### 4.1 Committee on Publication Ethics (COPE)
1.  **Authorship Ineligibility:** AI tools (e.g., ChatGPT, Claude) cannot be listed as authors or co-authors. Authorship requires legal personhood, moral accountability, the ability to approve final proofs, and legal responsibility for scientific integrity and conflict of interest disclosures.
2.  **Author Accountability:** Human authors are 100% accountable for all content in their manuscript, including any inaccuracies, fabricated references, or plagiarized text introduced by AI.
3.  **Mandatory Disclosure:** Authors must disclose in the Methods or Acknowledgments section which AI tools were used and the specific scope of their application (e.g., language editing, code optimization, literature search).
4.  **Confidentiality in Peer Review:** Reviewers are strictly prohibited from uploading unpublished manuscripts into commercial or public AI systems. Doing so constitutes a direct breach of reviewer confidentiality and intellectual property rights.

### 4.2 International Committee of Medical Journal Editors (ICMJE) & Nature Portfolio
*   **ICMJE:** Requires explicit descriptions of AI usage in both the cover letter and the published paper.
*   **Nature Portfolio:** Rejects any image, photograph, or scientific illustration created using generative AI (due to unresolved copyright issues and lack of verifiable provenance), except for articles specifically about generative AI.

---

## 5. Standard Operating Procedure (SOP): Step-by-Step Institutional Investigation

When a manuscript or student assignment is flagged as potentially containing unauthorized AI text, institutions should follow this 5-step protocol to ensure procedural fairness and evidentiary rigor.

```
                  ┌──────────────────────────────┐
                  │ 1. Triaged Flag Received     │
                  │ (Detector Score or Reviewer) │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │ 2. Independent Citation Audit│
                  │ (Check 100% of DOIs & Papers)│
                  └──────────────┬───────────────┘
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
      [Fabrications Found]              [All Citations Real]
                │                                 │
                ▼                                 ▼
    Direct Tier 1 Misconduct            ┌──────────────────────────────┐
    (Charge: Falsification/Fab)          │ 3. Document Telemetry Audit  │
                                        │ (Version history / metadata) │
                                        └──────────────┬───────────────┘
                                                       │
                                                       ▼
                                        ┌──────────────────────────────┐
                                        │ 4. The Pedagogical Interview │
                                        │ (Viva Voce / Concept Probe)  │
                                        └──────────────┬───────────────┘
                                                       │
                                                       ▼
                                        ┌──────────────────────────────┐
                                        │ 5. Formal Adjudication       │
                                        │ & Proportional Sanction      │
                                        └──────────────────────────────┘
```

### Step 1: Triage and Screening
*   Do not contact the author based solely on a high detector score.
*   Examine the submission for high-risk text characteristics: generic conclusions, low burstiness, and repeated transition words.

### Step 2: The Citation and Verification Audit (High Yield)
*   Extract 5 to 10 random citations from the reference list.
*   Verify each reference against PubMed, CrossRef, Google Scholar, and the journal's official archives.
*   *If fabricated DOIs, imaginary article titles, or phantom co-authors are identified, the case shifts from an ambiguous "AI writing style" debate to clear-cut **falsification and fabrication of scholarly records** under standard academic integrity policies.*

### Step 3: Forensic Document Telemetry Inspection
*   Request the original `.docx` file or inspect the native cloud platform (Google Docs, Microsoft 365, Overleaf).
*   Inspect document properties (Author, Creation Date, Total Editing Time, Modification Count). A 15-page essay with a "Total Editing Time" of 3 minutes is a critical diagnostic marker.
*   Review change-history logs for the absence of iterative drafting.

### Step 4: The Inquiry Interview (Viva Voce / Oral Defense)
The most humane, conclusive, and pedagogically sound method to resolve suspected AI generation is an in-person or live video interview:
*   **Targeted Inquiries:** Ask the author to explain complex terminology used in the paper:
    *   *"In paragraph 3, you note that 'the heteroskedasticity was mitigated using a Bayesian shrinkage prior.' Could you walk me through how you implemented that prior?"*
    *   *"Can you explain the main thesis of Reference [12] and how it informed your conceptual model?"*
*   **Draft Reconstruction:** Ask the author to sketch the workflow, provide their original search queries, or open their lab notebook / statistical code scripts.
*   Authentic authors can immediately discuss their reasoning, challenges, and rejected ideas. Authors who used an LLM to ghostwrite the submission will struggle to explain core arguments, specialized vocabulary, and methodology.

### Step 5: Adjudication and Proportional Sanctions
*   Structure the accusation on verifiable evidence: citation fabrication, failure to supply source data/drafts, and inability to demonstrate basic subject mastery during the inquiry interview.
*   Apply sanctions proportional to the offense:
    *   *Minor / Unintentional (e.g., undeclared grammar assistance):* Educational correction, requirement to rewrite with transparent disclosure.
    *   *Severe (e.g., fully synthetic paper, fabricated citations, fraudulent data):* Course failure, manuscript rejection with notification to the author's institution, or formal academic probation.

---

## 6. Future-Proofing: Transitioning to Process-Oriented Integrity

Post-hoc detection of AI-generated text is an unstable long-term strategy. As LLMs become more integrated into search engines, word processors, and research workflows, policing the final output text becomes increasingly impractical. Academic institutions must adapt their processes:

1.  **Milestone-Based Assessment:** Evaluate the research process over time (annotated bibliographies $\rightarrow$ hypothesis pitch $\rightarrow$ data logs $\rightarrow$ rough draft $\rightarrow$ final draft) rather than grading only an isolated, high-stakes final artifact.
2.  **Oral Defenses and In-Class Synthesis:** Incorporate short viva voce interviews or in-class timed synthesis components into capstone and high-stakes courses.
3.  **Explicit Citation of AI Contributions:** Adopt a clear taxonomy (e.g., CRediT extensions for GenAI) where students and researchers specify the exact prompts, tools, and roles played by AI (e.g., *"ChatGPT-4 was used to refine the Python script for data extraction; all resulting code was manually reviewed and validated by the author"*).
4.  **Authentic Problem Formulations:** Design assignments that require localized, highly contemporary, or personal fieldwork that cannot be retrieved or generated from generalized LLM training data.

---

## 7. Key References & Empirical Literature

1.  **Weber-Wulff, D., et al. (2023).** "Testing of detection tools for AI-generated text." *International Journal for Educational Integrity*, 19(26). [DOI: 10.1007/s40979-023-00146-z]
2.  **Liang, W., et al. (2023).** "GPT detectors are biased against non-native English writers." *Patterns*, 4(7), 100779. [DOI: 10.1016/j.patter.2023.100779]
3.  **Sadasivan, V. S., et al. (2023).** "Can AI-Generated Text be Reliably Detected?" *arXiv preprint arXiv:2303.11156*.
4.  **Cabanac, G., Labbé, C., & Magazinov, A. (2021).** "Tortured phrases: A dubious footprint of illicit text spinning in scientific publications." *Bulletin of the American Society for Information Science and Technology*.
5.  **Kirchenbauer, J., et al. (2023).** "A watermark for large language models." *International Conference on Machine Learning (ICML)*.
6.  **Committee on Publication Ethics (COPE). (2023).** "Authorship and AI tools: COPE position statement." *publicationethics.org*.
7.  **International Committee of Medical Journal Editors (ICMJE). (2023).** "Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals."
