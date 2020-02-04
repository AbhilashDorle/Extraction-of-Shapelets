from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
import numpy as np
import uShapeletClustering.computeDistance
def Kmeans(D,S,k,true_labels):
    rowsize = S.shape[0]  # number of ushapelets
    colsize = D.shape[0]  # number of timeseries
    inertia = []  # sumd list
    DIS = np.zeros(shape=(rowsize, colsize))
    label = []  # np.zeros(shape=(colsize,))#cls in paper
    kmeans = KMeans(n_clusters=k)
    rand_score = []
    for i in range(0, S.shape[0]):
        dis = uShapeletClustering.computeDistance.computeDistance(S[i], D)
        DIS[i] = dis
        sumDIS = float(10000)
        DIS_T = DIS.T
        for j in range(0, rowsize):
            kmeans.fit(DIS_T)
            inertia.append(kmeans.inertia_)
            if sum(inertia) < sumDIS:
                labels_pred = kmeans.labels_
                label.append(labels_pred)
                score = adjusted_rand_score(true_labels, labels_pred)
                rand_score.append(score)
    a = rand_score.index(max(rand_score))
    return label[a]