from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력 받기
n, m = map(int, input().split())
campus = []

# 캠퍼스 구성
for _ in range(n):
    campus.append(list(input().strip()))

# 시작 위치 = 도연이(I)
for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            start = [i, j]

# 캠퍼스 안 조건 설정
def inside(p, n, m):
    return 0 <= p[0] < n and 0 <= p[1] < m

# 움직일 방향 설정
offset = [[-1, 0],
          [0, 1],
          [1, 0],
          [0, -1]]

def bfs(campus, start, n, m):
    cnt = 0
    vstd = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([start])
    vstd[start[0]][start[1]] = 1
    
    while q:
        cur = q.popleft()
        for d in range(4):
            p = [cur[0] + offset[d][0], cur[1] + offset[d][1]]
            if inside(p, n, m) and not vstd[p[0]][p[1]]:
                if campus[p[0]][p[1]] == 'P':
                    cnt += 1
                if campus[p[0]][p[1]] != 'X':
                    vstd[p[0]][p[1]] = 1
                    q.append(p)
                    
    return cnt



cnt = bfs(campus, start, n, m)

if cnt == 0:
    print("TT")
else:
    print(cnt)
