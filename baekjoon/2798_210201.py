# 블랙잭

# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

n,m=map(int,input().split())
l=list(map(int,input().split()))
s=[];a=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s.append(l[i]+l[j]+l[k])
for i in s:
    if i<=m and i>a:a=i
print(a)
