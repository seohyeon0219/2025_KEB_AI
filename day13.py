import pandas as pd

data = [1, 7, 5, 2, 8, 3, 6, 4]

bins = [0, 3, 6, 9] # 첫 번째 구간 : 0~3, 두 번째 구간 : 3~6...

labels = ["low", "mid", "high"] # 구간마다 라벨 지정

cat = pd.cut(data, bins, True, labels)
# pd.cut(숫자 리스트, 나눌 구간, 생략 가능, 구간에 붙일 라벨)
# right = True 이므로 왼쪽 값은 포함하지 않고 오른쪽 값만 포함함
cat = pd.cut(data, bins, labels = labels, right = False)
# right = False 이므로 왼쪽 값을 포함하고 오른쪽 값은 포함하지 않음
print(cat)
# pd.cut -> 연속형 데이터를 범주형 데이터로 변환하는 과정




