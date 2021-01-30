# 터렛 *

# 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과
# 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x1-x2)**2+(y1-y2)**2)**0.5 # 두 점의 거리
    if r1>r2: r1,r2=r2,r1
    if d==0 and r1==r2: print(-1) # 같은 원
    elif d==r1+r2 or d==r2-r1:print(1) # 외접,내접
    elif r2-r1<d<r1+r2: print(2)# 두 원이 서로 다른 두 점에서 만날 때
    else: print(0)
