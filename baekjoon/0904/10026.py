# 10026번 적록색약

import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# input
n = int(input())
brd = [list(map(str, input().strip())) for _ in range(n)]


# bfs
# 안에 있는지
def inside(p, n):
    return 0 <= p[0] < n and 0 <= p[1] < n

# 움직일 방향 설정
offset = [[-1, 0],
          [0, 1],
          [1, 0],
          [0, -1]]

def bfs(x, y):
    start = [x, y]
    q = deque()
    q.append(start)
    vstd[start[0]][start[1]] = 1
    
    while q:
        cur = q.popleft()
        for d in range(4):
            p = [cur[0] + offset[d][0], cur[1] + offset[d][1]]
            if inside(p, n):
              if brd[p[0]][p[1]] == brd[cur[0]][cur[1]] and not vstd[p[0]][p[1]]:
                vstd[p[0]][p[1]] = 1
                q.append(p)


# not c-blind
# vstd 배열
vstd = [[0] * n for _ in range(n)]

ncb = 0
for i in range(n):
    for j in range(n):
        if not vstd[i][j]:
            bfs(i,j)
            ncb += 1


# c-blind
# vstd 배열
vstd = [[0] * n for _ in range(n)]

cb = 0

# R -> G
for i in range(n):
    for j in range(n):
        if brd[i][j] == 'R':
            brd[i][j] = 'G'
            
for i in range(n):
    for j in range(n):
        if not vstd[i][j]:
            bfs(i,j)
            cb += 1

print(ncb, cb)