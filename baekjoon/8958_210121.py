# OX퀴즈

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

def f(ox):
    c=1
    s=0
    for i in ox:
        if i == 'O':
            s+=c
            c+=1
        else: c=1
    return s

l=[input() for i in range(int(input()))]
for i in l: print(f(i))

# 다른 풀이 참고
for i in range(int(input())):
    # X 기준으로 나누고 o 합을 구함
    l = [len(j)*(len(j)+1)//2 for j in input().split('X')]
    print(sum(l))
