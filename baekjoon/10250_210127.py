# ACM 호텔

# 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성하고자 한다.
# 호텔은 직사각형 모양이라고 가정하자. 각 층에 W 개의 방이 있는 H 층 건물이라고 가정하자 (1 ≤ H, W ≤ 99).
# 그리고 엘리베이터는 가장 왼쪽에 있다고 가정하자(그림 1 참고). 이런 형태의 호텔을 
# H × W 형태 호텔이라고 부른다. 호텔 정문은 일층 엘리베이터 바로 앞에 있는데, 
# 정문에서 엘리베이터까지의 거리는 무시한다. 또 모든 인접한 두 방 사이의 거리는 같은 거리(거리 1)라고 
# 가정하고 호텔의 정면 쪽에만 방이 있다고 가정한다.
# 초기에 모든 방이 비어있다고 가정하에 이 정책에 따라 N 번째로 도착한 손님에게 배정될 방 번호를 계산
for _ in range(int(input())):
    a=0;b=1 # a: 층 수 b: 방 수
    h,w,n=map(int,input().split()) # h: 호텔의 층 수 w: 각 층의 방수 n: 몇번 째 손님
    for _ in range(1,n+1):
        if a>=h: a=1;b+=1
        else: a+=1
    print(f'{a}{b:02}')