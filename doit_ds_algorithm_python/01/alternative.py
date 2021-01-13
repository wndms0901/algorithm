# +와 -를 번갈아 출력하기

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?>'))

for _ in range(n // 2): # for문에 언더스코어(_)를 사용한 이유: 인덱스를 사용하지 않기 때문
    print('+-', end='')

if n % 2: 
    print('+', end='')
