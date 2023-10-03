# 1931번 : 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
arr = [()] * n

for i in range(n):
    start, end = map(int, input().split())
    arr[i] = [start, end]

# 시작시간, 마치는 시간 순으로 정렬한 배열로 그리디
arr = sorted(arr, key=lambda a: a[0])
arr = sorted(arr, key=lambda a: a[1])

# 마지막 시간 저장
end_time = arr[0][1]

# 개수 저장
result = 1 # 0이 아닌 이유 : 마지막 시간을 저장하고 시작하기 때문에

for i in range(1, n):   # for문도 1부터 시작하게 해야함.
    if arr[i][0] >= end_time:
        result += 1
        end_time = arr[i][1]

print(result)