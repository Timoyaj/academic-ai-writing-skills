# Banned Lexicon, 4-Tier AI Tells, and Scholarly Alternatives

This catalog details the exact lexical, structural, and typographical habits statistically overrepresented in Large Language Model outputs. Every occurrence in a draft elevates detector confidence, triggers referee skepticism, and signals synthetic origin.

---

## 1. Zero-Tolerance Typographical and Structural Bans

| AI Typographical Habit | Why It Triggers Detectors & Referees | Human Academic Standard |
| :--- | :--- | :--- |
| **Mid-Sentence Bolding (`**word**`)** | LLMs use bolding to make text artificially scannable. | **Zero mid-sentence bolding.** Peer-reviewed journal prose never bolds random nouns or verbs. Bolding is reserved exclusively for formal section headings. |
| **Em Dashes (`—` or `--`)** | LLMs generate em dashes at 300%–500% the human baseline frequency for dramatic parentheticals. | **Zero em dashes.** Use commas, parentheses, or separate sentences. |
| **Thematic Breaks (`---` or `----`)** | LLMs insert horizontal rules between sections or paragraphs. | **Zero thematic divider lines.** Transition smoothly between sections using standard manuscript paragraphs. |
| **Empty Parent Headings** | LLMs generate headings that only contain sub-headings without text. | **Sequential hierarchy.** Every heading level must contain substantive introductory text before any sub-heading begins. |
| **Colonitis (`**Concept:** Explanation`)** | LLMs convert analytical prose into bold-colon bullet points. | **Continuous prose.** Embed concepts naturally into sentences without announcement colons. |
| **ASCII Art & Box Diagrams** | Inserting Unicode flowchart characters (`┌───┐`, `│`, `▼`). | **Standard prose and LaTeX.** Real papers use formal tables, mathematical equations, or dedicated vector figures. |
| **Curly Quote Residue (`“` / `”`)** | Default typographic quote characters from chat interfaces. | **Standard straight quotes (`"` / `'`).** |
| **Placeholder Residuals** | Leaving unpopulated tokens: `[Name]`, `202X-xx-xx`, `PASTE_URL_HERE`. | **100% concrete.** Every parameter and reference is fully specified. |
| **Model Metadata Leaks** | Leaked citations: `oaicite`, `turn0search`, `[span_1]`, `【†】`, `:::writing`. | **Zero synthetic residue.** Standard clean LaTeX citations only. |

---

## 2. Four-Tier Pattern Taxonomy (ROI-Ranked & Era-Aware)

### Tier 1 — Critical Dead Giveaways (Always Eliminate)

| Banned AI Word / Phrase | Human Scholarly Alternative | Contextual Example |
| :--- | :--- | :--- |
| **Delve / Delve into** *(GPT-4 staple; dropped sharply post-2024)* | *Examine, investigate, analyze, inspect, test* | Instead of "We delve into the sample," write: "We evaluated sample variance across three cohorts." |
| **Stands as a testament to** | *Evidences, demonstrates, illustrates, confirms* | Instead of "stands as a testament to model accuracy," write: "confirms theoretical convergence." |
| **Intricate / Rich tapestry** | *Complex network, composite structure, interdependent framework* | Instead of "an intricate tapestry of relationships," write: "a multi-tiered covariance structure." |
| **Pivotal role / Crucial role** | *Mediates, constrains, drives, regulates, determines* | Instead of "plays a pivotal role in estimation," write: "directly constrains finite-sample variance." |
| **Beacon** | *Benchmark, baseline, reference standard* | Instead of "a beacon for future work," write: "an empirical benchmark for subsequent trials." |
| **Realm** | *Domain, discipline, field, literature* | Instead of "in the realm of econometrics," write: "within empirical econometrics." |
| **Underscore / Underline** *(persistent in Grok & GPT-5)* | *Emphasize, reveal, indicate, accentuate* | Instead of "These results underscore the need," write: "These estimates indicate the need." |
| **Highlighting / Showcasing** *(Dominant in GPT-4o & GPT-5)* | Direct empirical finding, active verb | Replace superficial participial tails with concrete factual clauses. |
| **Foster / Cultivate** | *Produce, induce, generate, stimulate* | Instead of "fostered higher precision," write: "yielded narrower confidence intervals." |
| **Enhance / Bolstered** | *Improved, increased, narrowed, strengthened* | Instead of "bolstered by enhanced estimators," write: "strengthened by second-order bias corrections." |
| **Harness / Harnessing** | *Apply, utilize, mobilize, exploit* | Instead of "harnessing random forests," write: "fitting decision trees to high-dimensional covariates." |
| **Multifaceted** | *Bivariate, multi-component, heterogeneous* | Instead of "a multifaceted issue," write: "a problem constrained by cluster size and sample attrition." |
| **Cornerstone / Bedrock** | *Prerequisite, foundational premise, baseline assumption* | Instead of "The cornerstone of the theorem," write: "The foundational premise of the theorem." |
| **Groundbreaking / Revolutionary** | *Substantive, significant, first empirical demonstration* | Strip promotional hyperbole completely. |
| **In connection with / Associated with** | *Direct role or relationship (was director of, authored, caused)* | Instead of "was associated with the discovery," write: "conducted the initial assay." |
| **Canned Notability Buzz** | Factual citation context | Strip phrases like "independent coverage," "widely profiled in trade publications," "active digital presence." |

### Tier 2 — Reliable Structural Tells

* **Copula Avoidance:** Replacing simple verbs (*is, are, constitutes, equals, has*) with decorative proxies: *serves as, stands as, represents, features, boasts, marks, operates as, functions as, refers to*.
  * *AI:* "The loss function serves as the primary objective."
  * *Human:* "The loss function is the primary objective."
  * *AI:* "The algorithm boasts linear computational complexity."
  * *Human:* "The algorithm has linear computational complexity."
* **Superficial `-ing` Participle Tails:** Appending vague participial clauses to paragraph ends (*highlighting the importance of, underscoring the need for, reflecting the complexity of, contributing to a broader understanding, ensuring, cultivating*).
  * *AI:* "...thus reducing bias, highlighting the importance of robust estimation."
  * *Human:* "...thus reducing bias in the presence of heavy-tailed covariates."
* **Negative Parallelisms & Strawman Pivots (3 Variants):**
  * *Variant A (Not just X, but also Y):* "The contribution is not just asymptotic convergence, but also finite-sample stability." $\to$ State directly: "The estimator achieves asymptotic convergence and maintains finite-sample stability."
  * *Variant B (Not X, but Y):* "The problem is not lack of data, but unobserved confounding." $\to$ State directly: "Unobserved confounding biases the estimate regardless of sample size."
  * *Variant C (Y rather than X):* "prioritizing empirical consolidation rather than theoretical purity" (Grok tell). $\to$ State the methodological focus directly without setting up an artificial contrast.
* **Formulaic "X and Y" Headings:** Sections titled *"Awards and recognition"*, *"Challenges and Future Prospects"*, *"Legacy and Impact"*. Replace with substantive disciplinary section titles.
* **Elegant Variation (Synonym Cycling):** Arbitrarily cycling synonyms (*estimator* $\to$ *formulation* $\to$ *computational engine* $\to$ *mathematical device*). Maintain canonical disciplinary terms consistently.

### Tier 3 — Rhetorical & Symmetry Tells

* **Compulsive Rule-of-Three:** AI invents exactly three reasons, three pillars, or three implications. Real research exhibits asymmetric empirical evidence.
* **False Ranges:** Creating non-scalar ranges (*"ranging from cell biology to quantum physics"*).
* **Fragmented Headings:** Section headings immediately followed by a redundant one-line summary sentence.
* **Unanchored Hedging:** Stacking speculative adverbs (*arguably, potentially, seemingly, tends to suggest*). Ground uncertainty in concrete confidence bounds or empirical conditions.

---

## 3. Spanish-Language Academic Tells

When drafting or editing manuscripts in Spanish:

* **Inflated Connectors:** *en este sentido, cabe destacar, es importante señalar, a su vez, por otro lado, en definitiva, sin lugar a dudas, en consecuencia, dicho lo anterior*.
* **Formulaic Openers:** *En el mundo actual, En la era digital, En un panorama cada vez más, Hoy en día, En los últimos años*.
* **Promotional Inflation:** *innovador, revolucionario, disruptivo, paradigmático, de vanguardia, emblemático, imprescindible*.
* **Spanish Copula Avoidance:** *se erige como, se presenta como, se consolida como, representa una, constituye una, supone un*.
* **Generic Closers:** *En conclusión, En definitiva, El futuro es prometedor, Las posibilidades son infinitas*.
* **Academic Inflation:** *Es menester, Resulta imperativo, Cobra especial relevancia, Merece especial atención, No cabe duda de que*.

---

## 4. Tortured Phrases (Spinning Blacklist)

| Tortured Phrase (Reject) | Authentic Term (Mandatory) |
| :--- | :--- |
| *Counterfeit consciousness* | **Artificial intelligence** |
| *Straight relapse* | **Linear regression** |
| *Colossal information* | **Big data** |
| *Arbitrary access memory* | **Random access memory (RAM)** |
| *Blunder rate* | **Error rate** |
| *Supervision group* | **Control group** |
| *Nucleic corrosive* | **Nucleic acid** |
| *Thoracic cancer* | **Breast cancer** |
| *Neuronal organization* | **Neural network** |
