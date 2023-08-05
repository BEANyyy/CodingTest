# 케빈 베이컨의 6단계 법칙

# Input
# 유저 수 n, 친구 관계 수 m
# 친구 관계가 m 줄 들어옴

# Output
# 케빈 베이컨의 수가 가장 작은 사람을 출력
#   = 각 유저 간의 거리의 합이 가장 작은 사람


n, m = map(int, input().split())

from collections import deque

#그래프 구성 : 딕셔너리로 인접노드 표현
g = {i: [] for i in range(1, n+1)}
for i in range(m):
    key, value = map(int, input().split())  #입력 받은 정수를 key, value로 각각 할당함.
    g[key].append(value)
    g[value].append(key)


def BFS(g, s, t): #start, target
    vstd = []
    q = deque([(s, 0)])  # 시작 노드 s와 단계 수를 큐 q에 넣기

    while q:
        u, steps = q.popleft() # 큐 q에서 가장 왼쪽의 노드를 꺼내서 u라는 변수에 할당. 가장 오래된 노드를 우선적으로 방문

        if u == t:        # 도착 노드에 도달하면
            return steps  # 단계 수 반환
        
        if u not in vstd: # u가 vstd에 없으면 vstd에 u를 추가
            vstd.append(u) 
            for neighbor in g[u]:
                q.append((neighbor, steps + 1))  # 인접 노드와 해당 단계 수를 함께 큐에 추가
    return -1 # 도착 노드까지 못 갔을 때

dist = [0] * n

for i in range(n):
    for j in range(n):
        dist[i] += BFS(g, i+1, j+1)

print(dist.index(min(dist))+1)
