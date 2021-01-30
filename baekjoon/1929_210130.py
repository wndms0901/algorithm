# 소수 구하기 *

# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 에라토스테네스의 체 참고
m,n=map(int,input().split())
l=[True]*1000000
for i in range(2,1000000):
    if l[i]==True:
        for j in range(2*i,1000000,i):
            l[j]=False
print(*[i for i in range(m,n+1) if l[i]==True and i!=1], sep='\n')
