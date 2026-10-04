# Methodology Precision & Mathematical Rigor Guide

In elite academic prose (Econometrica, JASA, Biometrika, Annals of Statistics, NeurIPS, ICML), methodology sections must be mathematically self-contained, disambiguating estimators, identification assumptions, and asymptotic regimes.

---

## 1. The Methodological Specification Framework

For every proposed statistical estimator, machine learning algorithm, or theoretical model, specify all five structural layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Parameter of Interest       ──> θ_0 ∈ Θ (Causal or Structural Target)│
│ 2. Identifying Assumptions     ──> Unconfoundedness, Overlap, Sparsity │
│ 3. Score & Estimator Form      ──> Neyman Orthogonal Estimating Eq     │
│ 4. Asymptotic Distribution     ──> √n(θ̂ - θ_0) ⇝ N(0, V) & Rates       │
│ 5. Finite-Sample Robustness    ──> Subgroup coverage, breakdown points │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Methodological Protocols

### 2.1 Identifying Assumptions Specification
Always state assumptions formally:
* **Unconfoundedness / Exogeneity:** $Y(d) \perp D \mid X$.
* **Overlap / Positivity:** $\epsilon \le P(D=1 \mid X) \le 1 - \epsilon$ almost surely for some $\epsilon > 0$.
* **Sparsity & Regularity:** $\| \beta_0 \|_0 \le s$ with $s = o(\sqrt{n}/\log p)$.

### 2.2 Neyman Orthogonality & Double Machine Learning (SW-DML)
When using machine learning estimators for nuisance parameters ($\eta = (\mu, e)$):
* Use score functions $\psi(W; \theta, \eta)$ satisfying the Neyman orthogonality condition:
  $$\partial_{\eta} \mathbb{E}[\psi(W; \theta_0, \eta_0)] = 0$$
* Enforce $K$-fold cross-fitting (sample splitting) so that out-of-fold predictions prevent overfitting bias from inflating the target variance:
  $$\sqrt{n}(\hat{\theta} - \theta_0) = \frac{1}{\sqrt{n}} \sum_{i=1}^n \psi(W_i; \theta_0, \eta_0) + o_p(1) \rightsquigarrow \mathcal{N}(0, V)$$

### 2.3 Rate-of-Convergence Transparency
State nuisance estimation rate requirements explicitly (e.g., product of first-stage RMSEs $\|\hat{\mu} - \mu_0\|_2 \cdot \|\hat{e} - e_0\|_2 = o_p(n^{-1/2})$) rather than asserting generic "fast enough" convergence.

---

## 3. Banned Methodological Hand-Waving

| Hand-Waving Phrase (Banned) | Precise Methodological Replacement |
| :--- | :--- |
| *"Under standard regularity conditions..."* | *"Assuming compactness of parameter space $\Theta$, twice-differentiability of the objective function, and bounded fourth moments of the error term..."* |
| *"Machine learning was applied to control for confounders..."* | *"Random forests with 500 trees were fit out-of-fold ($K=5$) on baseline covariates $X$ to estimate nuisance conditional expectations $\mathbb{E}[Y \mid X]$ and propensity scores $\mathbb{E}[D \mid X]$."* |
| *"The results are statistically significant..."* | *"The estimated treatment effect is $\hat{\tau} = 3.42$ ($95\%\text{ CI: }[1.18, 5.66]$, $p = 0.003$, clustered at the school level)."* |
| *"The model scales well..."* | *"Computational complexity is $O(n \cdot p \log p)$, requiring $14.2$ seconds per 100,000 observations on a 16-core workstation."* |

---

## 4. Thesis & Experimental Science Precision (ASET Protocols)

When drafting Chapter 3.0 (Materials and Methods) for postgraduate science and technology theses:

### 4.1 Geographical & Field Grounding (Mandatory GPS Coordinates)
* Field sampling sites, ecological surveys, or agricultural trial plots must never be vaguely designated.
* Always report exact GPS coordinates (Latitude, Longitude in decimal degrees or DMS) and elevation (m above sea level) alongside referenced regional cartographic maps.
* *Standard:* *"Field trials were conducted at the Teaching and Research Farm, Joseph Sarwuan Tarka University, Makurdi, Nigeria (Latitude 7°45'N, Longitude 8°37'E, elevation 98 m above sea level)."*

### 4.2 Design of Experiments (DoE) & Sampling Architecture
* State the formal layout: Randomized Complete Block Design (RCBD), Completely Randomized Design (CRD), Split-Plot, or Multi-Stage Stratified Clustered Design.
* Declare block count, replication factors, plot dimensions (e.g., $4\text{ m} \times 3\text{ m}$), alley spacing, and exact randomization procedures.

### 4.3 Statistical Software Environment & Reproducibility
* Explicitly state the software suite, release version, and active computational libraries.
* Report random seeds for stochastic algorithms and simulation studies ($R=1,000$ Monte Carlo replicates).
* *Standard:* *"Statistical analyses were executed in R version 4.4.1 (R Core Team, 2024) utilizing the `survey` (v4.4-2) and `grf` (v2.3.1) packages. Neyman-orthogonal score calculations and cross-fitting were performed with fixed pseudo-random seed 202610."*

