# 그룹 단어 체커

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 
# 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

def solve(a: str):
    for i in range(len(a)-1):
        if a[i]!=a[i+1]: 
            b=a[i+1:]
            if b.count(a[i]) > 0: return False
    return True
cnt=0
for i in range(int(input())):
    if solve(input()): cnt+=1
print(cnt) 


# 다른 풀이 참고
a = 0
for i in range(int(input())):
    s = input()
    a+=list(s) == sorted(s, key=s.find) # sorted에서 key=s.find로 설정하면 알파벳 순 정렬이 아니라 
                                        # s에서 찾아지는 문자 순서대로 정렬됨
print(a)
