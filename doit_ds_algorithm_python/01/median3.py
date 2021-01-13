# 세 정수를 입력받아 중앙값 구하기

def med3(a,b,c,):
    """a,b,c의 중앙값을 구하여 반환"""
    if a > b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

a = int(input('정수 a값을 입력하세요>'))
b = int(input('정수 b값을 입력하세요>'))
c = int(input('정수 c값을 입력하세요>'))

print(f'중앙값 = {med3(a,b,c)}')


