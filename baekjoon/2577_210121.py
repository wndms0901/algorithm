# 숫자의 개수

# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 
# 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.


def search(n,i):
    cnt=0
    for j in n:
        if i == j: cnt+=1
    return cnt

l=[int(input()) for i in range(3)]
n=l[0]*l[1]*l[2]
for i in range(10):
    print(search(str(n),str(i)))

# 다른 풀이 참고
n=1
for i in range(3):
    n*=int(input())
for i in range(10):
    print(str(n).count(str(i)))
