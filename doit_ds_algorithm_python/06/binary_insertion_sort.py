# 이진 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def binary_inserion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1,n):
        key = a[i]
        pl = 0 # 검색 범위의 맨 앞 원소 인덱스
        pr = i-1 # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl+pr) // 2 # 검색 범위의 가운데 원소 인덱스
            if a[pc] == key: # 검색 성공
                break
            elif a[pc] < key: 
                pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
            else:
                pr = pc -1  # 검색 범위를 앞쪽 절반으로 좁힘 
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1 # 삽입해야 할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key

if  __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요>'))
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_inserion_sort(x) # 배열 x를 이진 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')