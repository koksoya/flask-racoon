import requests
import json
import pandas as pd
from predictor import my_location_predictor

class Frames:
    def __init__(self):
        self.column = ['point_of_interest', 'finance', 'store', 'supermarket',
                  'clothing_store', 'label']
        self.store = {}
        self.bornova = self.retrieve("bornova")
        self.buca = self.retrieve("buca")
        self.konak = self.retrieve("konak")

    
    def retrieve(self,district):
        r = requests.get(
            "https://refined-cheer.firebaseio.com/"+district+".json")
        jsonObject = json.loads(r.text)
        my_dict = my_dictionary()

        self.store[district] = jsonObject

        for key in jsonObject.keys():
            element = jsonObject[key]
            my_dict.add(key, element.get("environment"))

        dynamicFrame = pd.DataFrame(my_dict).T

        self.column_equalizer_dropper(self.column,dynamicFrame)

        dynamicFrame.fillna(0, inplace=True)
        
        values = dynamicFrame.values
        predictor = my_location_predictor()
        predictions = predictor.predict(values)
        
        return dynamicFrame[predictions==1].index
        
    def column_equalizer_dropper(self, column, stores):
        drop_from_stores = set(stores.columns)-set(column)
        stores.drop(columns=list(drop_from_stores), inplace=True)
        add_to_stores = set(column)-set(stores.columns)
        for column in add_to_stores:
            if(column != "label"):
                stores[column] = 0

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

