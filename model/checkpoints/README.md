# Model pretrained parameters

These models have been trained using the [LazyQSAR package](https://github.com/ersilia-os/lazy-qsar) v3.6.3, mode `slow`.
In `slow` mode LazyQSAR screens five descriptors (CDDD, Chemeleon, CLAMP, Morgan, RDKit) and keeps only those its
portfolio retains. CDDD was rejected for all six models; the rest vary per model, as shown below.

Upon 5-fold crossvalidation on train test splits (80-20%), we obtain the following performance:

| **Model** | **Data** | **Frac Actives (%)** | **Descriptors** | **AUROC ± STDev** |
|-----------|----------|----------------------|-----------------|-------------------|
| allmols   | 8320     | 9.0                  | chemeleon, clamp, morgan | 0.981 ± 0.006 |
| sd        | 4250     | 9.6                  | chemeleon, clamp, morgan | 0.990 ± 0.006 |
| np        | 4070     | 8.3                  | chemeleon, morgan, rdkit | 0.967 ± 0.009 |
| ACE       | 2722     | 9.0                  | chemeleon, morgan        | 0.986 ± 0.007 |
| CCBs      | 1754     | 9.1                  | chemeleon, clamp, rdkit  | 0.971 ± 0.011 |
| AT1RBs    | 1683     | 9.1                  | chemeleon                | 0.996 ± 0.003 |

Negatives are property-matched ChEMBL decoys at about ten per active, not measured inactives. Separating actives from
decoys is an easier task than separating them from true inactives, so these AUROC values should not be read as
prospective performance.

Predictions are reported as a **rank score** against the Ersilia reference library of 50K compounds: a score of 0.65
is the library's 99th percentile, so by construction 1% of drug-like chemical space scores above it.

Values are not comparable with v1. On 1000 reference molecules the Spearman correlation between v1 probabilities and
v2 ranks runs from 0.33 (AT1RBs) to 0.77 (np), so the two versions order compounds differently.
