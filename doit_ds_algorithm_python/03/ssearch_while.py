# 배열 검색 - 선형 검색 / 이진 검색 / 해시법
# 선형 검색 : 무작위로 늘어놓은 데어터 집합에서 검색을 수행
# 이진 검색 : 일정한 규칙으로 늘어놓은 데이터 집합에서 아주 빠른 검색을 수행
# 해시법    : 추가, 삭제가 자주 일어나는 데이터 집합에서 아주 빠른 검색을 수행

# while문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while 문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i # 검색 성공 (인덱스를 반환)
    return -1 # 검색 실패 (-1을 반환)

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요>')) # num값을 입력받음
    x = [None] * num # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색한 값을 입력하세요>')) # 검색할 키 ky를 입력받음

    idx = seq_search(x, ky) # ky와 값이 같은 원소를 x에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')


