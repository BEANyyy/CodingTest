import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list = list(map(int, input().strip().split()))


for _ in range(m):
  i, j = map(int, input().split())
  sum = 0
  for x in range(i, j+1): # i를 그대로 쓰면 초기화 됨. 
    # 다른 변수 이름으로 할당하고 범위를 지정해야 함.
    sum += list[x-1]

  print(sum)