import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"a" : [4, 5, 6], # 딕셔너리의 key값은 컬럼명이 됨
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]}, index = [1, 2, 3], columns= ['a','b','c']) # index -> 로우의 index 값

df = pd.DataFrame(
    {"a" : [4, 5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]}) # key값, index를 지정하지 않으면 0부터 자동으로 지정됨

df = pd.DataFrame(
    [[4,7,10],
     [5,8,11],
     [6,9,12]],
)

print(df)
