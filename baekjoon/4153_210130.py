# 직각삼각형

# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

while True:
    l=[*map(int,input().split())]
    if sum(l)==0:break
    m=max(l);s=0
    for i in l:
        if i!=m:s+=i**2 
    if s==m**2:print('right')
    else:print('wrong')

# 다른 풀이
while True:
    l=[*map(int,input().split())]
    l.sort()
    if sum(l)==0:break
    if l[2]**2==l[0]**2+l[1]**2:print('right')
    else:print('wrong')
