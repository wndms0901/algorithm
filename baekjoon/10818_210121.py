# 최소, 최대

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

n = int(input())
lst = input().split()
a=b=int(lst[0])
for i in range(n):
    l = int(lst[i])
    if a<l: a=l
    if b>l: b=l
print(b,a)

# 다른 풀이
n = int(input())
lst = map(int,input().split())
a=b=next(lst)
for i in lst:
    if a<i: a=i
    if b>i: b=i
print(b,a)

# 다른 풀이2
input()
lst = [*map(int,input().split())]
print(min(lst),max(lst))
