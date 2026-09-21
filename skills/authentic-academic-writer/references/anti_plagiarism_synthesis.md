# Anti-Plagiarism Synthesis Protocol (< 4% Similarity Index)

Standard similarity detection engines (e.g., Turnitin, iThenticate, CrossRef Similarity Check) do not detect "ideas"; they identify **lexical n-gram string overlaps** (typically matching sequences of 6 or more consecutive words, or fuzzy matching with minor word substitutions).

The primary reason AI-generated literature reviews fail plagiarism checks is **patchwriting**: taking an existing abstract or paper section and swapping synonyms while leaving the underlying sentence structure and argument progression identical to the source.

---

## 1. The Mechanics of Plagiarism Flags

```
SOURCE SENTENCE:
"The rapid expansion of urban centers in developing nations has exacerbated ambient air pollution,
leading to a demonstrable rise in pediatric respiratory hospitalizations."

❌ PATCHWRITING (Flagged as Plagiarism & AI):
"The swift growth of city areas in developing countries has worsened surrounding air contamination,
resulting in a noticeable increase in child respiratory admissions."
[Result: 60-80% lexical and structural match in Turnitin; flagged as spun text/AI]

✅ CONCEPT EXTRACTION & STRUCTURAL INVERSION (< 4% Similarity):
"Pediatric admissions for pulmonary distress correlate directly with particulate exposure in rapidly industrializing cities, where infrastructural lags outpace emission regulations."
[Result: 0% match. Completely restructured causal direction, vocabulary, and conceptual hierarchy.]
```

---

## 2. The 4-Step Structural Inversion Method

Follow this workflow whenever incorporating external research, literature reviews, or theoretical frameworks:

### Step 1: Deconstruct Sources to Atomic Data Points
Read the target papers and record only the non-copyrightable factual cores as bullet points:
*   *Study:* Miller et al. (2022)
    *   Cohort: $N = 1,420$ acute myocardial infarction patients.
    *   Finding: Statin therapy initiation within 6 hours lowered 30-day mortality by 18% ($p = 0.012$).
    *   Limitation: Excluded patients with baseline renal impairment.

### Step 2: The Multi-Source Synthesis Matrix (The 3:1 Rule)
Never write a paragraph that summarizes only one paper. A scholarly paragraph should evaluate a **thematic claim** supported or disputed by multiple independent studies:

| Thematic Claim | Primary Evidence | Conflicting Evidence / Nuance | Methodological Divergence |
| :--- | :--- | :--- | :--- |
| Early statin intervention in AMI | Miller et al. (2022) (18% reduction, $N=1,420$) | Zhao & Kowalski (2023) (no benefit in elderly sub-cohort, $>80$ yrs) | Miller used IV administration; Zhao studied oral formulation. |

### Step 3: Invert the Narrative Sequence
Reconstruct the paragraph starting from the conceptual conflict or clinical boundary, rather than the chronological literature history:

> **Synthesized Output (Turnitin match = 0%):**
> "While early statin administration clearly improves 30-day survival following acute myocardial infarction, therapeutic benefits appear strictly route- and age-dependent. In large adult cohorts, immediate intravenous loading yields an 18% reduction in short-term mortality (Miller et al., 2022). Yet this protective advantage dissolves among octogenarian patients receiving oral regimens, where delayed gastrointestinal absorption blunts acute anti-inflammatory efficacy (Zhao & Kowalski, 2023). Route of delivery, rather than dosage alone, thus constitutes the critical determinant of early cardioprotection."

---

## 3. Strict Rules for Staying Below 4% Similarity

1. **Max Consecutive Matching Words:** Never exceed 4 consecutive identical words with any known published source, unless it is a standard domain-specific compound noun (e.g., *"polymerase chain reaction"*, *"gross domestic product"*).
2. **Direct Quotations Quota:**
   * Direct quotes should constitute **less than 1% of the total manuscript**.
   * In STEM and quantitative social sciences, direct quotes should be virtually 0%; ideas must be synthesized in the researcher's original framing.
   * In humanities, direct quotes must be enclosed in quotation marks with exact page numbers.
3. **Reference List Exclusion:** Ensure that when checking similarity reports, bibliography and small match filters (under 8 words) are excluded in institutional settings, as standard reference formatting naturally matches indexed bibliographies.
4. **No Template Hoarding:** Avoid using repetitive essay-template skeletons (e.g., standard 5-paragraph boilerplate introductions) that appear in hundreds of thousands of student essays online.
