# from statistics import LinearRegression
from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ls = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
# print(type(ls))
# print(ls)
x = ls[["GDP per capita (USD)"]].values
y = ls[["Life satisfaction"]].values

# ls.plot(kind="scatter", grid=True, x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23500, 62500, 4, 9])
# plt.show()

model = LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)
model.fit(x,y)

X_new = [[31721.3]] #ROK 2020
print(model.predict(X_new))
# LinearRegression 5.90
# KNeighborsRegressor 5.70