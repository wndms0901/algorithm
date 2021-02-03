# 수 정렬하기 2 *

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

from collections import deque
import heapq

def qsort(a,left,right):
    range = deque([],right-left+1)
    range.append((left,right))

    while range: # 비어있지 않을때 까지 반복
        pl,pr = left, right = range.pop()
        x = a[(left+right)//2]

        while pl<=pr:
            while a[pl]<x:pl+=1
            while a[pr]>x:pr-=1
            if pl<=pr:
                a[pl],a[pr]=a[pr],a[pl]
                pl+=1
                pr-=1

        if left<pr: range.append((left,pr))
        if pl<right: range.append((pl,right))
    return a

def merge_sort(a):
    def _merge_sort(a,left,right):
        """a[left]~a[right]를 재귀적으로 병합 정렬"""
        if left<right:
            center=(left+right)//2
            
            _merge_sort(a,left,center) # 배열 앞부분을 병합 정렬
            _merge_sort(a, center+1, right) # 배열 뒷부분을 병합 정렬
            p=j=0
            i=k=left

            while i <= center:
                buff[p]=a[i]
                p+=1;i+=1
            while i <= right and j<p:
                if buff[j]<=a[i]:
                    a[k]=buff[j]
                    j+=1
                else:
                    a[k]=a[i]
                    i+=1
                k+=1
            while j<p:
                a[k] = buff[j]
                k+=1;j+=1
    n = len(a)
    buff = [None]*n
    _merge_sort(a,0,n-1)
    del buff
    return a

def heap_sort(a):
    """힙 정렬"""
    def down_heap(a,left,right):
        """a[left]~a[right]를 힙으로 만들기"""
        tmp=a[left] # 루트
        parent=left
        while parent<(right+1)//2:
            cl = parent*2+1 # 왼쪽 자식
            cr = cl+1 # 오른쪽 자식
            child = cr if cr<=right and a[cr]>a[cl] else cl # 큰 값을 선택
            if tmp>=a[child]: break
            a[parent]=a[child]
            parent=child
        a[parent]=tmp
    n=len(a)
    for i in range((n-1)//2, -1, -1): # a[i]~a[n-1]을 힙으로 만들기
        down_heap(a,i,n-1)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0] # 최댓값인 a[0]와 마지막 원소를 교환
        down_heap(a,0,i-1)

def heap_sort2(a):
    heap=[]
    for i in a:
        heapq.heappush(heap,i)
    for i in range(len(a)):
        a[i]=heapq.heappop(heap)
    return a

# 다른 풀이 참고
import sys
l=[]
for _ in range(int(input())):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    print(i)
