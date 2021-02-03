# 통계학

# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 
# 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

import sys
n=int(input());l=[];p=0
for _ in range(n):
    l.append(int(sys.stdin.readline()))
if min(l)<0: p=-min(l)
c=[0]*(max(l)+p+1)
for i in range(n):
    c[l[i]+p]+=1
val3=c.index(max(c))-p
if c.count(max(c))>1:
    cnt=0;idx=0
    for i in range(len(c)):
        if max(c)==c[i]: cnt+=1
        if cnt==2: idx=i; break
    val3=idx-p
l.sort()
print(f'{sum(l)/n:.0f}')
print(l[n//2])
print(val3)
print(0 if len(l)==1 else abs(max(l)-min(l)))
