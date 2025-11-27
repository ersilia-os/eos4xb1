# Antihypertension prediction

This model is built on a manually curated collection of natural products and synthetic derivatives with antihypertension activity, as well as target-specific data. The actives have been curated by the CeDD (University of Buea) and the negatives are added from the decoy sampler eos3e6s. Models are built with LazyQSAR.



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
- **Interpretation:** Probability of antihypertensive activity (general or target-specific)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| antihypertension_all_proba | float | high | Probability of having an antihypertensive effect |
| antihypertension_sd_proba | float | high | Probability of having an antihypertensive effect with a domain applicability of the model to synthetic compounds |
| antihypertension_np_proba | float | high | Probability of having an antihypertensive effect with a domain applicability of the model to natural products |
| ace_inh_proba | float | high | Probability of inhibiting ACE protein |
| cc_inh_proba | float | high | Probability of being a CCB (Calcium Channel Blocker) |
| at1r_inh_proba | float | high | Probability of being an AT1R blocker |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`

### Resource Consumption


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
