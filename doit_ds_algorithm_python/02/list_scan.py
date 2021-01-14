# 리스트 스캔
x = [0, 1, 2]

# 원소 수를 len() 함수로 미리 알아내서 0에서 원소 수 -1까지 반복
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

# 인덱스와 원소를 짝지어 enumerate() 함수로 반복해서 꺼냄
for i, value in enumerate(x):
    print(f'x[{i}] = {value}')

# 인덱스와 원소를 짝지어 enumerate() 함수로 반복해서 꺼냄(1부터 카운트)
for i, value in enumerate(x, 1):
    print(f'{i}번째 = {value}')

# 인덱스 값을 사용하지 않고 in을 사용해서 원소를 처음부터 순서대로 꺼냄
for i in x:
    print(i)


