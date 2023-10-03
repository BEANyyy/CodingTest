# 12851 : 숨바꼭질 2


import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())

# 좌표 구성
end = 100000  # 100001로 하면 bfs에서 문제가 생김.. 바봡보바보바보바보
vstd = [0] * (end+1)

# 필요한 변수 선언
time = 0
way = 0

# bfs
def bfs(time, way):
    q = deque([n])  # 시작 위치 = 수빈 n
    
    while q:
        x = q.popleft()
        if x == k: # 도달했을 때
          time = vstd[x]
          way += 1
          continue  # break 안됨

        # -1, 1, *2 이동하며 k 좌표 찾기
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= end and (not vstd[nx] or vstd[nx] == vstd[x] + 1):
                vstd[nx] = vstd[x] + 1
                q.append(nx)

    print(time)
    print(way)   
     
bfs(time, way)
