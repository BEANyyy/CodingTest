# 최소 힙
import sys
import heapq
input = sys.stdin.readline

# 힙 생성
h = list()

# 연산의 개수 n 입력
n = int(input())

# 연산 입력 받기
for _ in range(n):
  cal = int(input())

  if cal == 0:
    if len(h) == 0:
      print(0)
    else:
      print(heapq.heappop(h))
  else:
      heapq.heappush(h, cal)

    


