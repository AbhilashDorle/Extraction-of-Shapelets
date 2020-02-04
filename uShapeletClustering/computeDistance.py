import numpy as np
import math
from scipy.spatial import distance
import uShapeletClustering.zNorm
def computeDistance(s,D):
    dis=np.full(D.shape[0],np.inf)
    dis = dis.astype('float64')
    normalized_s=uShapeletClustering.zNorm.zNorm(s.copy())
    # print(normalized_s)
    for i in range(0,D.shape[0]):
        ts=D.iloc[i]
        for j in range(0, (len(ts) - len(s) + 1)):
            # print('original dataseq:',ts[j:(j+len(s))])
            normalized_dataseq=uShapeletClustering.zNorm.zNorm(ts[j:(j+len(s))])
            # print('normalized dataseq:',normalized_dataseq)
            # print('shapelet:',normalized_s)
            d=distance.euclidean(normalized_s,normalized_dataseq)
            dis[i]=min(d,dis[i])
    dis=dis/math.sqrt(len(s))
    return dis