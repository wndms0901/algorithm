# 좌표 정렬하기 2

# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 
# 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys
l=[]
for _ in range(int(input())):
    x,y=map(int,sys.stdin.readline().split())
    l.append((y,x))
l.sort()
for i in range(len(l)):
    print(l[i][1], l[i][0])
