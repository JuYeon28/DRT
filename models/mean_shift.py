import numpy as np

from sklearn.cluster import MeanShift, estimate_bandwidth

from .base import ModelBase

class MeanShiftClustering(ModelBase):
    def __init__(self,X):
        self.bw = self.find_bandwidth(X)
        print(self.bw)
        self.model = MeanShift(bandwidth = self.bw)

    def _reset(self):
        self.bw = None

    def find_bandwidth(self,X):
        return estimate_bandwidth(X,quantile=0.05)

    def fit(self,X):
        cluster_labels = self.model.fit_predict(X)
        print('Cluster Label 유형:',np.unique(cluster_labels))
        return cluster_labels
        