# 수 정렬하기 3 *

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

import sys
a=[0]*10001
for _ in range(int(input())):
    a[int(sys.stdin.readline())]+=1
for i in range(10001):
    if a[i]!=0:
        for j in range(a[i]):
            print(i)
