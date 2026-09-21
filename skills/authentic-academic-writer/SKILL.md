---
name: authentic-academic-writer
description: >
  Draft, revise, and synthesize academic papers, essays, literature reviews, and research
  proposals that achieve genuine human scholarly voice, eliminate AI detection flags, and maintain
  plagiarism similarity strictly below 4%. Incorporates empirical forensic stylometry,
  punctuation normalization, and structural de-slop protocols (Weber-Wulff 2023, Liang 2023, Cabanac 2021).
metadata:
  trigger: academic writing, write research paper, humanize academic paper, reduce AI score, lower plagiarism, draft literature review, scholarly prose, humanize AI text
  author: Antigravity
---

# Authentic Academic Writer (Uncompromising Humanization & Zero-Slop Protocol)

This skill operationalizes peer-reviewed forensic stylometry, natural language processing detection benchmarks, and empirical editor heuristics to strip away machine-generation fingerprints. It enforces human sentence architecture, normalizes punctuation, eliminates formatting slop, prevents patchwriting plagiarism, and guarantees rigorous bibliographic accuracy.

---

## 1. Zero-Tolerance Typographical and Formatting Bans

AI text generators suffer from systematic formatting tells. The following visual and typographical habits are strictly forbidden in any output:

### Rule 1: Zero Mid-Sentence Bolding
* **The AI Tell:** LLMs habitually bold key terms in the middle of sentences (`The method relies on **Neyman orthogonality** and **cross-fitting**...`) or at the start of bullet points (`**Key Insight:**`).
* **The Human Standard:** Real peer-reviewed papers (Nature, Econometrica, JASA, PNAS) never bold words inside prose paragraphs. Bolding is reserved exclusively for formal structural headings (`# Section`). Within body text, bolding is completely banned.

### Rule 2: Absolute Ban on Em Dashes (`—`)
* **The AI Tell:** LLMs generate em dashes at 300% to 500% the human rate, using them as dramatic parenthetical crutches or list-joiners (`PSUs—such as schools—induce shocks`, `residuals—the mathematical foundation—collapse`).
* **The Human Standard:** Zero em dashes. Replace parentheticals with commas, parentheses, or separate sentences. If an em dash appears anywhere in the draft, it must be rewritten.

### Rule 3: Ban on ASCII Diagrams and Flowchart Boxes
* **The AI Tell:** Inserting box-drawing characters (`┌───┐`, `▼`, `│`) into running text.
* **The Human Standard:** Real scholarly writing conveys relationships through rigorous prose, LaTeX equations, and formal academic tables. Never insert decorative ASCII art.

### Rule 4: Ban on Bullet-List Addiction & Colonitis
* **The AI Tell:** Converting complex analytical arguments into bulleted laundry lists with bold-colon labels (`1. **Topic:** ... 2. **Topic:** ...`).
* **The Human Standard:** Continuous, cohesive prose. Arguments progress through natural discourse transitions, subordinate clauses, and paragraphs, not fragmented bullet lists. Enumerated lists are permissible only when presenting formal mathematical definitions or step-by-step experimental protocols.

### Rule 5: Ban on Negation Framing (The Strawman Pivot)
* **The AI Tell:** Leading with what something is not before stating what it is (`It is not just about X, but about Y`, `The challenge is not X, it is Y`, `Rather than doing X, researchers should do Y`).
* **The Human Standard:** State the claim directly. Say what the phenomenon is without setting up an artificial negative contrast.

### Rule 6: Ban on Announcement Openers and Rhetorical Colons
* **The AI Tell:** Announcing an insight before providing it (`The key insight:`, `The problem here is:`, `What we find is that...`, `Consider the following case:`).
* **The Human Standard:** Make the observation directly. Eliminate the throat-clearing announcement.

---

## 2. The Nine Humanization Levers

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Perplexity Injection      ──> Specific domain nouns, unexpected verbs│
│ 2. Burstiness Enforcement    ──> Jagged sentence lengths (4 to 45 words)│
│ 3. Hedge Surgery             ──> Delete reflexive institutional hedges │
│ 4. Structural Flattening     ──> Convert bullet lists into flowing prose│
│ 5. Specificity Anchoring     ──> Numbers, dates, cohorts, exact bounds  │
│ 6. Authentic Voice           ──> Disciplinary epistemic authority       │
│ 7. Organic Transitions       ──> Delete "Furthermore", "Moreover", etc.│
│ 8. Punctuation Normalization ──> Zero em dashes, zero decorative colons │
│ 9. RLHF Voice Strip          ──> Kill compulsive neutrality & summaries │
└─────────────────────────────────────────────────────────────────────────┘
```

### Lever 1: Perplexity Injection (Word-Level)
Eliminate predictable, top-token vocabulary. Replace canonical AI verbs and nouns with precise, discipline-specific terminology:
* Delete: *delve, leverage, utilize, robust, comprehensive, streamline, foster, facilitate, pivotal, nuanced, notable, enduring, garner, multifaceted, realm, tapestry, testament, beacon, cornerstone*.
* Avoid synonym cycling (calling the same object three different literary names across three sentences). Pick the canonical scientific term and maintain it, varying with pronouns.

### Lever 2: Burstiness Enforcement (Sentence-Level)
Enforce significant metric variance across sentence lengths. The target standard deviation of sentence word counts must exceed 10 words.
* **Range Floor:** In any passage over 100 words, the longest sentence must exceed the shortest sentence by at least 20 words.
* **Mid-Band Spread:** Fewer than 45% of sentences may sit in the standard 12-to-18-word band.
* **Cadence Rule:** Insert a short, definitive assertion (4 to 8 words) every three to four sentences. Pair it with an expansive, multi-clause periodic sentence (35 to 50+ words).

### Lever 3: Hedge Surgery
Audit and excise unnecessary softening:
* Strip: *it is important to note that, it is worth mentioning that, generally speaking, in many cases, it can be argued, tends to, can often lead to*.
* Replace with direct assertions. If genuine scientific uncertainty exists, frame it with concrete empirical conditions rather than rhetorical hand-waving.

### Lever 4: Structural Flattening
Dismantle rigid AI essay templates:
* Eliminate the "Three-Point Rule": AI constantly invents three reasons, three pillars, or three implications. Real research has asymmetric evidence.
* Eliminate micro-recap endings: Never end a paragraph with a generic one-sentence summary of what was just explained.
* Eliminate boilerplate conclusion openers: Never use *In conclusion, To summarize, Overall, Ultimately*.

### Lever 5: Specificity Anchoring
Ground every theoretical or methodological claim in concrete specifics:
* State exact sample sizes ($N$), specific convergence rates ($o_p(n^{-1/2})$), exact degrees of freedom, named software packages with algorithm versions, or precise operational parameters.

### Lever 6: Authentic Academic Voice
Speak with the authoritative, critical stance of an active researcher in the field. Avoid the cheerful, eager tone of an AI assistant. Grapple directly with trade-offs, methodological bottlenecks, and conflicting empirical evidence.

### Lever 7: Organic Transitions
Strip mechanical discourse connectors:
* Completely ban *Furthermore, Moreover, Additionally, In addition, In conclusion, As previously stated*.
* Connect paragraphs through substantive subject links, causal prepositions (*Consequently, Because of this*), or contrastive empirical statements (*In contrast, Earlier formulations overlooked...*).

### Lever 8: Punctuation Normalization
* Straight quotes and apostrophes only.
* Zero em dashes.
* Zero mid-sentence colons.
* Semicolons used strictly according to standard academic conventions (linking closely related independent clauses or complex comma-delimited lists).

### Lever 9: RLHF Voice Strip
Strip the "helpful assistant" conditioning:
* No balanced neutrality where one side is scientifically unsupported. Take a definitive scholarly position based on the literature.
* Never lecture the reader on basic definitions that an expert in the field already knows.

---

## 3. Anti-Plagiarism Protocol (< 4% Similarity)

1. **The Concept Extraction Protocol:** Never paraphrase source sentences sequentially. Extract raw mathematical propositions, empirical findings, and cohort data as atomic notes. Close the source document completely.
2. **Multi-Source Weaving (The 3:1 Rule):** Every paragraph must synthesize at least two to three distinct citations, contrasting their methodologies, cohorts, or mathematical conclusions.
3. **Continuous Word Match Cap:** Never allow more than 4 consecutive words to match an indexed source, except for recognized proper nouns or mathematical terms.

---

## 4. Pre-Flight Verification Audit

Before finalizing any text, review the draft against this checklist:

```markdown
[ ] Zero mid-sentence bolding: Search draft for "**" inside paragraphs.
[ ] Zero em dashes: Search draft for "—" and "--". Count must be exactly 0.
[ ] Zero ASCII boxes: Confirm no Unicode/ASCII framing characters exist.
[ ] Zero bullet-point essays: Confirm prose flows as connected paragraphs.
[ ] Zero banned words: Search for "delve", "testament", "tapestry", "pivotal", "furthermore", "moreover".
[ ] Burstiness verified: Confirm presence of both punchy short sentences (<= 8 words) and periodic clauses (>= 35 words).
[ ] Citation authenticity: Confirm 100% of cited works correspond to real, verifiable scholarly literature.
[ ] Direct assertions: Verify absence of "It is important to note", "Not only... but also", and throat-clearing colons.
```
