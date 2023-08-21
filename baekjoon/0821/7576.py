# 이미 익은 토마토 =>> 하루가 지나면 이 토마토의  상하좌우에 있는 토마토들이 익음
# 언제 모든 토마토가 익을 것인가~

from collections import deque
import sys
input = sys.stdin.readline

# 입력 받기
m, n = map(int, input().split())
brd = []
res = 0

# 상자 구성 
for _ in range(n):
    row = list(map(int, input().split()))
    brd.append(row)

# 시작 위치 = 익은 토마토(1)
q = deque([])

# bfs에서 쓸 q(=익은 토마토의 위치가 담긴 배열)을 선언.
for i in range(n):
    for j in range(m):
        if brd[i][j] == 1:
            start = [i, j]
            q.append(start)

# 박스 안 조건 설정
def inside(p, n, m):
    return 0 <= p[0] < n and 0 <= p[1] < m

# 움직일 방향 설정
offset = [[-1, 0],
          [0, 1],
          [1, 0],
          [0, -1]]

# bfs (dfs는 안됨.)
def bfs(brd, n, m):
    while q:
        cur = q.popleft() # q 안에 있는 첫 번째 익은 토마토 좌표를 pop
        # 상하좌우 이동하며 익힐 토마토(0) 찾기
        for d in range(4):
            p = [cur[0] + offset[d][0], cur[1] + offset[d][1]]
            # brd 안에 있고, 덜 익은 토마토(0)일 때를 조건으로
            if inside(p, n, m) and brd[p[0]][p[1]] == 0:
                # 익히고 1을 더해서 이 토마토가 총 몇 번 익혀졌는지 횟수를 세기
                # 익힌 횟수의 최댓값이 정답
                brd[p[0]][p[1]] = brd[cur[0]][cur[1]] + 1
                q.append(p)

bfs(brd, n, m)

for i in brd:
    for j in i:
        # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔다면 최댓값이 정답
    res = max(res, max(i))

# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res - 1)
