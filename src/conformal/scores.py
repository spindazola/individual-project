import numpy as np

def lac_scores(probs, labels):
    probs=np.asarray(probs,dtype=float)
    labels=np.asarray(labels,dtype=int)
    if probs.ndim != 2 or labels.ndim != 1 or labels.shape[0] != probs.shape[0]:
        raise ValueError("expected probs [N,K] and labels [N]")
    return 1.0-probs[np.arange(probs.shape[0]),labels]
