# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2):
        a[i], a[n -i -1] = a[n -i -1], a[i]

if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요>'))
    x = [None] * nx # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요>'))

    reverse_array(x) # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')


# reverse() 함수 사용
l = [0, 1, 2, 3, 4] # 리스트
l_reverse = l.reverse()
print(l_reverse) # None으로 출력됨
print(l) # 역순으로 정렬되어 출력됨

t = ('a', 'b', 'c') # 튜플
d = {'a': 1, 'b': 2, 'c': 3} # 딕셔너리
s = 'abc' # 문자열
# t.reverse() 에러 AttributeError: 'tuple' object has no attribute 'reverse'
# d.reverse() 에러 AttributeError: 'dict' object has no attribute 'reverse'
# s.reverse() 에러 AttributeError: 'str' object has no attribute 'reverse'

# reversed() 함수 사용
l = [0, 1, 2, 3, 4] # 리스트
t = ('a', 'b', 'c') # 튜플
d = {'aa': 1, 'bb': 2, 'cc': 3} # 딕셔너리
s = 'abc' # 문자열

print(reversed(l)) # <list_reverseiterator object at 0x000001EF23AF2FD0>
print(reversed(t)) # <reversed object at 0x000001D03D7A2FD0>
# print(reversed(d))  <dict_reversekeyiterator object at 0x000001D03D79D5E0>
print(reversed(s)) # <reversed object at 0x000001D03D7A2FD0>

print(list(reversed(l)))
print(tuple(reversed(t)))
# print(list(reversed(d)))  키값만 출력됨
print(''.join(reversed(s)))

