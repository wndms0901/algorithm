# N과 M (1) *

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

n, m = map(int, input().split())
v = [False] * (n+1)  # 탐사 여부 check
out = []  # 출력 내용

def solve(depth, n, m):
    if depth > m: 
        print(' '.join(map(str, out)))
        return
    for i in range(1,n+1):
        if not v[i]:
            v[i] = True
            out.append(i)
            solve(depth+1, n, m)
            v[i] = False
            out.pop()
solve(1, n, m)           


# 다른 풀이 참고
N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용

def solve2(depth, N, M):
    if depth == M:  # 탈출 조건
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력
        return
    for i in range(len(visited)):  # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면
            visited[i] = True  # 탐사 시작(중복 제거)
            out.append(i+1)  # 탐사 내용
            solve(depth+1, N, M)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

solve2(0, N, M)
