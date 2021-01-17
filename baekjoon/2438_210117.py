# 별 찍기 -1

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

for i in range(int(input())):
    for _ in range(i+1):
        print('*',end='')
    print()


# 다른 풀이 참고
for i in range(int(input())):print('*'*(i+1))

