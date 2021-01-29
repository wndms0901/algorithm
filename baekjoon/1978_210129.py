# 소수 찾기

# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

input()
l=list(map(int,input().split()))
p=[2,3]
for n in range(5,1000+1,2):
    i=1
    while p[i]*p[i]<=n:
        if n%p[i]==0: break
        i+=1
    else:
        p.append(n)
c=0
for i in l:
    if i in p:c+=1
print(c)
