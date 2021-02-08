# N과 M (3)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

n,m=map(int,input().split())
l=[]
def solve(depth,n,m):
    if depth > m:
        print(*l)
        return
    for i in range(1,n+1):
        l.append(i)
        solve(depth+1,n,m)
        l.pop()
solve(1,n,m)
