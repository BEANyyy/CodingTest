# 15650 N과 M (2)
# 다른 코드를 참고하고 풀었느냐 : X

# nCm : 조합 수로 풀면 되는 것 같다
# 사전 순으로 증가하는 순서

import sys
input = sys.stdin.readline
from itertools import combinations

# input
n, m = map(int, input().split())

# 1. 1 ~ n까지 배열을 만들어서 저장 
arr = [0] * n
for i in range(n):
    arr[i] = i + 1

# 2. 조합 라이브러리를 활용하여 출력
for seq in combinations(arr, m):
    print(*seq)