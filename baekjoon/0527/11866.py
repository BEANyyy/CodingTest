import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())           # 사람 수 n, 제거할 사람 k
q = deque([])

# front = 0
# rear = n
# 원래는 원형 큐로 구현해 보려고 했는데.. 너무 귀찮아서..

for i in range(n):
    q.append(i+1)

print('<', end="")

while q:
  for i in range(k-1):
     q.append(q[0])
     q.popleft()
  print(q.popleft(), end="")
  if q:
     print(", ", end="")    # 띄어쓰기를 잘 붙이자!

print(">")
