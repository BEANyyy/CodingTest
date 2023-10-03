# 15650 N과 M (2)
# 다른 코드를 참고하고 풀었느냐 : O
# 이분은 백트래킹 사용하셨음.

import sys
input = sys.stdin.readline

# input
n, m = map(int, input().split())

# 1. 1 ~ n까지 배열을 만들어서 저장 
arr = [i for i in range(0, n+1)]

index = 0

def backTracking(result):
    # 개수에 맞게 꽉 찼다면 결과 출력
    if len(result) == m:
        print(*result)
        return

    for i in range(1, n+1):
        if (i not in result) and (len(result)==0 or i > result[-1]):
            result.append(arr[i])
            # 재귀로 백트래킹 실행
            backTracking(result)
            # 재귀 끝난 뒤 빠져나와서 바로 직전에 담았던 것 제거하기
            result.pop()

backTracking([])