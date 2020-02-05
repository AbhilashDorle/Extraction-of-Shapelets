import pandas as pd
import numpy as np
import uShapeletClustering.Clustering
import scipy.io
timeseries_df=pd.read_csv(r"D:\Dr. Sheng Li\Datasets\UCRArchive_2018\GunPoint\sample2.tsv",sep="\t")# Line 2 in table 2
# # dataset=timeseries_df.drop(timeseries_df.columns[0],axis=1)
# # dataset.columns = range(dataset.shape[1])
labels=np.array(timeseries_df['0'])
unique_labels=np.unique(labels)
num_classes=['one','two','three']
# print('The number of classes are',num_classes)
# shape=input("Enter the length of uShapelet:")
shape=[5];
# K=input("Enter the number of clusters:")
K=2
shapelets=uShapeletClustering.Clustering.cluster(shape, timeseries_df, labels,K)
print(shapelets)
S=[]
for slist in shapelets:
    temp=np.zeros((len(slist),),dtype=np.object)
    temp[:]=slist
    S.append(temp)
matlab_dict={}
count=0
for i in range(len(shapelets)):
    matlab_dict[num_classes[count]]=S[i]
    count=count+1
scipy.io.savemat('new.mat', matlab_dict)