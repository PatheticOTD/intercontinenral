import numpy as np
from scipy.stats import mode
from sklearn.base import BaseEstimator, ClassifierMixin

class MostFrequentClassifier(ClassifierMixin, BaseEstimator):
    # Predicts the rounded (just in case) median of y_train
    def __init__(self, *, param = 1):
        self.param = param
        
    def fit(self, X=None, y=None):
        self.is_fitted_ = True
        
        self.param = mode(y)[0]
        return self

    def predict(self, X=None):
        return np.full(shape=X.shape[0], fill_value = self.param)