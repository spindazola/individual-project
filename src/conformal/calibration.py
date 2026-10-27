import math
import numpy as np

def conformal_quantile(scores, alpha):
    scores=np.asarray(scores,dtype=float)
    if scores.ndim != 1 or scores.size == 0:
        raise ValueError("scores must be a non-empty 1D array")
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    n=scores.size
    level=min(math.ceil((n+1)*(1-alpha))/n,1.0)
    return float(np.quantile(scores, level, method="higher"))
