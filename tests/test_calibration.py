import numpy as np
from src.conformal.calibration import conformal_quantile

def test_quantile_returns_observed_score():
    scores=np.array([0.1,0.2,0.3,0.4,0.5])
    assert conformal_quantile(scores,0.2) in scores
