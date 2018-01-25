# -*- coding: utf-8 -*-
# this is another comment to finish this - jan 24
# Simple Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, 1]

