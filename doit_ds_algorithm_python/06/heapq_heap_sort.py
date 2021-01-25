# 힙 정렬 알고리즘 구현하기(heapq.push와 heapq.pop을 사용)

import heapq
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬(heapq.push와 heapq.pop을 사용)"""
    heap = []
    for i in a:
        # heappush
        # 힙에 원소를 추가
        heapq.heappush(heap, i)
    print('heap', heap)
    for i in range(len(a)):
        # heappop
        # 가장 작은 원소를 꺼내어 리턴, 자동적으로 그 다음으로 작은 원소가 루트노트가 됨
        a[i] = heapq.heappop(heap) 

if __name__ == '__main__':
    print('힙 정렬을 수행합니다(heapq.push와 heapq.pop를 사용).')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
