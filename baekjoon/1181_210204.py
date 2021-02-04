# 단어 정렬

# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

import sys
l=[]
for _ in range(int(input())):
    t=sys.stdin.readline()
    l.append((len(t)-1,t[:len(t)-1]))
l=list(set(l))
l.sort()
for i in range(len(l)):
    print(l[i][1])
