# Assignment
# v0.9) v0.8의 결측치 값을 산술평균으로 채워넣는 다양한 방법을 버전별로 적용하시오.
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {
        'A':[1,2,np.nan,4],
        'B':[np.nan,12,3,4],
        'C':[1,2,3,4]
    }
)

print(df)