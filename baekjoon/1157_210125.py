# 단어 공부

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

def solve(t: tuple) -> str:
    m=max(t)[0]
    cnt=0
    for i in t:
        if m == i[0]: cnt+=1
    if cnt>1: return '?'
    return max(t)[1]

a=input().upper();b={i for i in a};c=[]
for i in b:
    n=0
    for j in a:
        if i==j: n+=1
    c.append((n,i))
print(solve(c))

# 다른 풀이 참고
s,a=input().upper(),[]
for i in range(65,90+1):
    a.append(s.count(chr(i)))
print('?' if a.count(max(a))>1 else chr(a.index(max(a))+65))
