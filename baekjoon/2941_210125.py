# 크로아티아 알파벳

# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
# 위 목록에 없는 알파벳은 한 글자씩 센다.

x=input()
a=x.count('c=')
b=x.count('c-')
c=x.count('dz=')
d=x.count('d-')
e=x.count('lj')
f=x.count('nj')
g=x.count('s=')
h=x.count('z=')
print(len(x)-(a+b+c+d+e+f+g+h))

# 다른 풀이 참고
a = input()
print(len(a)-sum(a.count(i) for i in ['-','=','lj','nj','dz=']))
