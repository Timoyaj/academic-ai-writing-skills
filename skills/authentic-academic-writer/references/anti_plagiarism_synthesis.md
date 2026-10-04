# Anti-Plagiarism Synthesis & Citation Discipline Protocol (< 4% Similarity Index)

Standard similarity detection engines (Turnitin, iThenticate, CrossRef Similarity Check) do not detect "ideas"; they identify **lexical n-gram string overlaps** (typically matching sequences of 6 or more consecutive words, or fuzzy matching with minor word substitutions).

The primary reason AI-generated literature reviews fail plagiarism checks is **patchwriting**: taking an existing abstract or paper section and swapping synonyms while leaving the underlying sentence structure and argument progression identical to the source.

---

## 1. The 4-Step Structural Inversion Method

Follow this workflow whenever incorporating external research, literature reviews, or theoretical frameworks:

### Step 1: Deconstruct Sources to Atomic Data Points
Read target papers and record only non-copyrightable factual cores as atomic notes:
* *Study:* Miller et al. (2022)
  * Cohort: $N = 1,420$ acute myocardial infarction patients.
  * Finding: Statin therapy initiation within 6 hours lowered 30-day mortality by 18% ($p = 0.012$).
  * Limitation: Excluded patients with baseline renal impairment.

### Step 2: Multi-Source Synthesis Matrix (The 3:1 Rule)
Never write a paragraph that summarizes only one paper. A scholarly paragraph must evaluate a **thematic claim** supported or disputed by multiple independent studies:

| Thematic Claim | Primary Evidence | Conflicting Evidence / Nuance | Methodological Divergence |
| :--- | :--- | :--- | :--- |
| Early statin intervention in AMI | Miller et al. (2022) (18% reduction, $N=1,420$) | Zhao & Kowalski (2023) (no benefit in elderly sub-cohort, $>80$ yrs) | Miller used IV administration; Zhao studied oral formulation. |

### Step 3: Invert Narrative Sequence
Reconstruct the paragraph starting from the conceptual conflict or empirical boundary, rather than the chronological literature history:

> **Synthesized Output (Turnitin match = 0%):**
> "While early statin administration clearly improves 30-day survival following acute myocardial infarction, therapeutic benefits appear strictly route- and age-dependent. In large adult cohorts, immediate intravenous loading yields an 18% reduction in short-term mortality (Miller et al., 2022). Yet this protective advantage dissolves among octogenarian patients receiving oral regimens, where delayed gastrointestinal absorption blunts acute anti-inflammatory efficacy (Zhao & Kowalski, 2023). Route of delivery, rather than dosage alone, thus constitutes the critical determinant of early cardioprotection."

---

## 2. Mechanical Citation Discipline Gate

1. **Zero Phantom Citations:** Every single empirical finding, coefficient, or historical fact must resolve to a verified, authentic bibliographic source. Never cite imaginary studies or extrapolate claims beyond what the cited paper proved.
2. **Citation Token Formatting:** Use standard inline citation anchors (`(Author, Year)` or `\cite{key}`) immediately following the empirical claim.
3. **Continuous Word Match Cap:** Never allow more than 4 consecutive identical words to match an indexed source, except for recognized proper nouns or mathematical terms.
4. **Direct Quotes Quota:** Keep direct quotations strictly below 1% of the total manuscript. Ideas and findings must be re-synthesized in original prose.

---

## 3. Two-Stage Contradiction Resolution Protocol

When synthesizing conflicting literature, do not average opposing results into a vague compromise. Distinguish between genuine conflict and scope divergence:

### Stage 1: Candidate Extraction
Identify pairs of papers studying the same phenomenon that report conflicting signs or effects.

### Stage 2: Same-Question vs. Scope-Variation Judgment

* **Theoretical Conflict (`same_question`):**
  * *Condition:* Both papers measure the exact same construct in the same population under comparable operational conditions.
  * *Resolution:* Name the competing theoretical camps directly and isolate the mathematical or estimation divergence.
* **Scope Variation (`different_questions`):**
  * *Condition:* The studies differ in population cohorts, sampling frames, covariate controls, or intervention durations.
  * *Resolution:* Explain how both empirical findings can hold simultaneously within their respective scopes.
* **Uncertain (`uncertain`):**
  * *Condition:* Methodological details in published papers are insufficient to resolve the divergence.
  * *Resolution:* Explicitly identify the empirical ambiguity as an open research gap.
