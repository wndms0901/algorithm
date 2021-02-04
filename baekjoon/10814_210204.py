# 나이순 정렬 *
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로,
# 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

import sys
n=int(input());a=[];b=[]
for _ in range(n):
    x,y=sys.stdin.readline().split()
    a.append(int(x));b.append(y)
f=[0]*(max(a)+1);l=[0]*n
for i in range(n):f[a[i]]+=1
for i in range(1,max(a)+1):f[i] += f[i-1]
for i in range(n-1,-1,-1):f[a[i]]-=1;l[f[a[i]]]=(a[i],b[i])
for i in range(n): print(l[i][0],l[i][1])
