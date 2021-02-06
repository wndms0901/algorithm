# N과 M (2) *

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

n, m = map(int, input().split())
v = [False] * (n+1)
out = []

def solve(depth, n, m):
    if depth > m:
        print(' '.join(map(str, out)))
        return
    for i in range(1, n+1):
        if not v[i]:
            v[i] = True
            out.append(i)
            solve(depth+1,n,m)
            out.pop()
            for j in range(i+1,n+1):
                v[j]=False

solve(1,n,m)
