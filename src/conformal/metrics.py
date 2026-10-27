import numpy as np

def marginal_coverage(prediction_sets, labels):
    prediction_sets=np.asarray(prediction_sets,dtype=bool)
    labels=np.asarray(labels,dtype=int)
    return float(prediction_sets[np.arange(prediction_sets.shape[0]),labels].mean())

def set_sizes(prediction_sets):
    return np.asarray(prediction_sets,dtype=bool).sum(axis=1)
