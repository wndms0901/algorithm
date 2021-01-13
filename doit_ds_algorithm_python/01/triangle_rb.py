# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기(1)

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요>'))

for i in range(n):
    print(' ' * (n-(i+1)), end='')    
    for j in range(i + 1):
        print('*', end='')
    print()

# 오른쪽 아래가 직각인 이등변 삼각형으로 * 출력하기(2)

print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다.')
n = int(input('짧은 변의 길이를 입력하세요>'))

for i in range(n):
    for _ in range(n -i -1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()
   