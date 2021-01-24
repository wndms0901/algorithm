# 숫자의 합

# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

input();l=[int(i) for i in input()]
print(sum(l))

# 다른 풀이
n=int(input())
string=input()
s=0
for i in range(n):
    s+=int(string[i])
print(s)

# 다른 풀이 참고
input();print(sum(map(int,input())))
