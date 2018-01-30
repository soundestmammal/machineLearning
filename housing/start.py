# Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

melbourne_file_path = "melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_price_data = melbourne_data.Price

print(melbourne_price_data.head())