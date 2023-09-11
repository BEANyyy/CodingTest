import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

brd = [list(map(int, input().split())) for _ in range(n)]

# 목표 지점
for i in range(n):
    for j in range(m):
        if brd[i][j] == 2:
            start = [i, j]

# 박스 안 조건 설정
def inside(p, n, m):
    return 0 <= p[0] < n and 0 <= p[1] < m

# 움직일 방향 설정
offset = [[-1, 0],
          [0, 1],
          [1, 0],
          [0, -1]]

vstd = [[-1] * m for _ in range(n)]

# bfs
def bfs(start):    
    vstd[start[0]][start[1]] = 0
    q = deque([start])  # 시작 노드 s를 큐 q에 넣기

    while q:
        cur = q.popleft()
        for d in range(4):
            p = [cur[0] + offset[d][0], cur[1] + offset[d][1]]

            if inside(p, n, m) and vstd[p[0]][p[1]] == -1:
                if brd[p[0]][p[1]] == 0: 
                    vstd[p[0]][p[1]] = 0
                elif brd[p[0]][p[1]] == 1:
                    vstd[p[0]][p[1]] = vstd[cur[0]][cur[1]] + 1
                    q.append(p)
        
for i in range(n):
  for j in range(m):
      if brd[i][j] ==2 and vstd[i][j] == -1:
        bfs((i, j))

# 제출 형식 맞추기, 문제 대충 보지 말고 -1 챙기기
for i in range(n):
  for j in range(m):
      if brd[i][j] == 0:
          print(0, end=' ')
      else:
          print(vstd[i][j], end=' ')
  print()

