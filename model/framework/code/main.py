import os
import sys

from ersilia_pack_utils.core import read_smiles, write_out
from lazyqsar.api.classifier_predict import predict

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
checkpoints = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

MODELS = {
    "antihypertension_all_rank": "allmols_eos3e6snegs",
    "antihypertension_sd_rank": "sd_eos3e6snegs",
    "antihypertension_np_rank": "np_eos3e6snegs",
    "ace_inh_rank": "ACE_eos3e6snegs",
    "cc_inh_rank": "CCBs_eos3e6snegs",
    "at1r_inh_rank": "AT1RBs_eos3e6snegs",
}

_, smiles_list = read_smiles(input_file)

outputs, header = predict(
    {name: os.path.join(checkpoints, folder) for name, folder in MODELS.items()},
    smiles=smiles_list,
    predict_type="rank",
)

# Ersilia reports missing values as empty cells; csv.writer would otherwise
# render an unparseable SMILES as the string "nan".
outputs = [["" if v is None or v != v else v for v in row] for row in outputs]

write_out(outputs, header, output_file)