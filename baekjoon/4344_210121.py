# 평균은 넘겠지

# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# for i in range(int(input())):
#     l=[*map(int,input().split())]
#     avg = (sum(l)-l[0])/l[0]
#     std = [value for i,value in enumerate(l) if i!=0 and value>avg] # l[0]은 점수가 아니기 때문에 제외
#     print(format(len(std)/l[0]*100, '.3f'),'%',sep='')


# 다른 풀이 참고
for _ in range(int(input())):
    # a는 학생수 b는 점수
    a,*b=map(int,input().split())
    s = len([i for i in b if i>sum(b)/a]) # 평균을 넘는 학생들의 수
    print("%.3f%%"%(s/a*100)) # %%은 Literal % (문자 % 자체)
