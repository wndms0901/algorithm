# 큰 수 A+B

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

print(sum(map(int,input().split())))

# 다른 풀이
a,b=input().split()
p=0
r=''
if len(b)>len(a): a,b=b,a
if len(a)!=len(b): b='0'*(len(a)-len(b))+b

for i in range(len(a)-1,0-1,-1):
    x=int(a[i])+int(b[i])+p;p=0
    if x>9:p=x//10;r+=str(x%10)
    else: r+=str(x)
if p>0:r+=str(p)

print(r[::-1])
