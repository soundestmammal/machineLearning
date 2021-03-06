import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 #  Importing the dataset 
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[: , 1:2].values
y = dataset.iloc[: , 2].values
y = y.reshape(-1,1)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

# Visualizing the SVR results
plt.scatter(X, y, color="red")
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Truth or Bluff(SVR)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

