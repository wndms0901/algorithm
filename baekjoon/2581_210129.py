# 소수

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로,
#  이들 소수의 합은 620이고, 최솟값은 61이 된다.

m=int(input());n=int(input())
p=[2,3];l=[]

for x in range(5,10000+1,2):
    i=1
    while p[i]*p[i]<=x:
        if x%p[i]==0: break
        i+=1
    else: p.append(x)

for j in range(m,n+1):
    if p.count(j)>0: l.append(j)
if len(l) == 0: print(-1)
else: print(sum(l),min(l), sep='\n')
