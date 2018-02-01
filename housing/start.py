# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

melbourne_file_path = "melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_price_data = melbourne_data.Price

print(melbourne_price_data.head())

columns_of_interest = ['Landsize' , 'BuildingArea']
two_columns_of_data = melbourne_data[columns_of_interest]
two_columns_of_data.describe()

melbourne_data = melbourne_data.dropna() 

y = melbourne_data.
melbourne_predictors = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_predictors]

from sklearn.tree import DecisionTreeRegressor

melbourne_model = DecisionTreeRegressor()
melbourne_model.fit(X , y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()