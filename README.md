# Antihypertension prediction

Scores molecules for antihypertensive potential, overall and through three mechanisms, angiotensin-converting enzyme inhibition, calcium channel blockade and angiotensin II receptor antagonism, with separate models for natural products and for synthetic derivatives. Ersilia trained the six LazyQSAR classifiers for the Centre for Drug Discovery at the University of Buea, whose team curated the actives. Negatives are property-matched ChEMBL decoys at about ten per active rather than measured inactives, so the scores rank candidates instead of estimating real hit rates.

This model was incorporated on 2025-11-25.Last packaged on 2025-11-27.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4xb1`
- **Slug:** `antihypertension-prediction`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Therapeutic indication`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `6`
- **Output Consistency:** `Fixed`
- **Interpretation:** Rank score of predicted antihypertensive activity, overall and within the natural product and synthetic subsets, and via ACE, calcium channel or AT1R mechanisms. Calibrated against 50K compounds from the Ersilia reference library, so a rank above 0.65 beats 99% of them.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| antihypertension_all_rank | float | high | Rank score of the compound's predicted antihypertensive activity from the model trained on all compounds. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| antihypertension_sd_rank | float | high | Rank score of the compound's predicted antihypertensive activity from the model trained on synthetic derivatives. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| antihypertension_np_rank | float | high | Rank score of the compound's predicted antihypertensive activity from the model trained on natural products. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| ace_inh_rank | float | high | Rank score of the compound's predicted inhibition of the angiotensin-converting enzyme (ACE). Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| cc_inh_rank | float | high | Rank score of the compound's predicted calcium channel blocking activity (CCB). Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |
| at1r_inh_rank | float | high | Rank score of the compound's predicted angiotensin II receptor (AT1R) blocking activity. Calibrated against 50K compounds from the Ersilia reference library so that a score of 0.65 is better than 99% of them. Recommended threshold: 0.65. |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4xb1](https://hub.docker.com/r/ersiliaos/eos4xb1)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4xb1.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4xb1.zip)

### Resource Consumption
- **Model Size (Mb):** `68`
- **Environment Size (Mb):** `7511`
- **Image Size (Mb):** `7529.45`

**Computational Performance (seconds):**
- 10 inputs: `44.58`
- 100 inputs: `73.79`
- 10000 inputs: `1260.92`

### References
- **Source Code**: [https://github.com/ersilia-os/anti-hypertension-cedd](https://github.com/ersilia-os/anti-hypertension-cedd)
- **Publication**: [https://ersilia.io](https://ersilia.io)
- **Publication Type:** `Other`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-or-later](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4xb1
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4xb1
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
