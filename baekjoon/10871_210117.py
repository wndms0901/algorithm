# X보다 작은 수

# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

n, x = map(int,input().split())
lst = map(int,input().split())
for i in lst:
    if i < x: print(i,end=' ')

# 다른 풀이 참고
n,x=map(int,input().split())
print(*(i for i in input().split() if int(i)<x))

