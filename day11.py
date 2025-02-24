import numpy as np
import pandas as pd

df = pd.DataFrame(
    {"a" : [4, 5, 6], # 딕셔너리의 key값은 컬럼명이 됨
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]}, index = [1, 2, 3]) # index -> 로우의 index 값

print(df)
