# 스택으로 재귀 함수 구현하기 (재귀를 제거)

from collections import deque

def recur(n: int) -> int:
    """재귀를 제거한 recur() 함수"""
    s = deque([None] * n)

    while True:
        if n > 0:
            s.append(n) # n값을 푸시
            n -= 1
            continue
        if s:   # 스택이 비어 있지 않으면
            n = s.pop() # 저장한 값을 n에 팝
            if n is None:
                break
            print(n)
            n = n - 2
            continue

x = int(input('정숫값을 입력하세요'))
recur(x)
