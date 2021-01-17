# A + B -3

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

n = int(input())
lst = [None] * n
for i in range(n):
   a, b = input().split()
   lst[i] = int(a) + int(b)
for x in lst:
    print(x)
   
# 다른 풀이 참고
for _ in range(int(input())):
    print(sum(map(int,input().split())))

exec("print(sum(map(int,input().split())));"*int(input()))

exec('print(eval("+".join(input())));'*int(input()))
