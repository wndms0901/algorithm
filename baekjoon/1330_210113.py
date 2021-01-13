# 두 수 비교하기

# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

# A가 B보다 큰 경우에는 '>'를 출력한다.
# A가 B보다 작은 경우에는 '<'를 출력한다.
# A와 B가 같은 경우에는 '=='를 출력한다.

# 제한 -10,000 ≤ A, B ≤ 10,000

a, b = map(int, input().split())

if a > b: print('>')
elif a < b: print('<')
else: print('==')
    
# 다른풀이 - 리스트 내포 사용
a, b = [int(n) for n in input().split()]
if a > b: print('>')
elif a < b: print('<')
else: print('==')
