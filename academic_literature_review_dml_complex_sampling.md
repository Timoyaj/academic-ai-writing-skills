# Complex Survey Structures in Semiparametric Inference: A Methodological Review of Two-Phase Stratified Clustered Sampling within Debiased Machine Learning

## 1. Foundational Tensions in Modern Semiparametrics

Double or debiased machine learning provides a mathematically coherent framework for estimating low-dimensional causal parameters while using flexible, data-adaptive algorithms to control for high-dimensional confounding (Chernozhukov et al., 2018). The operating characteristics of this methodology rely on two foundational devices. First, Neyman-orthogonal score equations neutralize the first-order sensitivity of target parameter estimates to estimation errors in infinite-dimensional nuisance functions. Second, out-of-sample cross-fitting prevents empirical process overfitting, enabling valid asymptotic inference without requiring empirical risk minimizers to satisfy traditional Donsker class restrictions.

These theoretical guarantees presuppose independent and identically distributed observations. In applied econometrics, social policy research, and public health epidemiology, this baseline assumption is frequently untenable. 

Empirical investigations routinely gather evidence through complex multi-stage surveys. These probability designs introduce three distinct structural departures from the classic sampling framework: cluster correlations, unequal sampling weights derived from administrative stratification, and missingness induced by multi-phase measurement protocols (Särndal, Swensson, & Wretman, 1992; Lumley, 2010). 

When applied to such data, standard algorithmic pipelines fail. Unit-level cross-fitting ignores cluster boundaries, which permits latent cluster-specific random effects to contaminate training and testing partitions. Similarly, unweighted loss functions misalign nuisance estimators, pulling non-parametric predictions toward unrepresentative sample distributions. Finally, two-phase sampling generates an informative coarsening mechanism where expensive biological or behavioral variables are observed only for a stratified subsample of the initial master cohort (Breslow & Wellner, 2007). Resolving these contradictions requires unifying the superpopulation model-based framework of semiparametric inference with the design-based randomization framework of classical finite-population survey theory.

## 2. Orthogonal Moment Conditions under Stratified Two-Phase Selection

Let theta denote the finite-dimensional parameter of interest, such as the population average treatment effect, and let eta denote the vector of infinite-dimensional nuisance functions. In an unweighted superpopulation context, the target parameter solves an expectation equation evaluated at the true parameter values:

$$\mathbb{E}_P[\psi(W; \theta_0, \eta_0)] = 0$$

where the Gâteaux derivative with respect to eta vanishes at the parameter boundary. 

Under complex sampling, observation selection unfolds sequentially. Individual units are drawn into a master sample with inclusion probability $\pi_{1i}$, nested within geographic or institutional strata and cluster units. A second-phase selection mechanism subsequently draws a validation subsample with conditional probability $\pi_{2i|1}$, depending directly on covariates observed in the primary stage. 

The joint probability of observation is $\pi_i = \pi_{1i} \times \pi_{2i|1}$. This structure generates a design-weighted moment condition:

$$\mathbb{E}_p \left[ \frac{1}{N} \sum_{i \in S_2} \frac{1}{\pi_i} \psi(W_i; \theta_0, \eta_0) \right] = \frac{1}{N} \sum_{i=1}^N \psi(W_i; \theta_0, \eta_0)$$

which converges in probability to the superpopulation expectation under standard regularity conditions.

The presence of multi-phase selection alters the semiparametric efficiency bound. Following early semiparametric missing-data formulations (Robins, Rotnitzky, & Zhao, 1994; van der Laan & Robins, 2003), the optimal influence curve requires projecting the full-data score onto the observed data filtration. Letting $R_i$ serve as the binary indicator for second-phase selection, the augmented orthogonal score takes the following analytical form:

$$\psi^*(W_i; \theta_0, \eta_0) = \frac{R_i}{\pi_{2i|1}} \psi(W_i; \theta_0, \eta_0) - \left( \frac{R_i - \pi_{2i|1}}{\pi_{2i|1}} \right) \mathbb{E}[\psi(W_i; \theta_0, \eta_0) \mid W_{1i}]$$

This representation provides two distinct layers of protection. Small estimation errors in the surrogate expectation term $\mathbb{E}[\psi \mid W_{1i}]$ do not induce first-order bias on the primary target parameter. Furthermore, because second-phase selection probabilities are strictly determined by the sampling design rather than by unmeasured behavioral choices, inverse probability weighting remains design-unbiased even when the machine learning outcome regressions suffer from mild rate misspecification (Saegusa & Wellner, 2013).

Recent advances in non-parametric estimation bypass direct inverse probability weighting by computing the Riesz representer of the target functional directly (Chernozhukov, Newey, & Singh, 2022; Bjelac et al., 2026). When inclusion probabilities in sparse survey strata approach zero, empirical denominators destabilize. Formulating the estimation problem through regularized minimax loss functions allows the Riesz representer to absorb complex sampling weights naturally, preserving finite-sample stability without ad-hoc weight trimming.

## 3. Partitioning Mechanics: Cluster-Level and Nested Hierarchies

Standard cross-fitting protocols allocate individual units to validation folds uniformly at random. When data exhibit clustered dependence, this practice introduces severe empirical distortion.

Units within the same primary sampling unit share unobserved background conditions. In education policy evaluations, students within a given school share classroom infrastructure, teacher instruction quality, and community resources. If two students from the same school are split across training and evaluation folds, flexible machine learning models exploit school-level latent indicators to predict outcomes across the fold boundary. The resulting evaluation residuals are artificially deflated. This violates the conditional independence between nuisance estimation errors and evaluation scores, causing empirical standard error formulas to understate true sampling variability by substantial margins.

Valid inference demands that partitioning occur strictly at the primary sampling unit level (Chiang, Kato, Ma, & Sasaki, 2021). The collection of clusters must be partitioned into $K$ subsets, with each subset assigned entirely to a single fold. To maintain balance, cluster allocation must be stratified across administrative design strata. All individual records associated with a specific cluster remain bound to that cluster across every stage of training and testing.

Two-phase designs impose an additional hierarchical constraint. Phase-two validation subsamples cannot be partitioned independently of the phase-one master cohort. If fold assignments are generated on the phase-two sample alone, auxiliary prediction models trained on phase-one records will leak information into validation cohorts. The cross-fitting structure must therefore be fixed at the primary cluster level during the first phase of sampling, with validation units deterministically inheriting the fold assignment of their parent cluster.

## 4. Asymptotic Distribution and Multi-Stage Variance Estimation

When nuisance estimators achieve convergence rates faster than $n^{-1/4}$ under design-weighted norms, the empirical estimator satisfies an asymptotic linear expansion across independent clusters:

$$\sqrt{C} (\hat{\theta} - \theta_0) = J_0^{-1} \frac{1}{\sqrt{C}} \sum_{c=1}^C \xi_c + o_p(1)$$

where $C$ denotes the total count of primary sampling units, $J_0$ is the expected Jacobian of the orthogonal score, and $\xi_c$ represents the aggregated, design-weighted score contribution of cluster $c$.

Because primary sampling units are drawn independently within strata, asymptotic normality follows from central limit theorems for independent triangular arrays. The asymptotic variance estimator takes a stratified cluster-robust sandwich form:

$$\hat{\mathbb{V}} = \hat{J}^{-1} \hat{\Omega} (\hat{J}^{-1})^T$$

The empirical middle matrix accounts directly for stratum-level centered deviations:

$$\hat{\Omega} = \frac{1}{C} \sum_{h=1}^H \frac{C_h}{C_h - 1} \sum_{c=1}^{C_h} (u_{hc} - \bar{u}_h)(u_{hc} - \bar{u}_h)^T$$

where $u_{hc}$ denotes the sum of weighted scores within cluster $c$ of stratum $h$, and $\bar{u}_h$ is the corresponding stratum-level mean vector.

Standard econometric software often calculates confidence intervals assuming an infinite superpopulation, ignoring finite-population adjustments. When the sampling fraction at the primary cluster stage or within phase-two strata exceeds five percent of the target population, this omission produces overly conservative intervals. Total variance decomposes into two orthogonal components:

$$\text{Var}_{\text{total}} = \text{Var}_{\text{Phase 1}} + \text{Var}_{\text{Phase 2}}$$

Finite population correction factors must be applied across both stages to reflect the reduction in sampling uncertainty attributable to exhaustive sampling within fixed finite populations.

## 5. Methodological Pitfalls in Applied Literature

The integration of complex survey weights into machine learning workflows remains susceptible to systematic procedural errors.

A recurring error involves training machine learning algorithms on unweighted objective functions and reintroducing survey weights only during the final score-evaluation step. This practice rests on the mistaken assumption that flexible models automatically recover true conditional expectations without weighting. When sampling probabilities correlate with outcomes conditional on covariates, unweighted empirical loss minimizers converge to pseudo-true values that reflect the sample distribution rather than the target population. The resulting estimation error fails to satisfy the necessary rate conditions, transferring first-order bias directly into the target structural estimator. Sampling weights must enter the objective functions during algorithm training.

A second common vulnerability concerns cluster cardinality. Asymptotic normality in cluster-robust debiased machine learning requires the number of primary sampling units to approach infinity. In state-level or regional evaluations, researchers frequently analyze datasets containing fewer than thirty clusters. Under these small-sample regimes, empirical sandwich variance estimators exhibit substantial downward bias, and cross-fitting across five folds leaves too few clusters per training iteration to guarantee stable model convergence. In such environments, researchers must replace normal critical values with cluster wild bootstrap procedures adapted for estimating equations (MacKinnon, Nielsen, & Webb, 2023).

## 6. Open Methodological Frontiers

Three major theoretical challenges remain unresolved at this methodological intersection.

First, optimal second-phase sampling historically relies on Neyman allocation, which balances stratum-specific variance against unit acquisition costs. In high-dimensional settings, early phase-one machine learning predictions could theoretically be used to guide phase-two sample allocation adaptively. Establishing how such sequential, data-dependent sampling rules can be deployed without violating the downstream orthogonality of the moment conditions remains an open mathematical question.

Second, severe dimensionality bottlenecks frequently occur between sampling phases. In large epidemiological cohorts, administrative records often capture hundreds of potential confounders at baseline, while second-phase clinical assays are restricted to modest patient cohorts across a limited number of participating hospitals. Understanding the minimax convergence rates for Riesz representers when the ambient covariate dimension substantially exceeds the effective degrees of freedom of the second-phase sample represents a vital area for formal statistical inquiry.

Finally, modern survey methodology increasingly combines formal probability surveys with opportunistic non-probability samples, such as volunteer web panels or electronic health records (Seaman et al., 2025; Dagdoug & Haziza, 2026). Developing debiased machine learning architectures that treat unrepresentative non-probability cohorts as a biased first phase, calibrated against a rigorous probability validation sample, offers a promising path forward for empirical social science and population health research.

## References

Bjelac, M., et al. (2026). Automatic debiased machine learning and sensitivity analysis for sample selection models. arXiv preprint arXiv:2601.08922.

Breslow, N. E., and Wellner, J. A. (2007). Weighted likelihood for semiparametric models and two-phase stratified samples, with applications to Cox's proportional hazards model. Scandinavian Journal of Statistics, 34(1), 86-102.

Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo, E., Hansen, C., Newey, W., and Robins, J. (2018). Double/debiased machine learning for treatment and structural parameters. The Econometrics Journal, 21(1), C1-C68.

Chernozhukov, V., Newey, W. K., and Singh, R. (2022). Automatic debiased machine learning of causal and structural effects. Econometrica, 90(3), 967-1027.

Chiang, H. D., Kato, K., Ma, Y., and Sasaki, Y. (2021). Multiway cluster robust double/debiased machine learning. Journal of Business and Economic Statistics, 40(2), 497-512.

Dagdoug, M., and Haziza, D. (2026). Machine learning methods for finite population parameter estimation in survey sampling. arXiv preprint arXiv:2602.04112.

Lumley, T. (2010). Complex Surveys: A Guide to Analysis Using R. John Wiley and Sons.

MacKinnon, J. G., Nielsen, M. O., and Webb, M. D. (2023). Cluster-robust inference: A guide to empirical practice. Journal of Econometrics, 232(2), 272-299.

Robins, J. M., Rotnitzky, A., and Zhao, L. P. (1994). Estimation of regression coefficients when some regressors are not always observed. Journal of the American Statistical Association, 89(427), 846-866.

Saegusa, T., and Wellner, J. A. (2013). Weighted likelihood estimation under two-phase sampling. The Annals of Statistics, 41(1), 269-295.

Särndal, C.-E., Swensson, B., and Wretman, J. (1992). Model Assisted Survey Sampling. Springer-Verlag.

Seaman, S., et al. (2025). Debiased machine learning for combining probability and non-probability survey data. arXiv preprint arXiv:2502.11084.

van der Laan, M. J., and Robins, J. M. (2003). Unified Methods for Censored Longitudinal Data and Causality. Springer Science and Business Media.
