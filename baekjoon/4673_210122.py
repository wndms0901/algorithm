# 셀프 넘버

# 셀프 넘버는 1949년 인도 수학자 D.R. Kaprekar가 이름 붙였다. 
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자. 
# 예를 들어, d(75) = 75+7+5 = 87이다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다. 
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def solve():
    n=1;s=set()
    while n<=10000:
        l=[int(i) for i in str(n)]
        value=sum(l,n)
        s.add(value)
        n+=1
    return s

l=set(range(1,10000+1))
s=solve()
t=list(l-s)
t.sort()
print(*t, sep='\n') 
