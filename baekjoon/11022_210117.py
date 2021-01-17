# A + B -8

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

for i in range(int(input())):
    lst = input().split()
    print(f'Case #{i+1}: {lst[0]} + {lst[1]} = {sum(map(int,lst))}')


# 다른 풀이 참고
a=int(input())
for i in range(1,a+1):
 a,b=map(int,input().split())
 print(f"Case #{i}: {a} + {b} = {a+b}")
 