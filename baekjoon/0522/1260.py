#n, m, v
n, m, v = map(int, input().split())  #자료형 정수로

#그래프 구성 : 딕셔너리로 인접노드 표현
g = {i: [] for i in range(1, n+1)}
for i in range(m):
    key, value = map(int, input().split())
    g[key].append(value)
    g[value].append(key)

for key, value in g.items():
    g[key] = sorted(value)


def DFS(g, s, vstd=None):
    if vstd is None:
        vstd = []
    if s in vstd:
        return vstd
    vstd.append(s)
    for u in g[s]:
        vstd = DFS(g, u, vstd)
    return vstd

#bfs
from collections import deque

def BFS(g, s):
    vstd = []
    q = deque([s])

    while q:
        u = q.popleft()
        if u not in vstd:
            vstd.append(u)
            q.extend(g[u])
    return vstd

print(' '.join(list(map(str, DFS(g, v)))))
print(' '.join(list(map(str, BFS(g, v)))))