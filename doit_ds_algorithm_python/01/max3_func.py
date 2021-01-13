# 세 정수의 최대값 구하기

def max3(a,b,c):
    """a,b,c의 최대값을 구하여 반환"""
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum # 최대값 반환

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(3, 6, 2) = {max3(3, 6, 1)}')