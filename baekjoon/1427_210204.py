# 소트인사이드

# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

n=input()
for i in sorted(n,reverse=True):
    print(i,end='')
