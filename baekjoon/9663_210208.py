# N-Queen **

# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

n=int(input())
pos=[0]*n
flag_a=[False]*n
flag_b=[False]*((n-1)*2+1)
flag_c=[False]*((n-1)*2+1)
cnt=0

def solve(i):
    global cnt
    for j in range(n):
        if (    not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[j-i+(n-1)]):
            pos[i]=j    
            if i == n-1:
                cnt+=1
            else: 
                flag_a[j]=flag_b[i+j]=flag_c[j-i+(n-1)]=True
                solve(i+1)
                flag_a[j]=flag_b[i+j]=flag_c[j-i+(n-1)]=False
solve(0)
print(cnt)
