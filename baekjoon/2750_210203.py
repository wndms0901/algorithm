# 수 정렬하기 *

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

def bubble_sort(a):
    n=len(a)
    k=0
    while k < n-1:
        last = n-1
        for j in range(n-1,k,-1):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j], a[j-1]
                last =j
        k = last
    return a
def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a
def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        tmp=a[i]
        while j > 0 and a[j-1]> tmp:
            a[j] = a[j-1]
            j-=1
        a[j] = tmp
    return a

a=[]
for _ in range(int(input())):
    a.append(int(input()))
print(*bubble_sort(a), sep='\n')
