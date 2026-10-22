import json
import os

import numpy as np
import stylia
from sklearn.metrics import auc, roc_curve

# Format: slide | Style: ersilia - change with stylia.set_format() / stylia.set_style()
stylia.set_format("slide")
stylia.set_style("ersilia")

root = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.abspath(os.path.join(root, "..", "results"))

MODELS = [
    "allmols_eos3e6snegs",
    "sd_eos3e6snegs",
    "np_eos3e6snegs",
    "ACE_eos3e6snegs",
    "CCBs_eos3e6snegs",
    "AT1RBs_eos3e6snegs",
]

MAX_POINTS = 100


def load_results(name):
    with open(os.path.join(results_dir, f"report_crossval_{name}.json"), "r") as f:
        return json.load(f)


def plot_roc_curve(ax, name):
    results = load_results(name)
    nc = stylia.NamedColors()
    mean_fpr = np.linspace(0, 1, 100)
    tprs, aucs = [], []
    for fold in results.values():
        fpr, tpr, _ = roc_curve(fold["y_true"], fold["y_hat"])
        aucs.append(auc(fpr, tpr))
        tpr_interp = np.interp(mean_fpr, fpr, tpr, left=0.0, right=1.0)
        tpr_interp[0] = 0.0
        tprs.append(tpr_interp)
        ax.plot(mean_fpr, tpr_interp, color=nc.get("plum", lighten=0.5))
    mean_tpr = np.mean(tprs, axis=0)
    ax.plot(
        mean_fpr,
        mean_tpr,
        color=nc.plum,
        label="AUC = {:.3f} $\\pm$ {:.3f}".format(np.mean(aucs), np.std(aucs)),
    )
    ax.plot([0, 1], [0, 1], linestyle="--", color=nc.gray)
    ax.legend(loc="lower right")
    stylia.label(ax, xlabel="False positive rate", ylabel="True positive rate", title=name)


def plot_yhat(ax, name):
    # The crossvalidation reports store probabilities, not ranks, so this panel
    # is on the proba scale and carries no 0.65 decision line.
    results = load_results(name)
    nc = stylia.NamedColors()
    fold = results[list(results)[0]]
    y_hat = np.array(fold["y_hat"])
    y_true = np.array(fold["y_true"])
    for label, color in ((0, nc.gray), (1, nc.plum)):
        y = y_hat[y_true == label]
        np.random.shuffle(y)
        y = y[:MAX_POINTS]
        ax.scatter(label + np.random.uniform(-0.1, 0.1, size=y.size), y, color=color, alpha=0.5)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Neg", "Pos"])
    ax.set_ylim(-0.05, 1.05)
    stylia.label(ax, xlabel="", ylabel="Probability", title=name)


fig, axs = stylia.create_figure(2, 3)
for name in MODELS:
    plot_roc_curve(axs.next(), name)
stylia.save_figure(os.path.join(results_dir, "performance_5fold.png"))

fig, axs = stylia.create_figure(2, 3)
for name in MODELS:
    plot_yhat(axs.next(), name)
stylia.save_figure(os.path.join(results_dir, "yhat_5fold.png"))

for name in MODELS:
    roc_aucs = [fold["roc_auc"] for fold in load_results(name).values()]
    print(f"{name}: MEAN AUC {np.mean(roc_aucs):.3f} +/- {np.std(roc_aucs):.3f}")
