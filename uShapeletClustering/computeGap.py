import uShapeletClustering.computeDistance
import numpy as np
def computeGap(s,D,k):
    dis=uShapeletClustering.computeDistance.computeDistance(s,D)
    dis=np.sort(dis)
    maxGap=0
    dt=0
    Da=[]
    Db=[]
    for l in range(0,(dis.shape[0]-1)):
        d=(dis[l]+dis[l+1])/2
        for i in range(0,dis.shape[0]):
            if dis[i]<d:
                Da.append(dis[i])
            else:
                Db.append(dis[i])
        r=len(Da)/len(Db)
        # print(r)
        # print(Db)
        # print(1/k)
        # print(1-(1/k))
        # print('***************************')
        if r>0 and r<0.7:
            ma=np.mean(Da)
            mb=np.mean(Db)
            sa=np.std(Da)
            sb=np.std(Db)
            gap= mb-sb-(ma+sa)
            # print(gap)
            # print('####################################################')
            if gap>maxGap:
                maxGap=gap
                dt=d
    return maxGap,dt