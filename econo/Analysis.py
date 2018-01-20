# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_stata('401K.DTA')

part = dataset.iloc[:, 0].values
match = dataset.iloc[:, 1].values

avgPart = np.mean(part)
avgMatch = np.mean(match)

print("The average participation rate is ", avgPart)
print("The average match rate is ", avgMatch)

# prate = bnot + multiplier * mrate + u
# assume that u = 0

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(match, part, test_size = 0.5, random_state = 0)

X_train = [X_train]
y_train = [y_train]
X_test = [X_test]
y_test = [y_test]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train, sample_weight = None)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_test), color = 'blue')
plt.title('401K Problem')
plt.xlabel('Matching rate')
plt.ylabel('Participation rate')
plt.show()



