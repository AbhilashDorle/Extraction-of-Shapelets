import numpy as np
def zNorm(s):
    series_mean=np.mean(s)
    series_std=np.std(s)
    s=(s-series_mean)/series_std
    return s