from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

import sys
import os

os.chdir("../")

os.getcwd()

from source.data_preprocess import DataPreprocessing


class ModelBuilder(DataPreprocessing):
    def __init__(self, *args, **kwargs):
        super(ModelBuilder, self).__init__(*args, **kwargs)
    
    def dt(self, X_train, X_test, Y_train, Y_test):
        DT_classifier = MLPClassifier(hidden_layer_sizes=(100,), learning_rate_init=0.001, random_state=1, max_iter=1000)

        DT_classifier.fit(X = X_train, y = Y_train)

        DT_predicted = DT_classifier.predict(X_test)
        
        DT_classifier.score(X_test, Y_test)
        
        error = 0
        for i in range(len(Y_test)):
            error += np.sum(DT_predicted != Y_test)

        total_accuracy = 1 - error / len(Y_test)

        #get performance
        self.accuracy = accuracy_score(Y_test, DT_predicted)

        return DT_classifier