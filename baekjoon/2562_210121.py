# 최댓값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
# 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

a=[]
for _ in range(9): a.append(int(input()))
m=max(a)
for i in range(9):
    if m == a[i]: idx = i
print(m)
print(idx+1)
    
# 다른 풀이 참고1
l=[int(input())for i in range(9)]
print(max(l),l.index(max(l))+1)

# 다른 풀이 참고2
print(*max((int(input()), i+1) for i in range(9))) 

a = max(((int(input()), i+1) for i in range(9))) # 위 코드 참고
print(*a)
