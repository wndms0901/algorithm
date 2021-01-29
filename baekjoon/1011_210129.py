# Fly me to the Alpha Centauri *

# 이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다. 
# 예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나 사실상 
# 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며, 그 다음에는 0 , 1 , 2 
# 광년을 이동할 수 있는 것이다. ( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )
# 김우현은 공간이동 장치 작동시의 에너지 소모가 크다는 점을 잘 알고 있기 때문에 x지점에서 y지점을 향해 
# 최소한의 작동 횟수로 이동하려 한다. 하지만 y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 
# 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
# 김우현을 위해 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.

# 문제 풀이 참고
# 거리        값      작동횟수
#  1          1          1 
#  2          11         2
#  3         111         3
#  4         121         3
#  5         1211        4
#  6         1221        4
#  7         12211       5
#  8         12221       5
#  9         12321       5
#  10        123211      6
# 거리가 제곱인 수일 때 작동횟수가 2(거리의 제곱근-1)+1씩 증가
# 1**2<n<2**2는 1/1 증가
# 2**2<n<3**2는 1/1/2/2
# 3**2<n<4**2는 1/1/1/2/2/2
import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    d=y-x # 거리
    d2=int(math.sqrt(d)) # 거리의 제곱근(정수)
    # 거리의 제곱근이 정수이면 작동횟수가 2(거리의 제곱근-1)+1씩 증가
    if d2==math.sqrt(d): print(2*(d2-1)+1)
    elif d <=(((d2+1)**2)+(d2**2))//2:
        print(2*(d2-1)+1+1)
    else: print(2*((d2+1)-1)+1)