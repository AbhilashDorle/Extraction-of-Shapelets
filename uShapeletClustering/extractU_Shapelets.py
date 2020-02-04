import uShapeletClustering.computeGap
import uShapeletClustering.computeDistance
import numpy as np
import pandas as pd
def extract_Shapelets(D,sLen,k):
    S=[]
    ts=D.iloc[0]
    while(True):
        cnt=-1
        s=[]
        Gap=[]
        dt=[]
        Da=[]
        for sl in sLen:
            for j in range(0, (len(ts) - sl) + 1):
                s.append(list(ts[j:(j+sl)]))
                temp_gap,temp_dt=uShapeletClustering.computeGap.computeGap(s[cnt+1],D,k)
                Gap.append(temp_gap)
                dt.append(temp_dt)
        # print(Gap)
        index1=Gap.index(max(Gap))
        S.append(s[index1])
        dis=uShapeletClustering.computeDistance.computeDistance(s[index1],D)
        for i in range(0,(dis.shape[0])):
            if dis[i]<dt[index1]:
                Da.append(dis[i])
        if len(Da)==1:
            break;
        else:
            index2=np.where(dis==np.amax(dis))
            ts=D.iloc[index2]
            sum_value=np.mean(Da)+np.std(Da)
            D_hat=[]
            for i in range(0,dis.shape[0]):
                if dis[i]<sum_value:
                    D_hat.append(np.where(dis==dis[i])[0][0])
            D = D.drop(D.index[D_hat])
            D = np.array(D)
            D = pd.DataFrame(D)
    S = set(tuple(row) for row in S)
    return S