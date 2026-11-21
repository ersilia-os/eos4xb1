# Fit folder: antihypertension-prediction (eos4xb1)

This folder holds the data, code and results needed to rebuild the model. It is stored with
[eosvc](https://github.com/ersilia-os/eosvc) in the **public** bucket; only this README is
tracked in git.

## Data processing

The six training sets in `data/` combine actives curated by the Centre for Drug Discovery at the University of Buea with property-matched ChEMBL decoys (`_eos3e6snegs`, about ten per active). No processing script was kept with them.

## Model building

`src/01_fit_oof.py` builds one LazyQSAR 3.9.3 classifier per task, in slow mode. For each task
it runs five-fold stratified out-of-fold (OOF) cross-validation (seed 42), so every compound
gets one prediction from a model that never saw it. It writes the OOF predictions and metrics to
`results/`, then trains the final model on all compounds into `model/checkpoints/<task>/`.
`src/02_performance.py` plots the OOF ROC curve and the OOF rank of actives and inactives per
task, and collects all metrics in `results/oof_metrics.json`.

```bash
cd src
OMP_NUM_THREADS=1 python 01_fit_oof.py        # or one task: python 01_fit_oof.py allmols_eos3e6snegs
python 02_performance.py
```

| Task | Output column | Training file | Compounds | Actives | OOF AUROC | Descriptors in final model |
|---|---|---|---|---|---|---|
| `allmols_eos3e6snegs` | `antihypertension_all_rank` | `data/allmols_eos3e6snegs.csv` | 8,320 | 749 | 0.981 | chemeleon, morgan, clamp |
| `sd_eos3e6snegs` | `antihypertension_sd_rank` | `data/sd_eos3e6snegs.csv` | 4,250 | 410 | 0.992 | chemeleon, morgan, clamp |
| `np_eos3e6snegs` | `antihypertension_np_rank` | `data/np_eos3e6snegs.csv` | 4,070 | 339 | 0.965 | chemeleon, rdkit, morgan |
| `ACE_eos3e6snegs` | `ace_inh_rank` | `data/ACE_eos3e6snegs.csv` | 2,722 | 245 | 0.985 | chemeleon, morgan |
| `CCBs_eos3e6snegs` | `cc_inh_rank` | `data/CCBs_eos3e6snegs.csv` | 1,754 | 159 | 0.971 | chemeleon, rdkit, clamp |
| `AT1RBs_eos3e6snegs` | `at1r_inh_rank` | `data/AT1RBs_eos3e6snegs.csv` | 1,683 | 153 | 0.996 | chemeleon, rdkit, clamp |
