# n, m 내의 미로찾기 + 만날 수 있는 사람 수
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())

# campus 구성하기
campus = []

# 시작 위치 = 도연이(I)
for i in range(n):
  campus[i] = list(input())
  for j in range(len(campus[i])):
        if campus[i][j] == "I":
            cur = [i, j]            

# campus 탐색하기
def inside(p):  # p = (i, j)
    return 0 <= p[0] < n and 0 <= p[1] < m

offset = [[-1, 0],
          [0, 1],
          [1, 0],
          [0, -1]]

def move(p, d):
    p[0] += offset[d][0]
    p[1] += offset[d][1]
    return p

cnt = 0
vstd = [[0 for j in range(m)] for i in range(n)]
    
def DFS(cur):   # g(그래프), s(시작 노드), vstd(방문한 노드 리스트)
    global cnt
    if inside(cur) and not vstd[cur[0]][cur[1]]:
        vstd[cur[0]][cur[1]] = 1
        if campus[cur[0]][cur[1]] == 'P':
            cnt += 1
        for d in range(4):
            p = cur.copy()
            p = move(p, d)
            if inside(p) and not vstd[p[0]][p[1]]:
              if campus[p[0]][p[1]] != 'X':
                  DFS(p)
    return cnt
                
cnt = DFS(cur)

if cnt == 0:
    print("TT")
else:
    print(cnt)