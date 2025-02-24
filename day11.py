import numpy as np

v = np.array([1,3,-9,2])
# 파이썬에서는 리스트에 다른 타입이 들어갈 수 있지만 넘파이에서는 다른 타입을 넣으면 전체가 다 바뀜
# float64 = double
print(v, v.ndim)

a = np.array([1,3,5,7]) # 32바이트 -> 한 칸 당 8바이트
print(a, a.dim, a.shape, a.dtype)
b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(b, b.dim, b.shape, b.dtype, b.strides)
c = np.array([[[1,2,3,4], [5,6,7,"8"], [9,10,11,12]]])
c = np.array([[[1,2,3,4,1], [5,6,7,8,1]], [[1,2,3,4], [9,10,11,12]]])
print(c, c.dim, c.shape, c.dtype)

# ndim -> 배열의 차원 수를 나타내는 속성
# shape -> 배열의 차원과 크기를 나타내는 튜플 형태의 속성
# dtype -> 배열 요소들의 데이터 타입을 나타내는 속성 (요소들은 해당 데이터 타입으로 일괄적으로 처리)
# strides -> 면, 행, 열 간의 간격을 나타냄


# zeros().ones() -> 주어진 모양(shape)에 대해 모든 요소가 0 또는 1인 배열을 생성하는 함수
ones = np.ones((3,4))
print(ones)
# zeros = np.ones((3,4))
zeros = np.ones((3,4),dtype = np.int16) # int16으로 지정했기 때문에 한 원소를 저장할 때 2바이트 사용
print(zeros)


# arrage() -> 지정된 범위 내에서 일정한 간격으로 숫자가 담긴 배열을 생성하는 함수

a = np.arrage(5)
print(a, a.ndim. a.shape, a.size)

a = np.arrange(5,11)
print(a, a.ndim, a.shape, a.size)

a = np.arrange(5,11,2)
print(a, a.ndim, a.shape, a.size)

a = np.arrange(2.0, 11.8, 0.2)
print(a, a.ndim, a.shape, a.size)

a = np.arrange(2.0, 11.8, 2.0, dtype = np.int16)
print(a, a.dim, a.shape, a.size)

# linspace() -> 지정된 범위 내에서 균등하게 분할된 숫자가 담긴 배열을 생성하는 함수
# reshape() -> 배열의 모양(shape)을 변경하는 메서드로 새로운 모양에 맞게 요소들을 재배열
