# 웜 바이러스에 감염된 컴퓨터 수
# 그냥 그래프가 연결된 노드 수를 구하는 것 같음

from collections import deque

n = int(input())
k = int(input())

#그래프 구성 : 딕셔너리로 인접노드 표현
g = {i: [] for i in range(1, n+1)}
for i in range(k):
    key, value = map(int, input().split())  #입력 받은 정수를 key, value로 각각 할당함.
    g[key].append(value)
    g[value].append(key)

def BFS(g, s):
    vstd = []
    q = deque([s])  # 시작 노드 s를 큐 q에 넣기

    while q:
        u = q.popleft() # 큐 q에서 가장 왼쪽의 노드를 꺼내서 u라는 변수에 할당. 가장 오래된 노드를 우선적으로 방문
        if u not in vstd: # u가 vstd에 없으면 vstd에 u를 추가
            vstd.append(u) 
            q.extend(g[u])  # u의 인접 노드들을 큐 q에 추가. q : 다음에 방문할 노드 저장
    return len(vstd) -1 # 1도 들어가니까 빼기

print(BFS(g, 1))