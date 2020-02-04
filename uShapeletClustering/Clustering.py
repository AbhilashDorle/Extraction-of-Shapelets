import uShapeletClustering.extractU_Shapelets
import uShapeletClustering.Kmeans
import numpy as np
from tslearn.shapelets import ShapeletModel
from tslearn.shapelets import grabocka_params_to_shapelet_size_dict
from keras.optimizers import Adagrad
def cluster(shape,timeseries_df,data_labels,k):
    Shapelet_list = []
    for i in range(1,max(data_labels)+1):
        ts_df=timeseries_df[timeseries_df['0']==i]
        ts_df=ts_df.reset_index(drop=True)
        # cluster_list.append(extractU_Shapelets(shape)
        labels = ts_df['0']
        ts_df = ts_df.drop(ts_df.columns[0], axis=1)
        S=uShapeletClustering.extractU_Shapelets.extract_Shapelets(ts_df.copy(),shape,k)
        S = np.array(list(S))
        pred_label=uShapeletClustering.Kmeans.Kmeans(ts_df.copy(),S,k,labels)
        shapelet_sizes = grabocka_params_to_shapelet_size_dict(n_ts=ts_df.shape[0],
                                                               ts_sz=ts_df.shape[1],
                                                               n_classes=2,
                                                               l=0.5,
                                                               r=1)
        shp_clf = ShapeletModel(n_shapelets_per_size=shapelet_sizes,
                            optimizer=Adagrad(lr=.1),
                            weight_regularizer=.01,
                            max_iter=50,
                            verbose=0)
        shp_clf.fit(ts_df, pred_label)
        shapelets=shp_clf.shapelets_;
        temp_list=[]
        for i in range(0, shapelets.shape[0]):
            temp= shapelets[i].T
            temp_list.append(temp[0])
        Shapelet_list.append(temp_list)
    return Shapelet_list
