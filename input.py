import pandas as pd
import numpy as np
import uShapeletClustering.Clustering

timeseries_df=pd.read_csv(r"D:\Dr. Sheng Li\Datasets\UCRArchive_2018\GunPoint\sample4.tsv",sep="\t")# Line 2 in table 2
# # dataset=timeseries_df.drop(timeseries_df.columns[0],axis=1)
# # dataset.columns = range(dataset.shape[1])
labels=np.array(timeseries_df['0'])
# unique_labels=np.unique(labels)
# num_classes=unique_labels.shape[0]
# print('The number of classes are',num_classes)
# shape=input("Enter the length of uShapelet:")
shape=[35];
# K=input("Enter the number of clusters:")
K=2
shapelets=uShapeletClustering.Clustering.cluster(shape, timeseries_df, labels,K)
print(shapelets)
print('***************')
print(shapelets[0])
print('###################')
print(shapelets[0][0])
print('&&&&&&&&&&&&&&&&&')
print(shapelets[0][0][0])