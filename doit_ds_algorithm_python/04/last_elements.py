# 원하는 개수(n)만큼 값을 입력받아 마지막 n개를 저장

n = int(input('정수를 몇개 저장할까요>'))
a = [None] * n # 입력받은 값을 저장하는 배열

cnt = 0 # 정수를 입력받은 개수
while True:
    print('cnt%n',cnt%n)
    a[cnt % n] = int(input((f'{cnt +1}번째 정수를 입력하세요>')))
    cnt += 1

    retry = input(f'계속 할까요?(Y ... Yes / N ... No)>')
    if retry in {'N', 'n'}: # N이나 n을 입력하면 더 이상 값을 받지 않음
        break

i = cnt - n
if i < 0 : i = 0 # 배열 크기보다 입력받은 개수가 더 작은 경우

while i < cnt: # 마지막에 저장된 순서대로 출력
    print(f'{i + 1}번째 = {a[i % n]}')
    i += 1

