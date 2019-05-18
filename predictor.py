import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier

class my_location_predictor():
    def __init__(self):
        pass
    
    def deserialize(self):
    # de-serialize mlp_nn.pkl file into an object called model using pickle
        with open('model.pkl', 'rb') as handle:
            model = pickle.load(handle)
            return model

    def predict(self,values):
        model = self.deserialize()
        return model.predict(values)