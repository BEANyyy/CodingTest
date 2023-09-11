# 11724번 : 연결 요소의 개수
# 무방향 그래프의 연결 요소 개수를 구하는 프로그램

from collections import deque

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

#그래프 구성 : 딕셔너리로 인접노드 표현
g = {i: [] for i in range(1, n+1)}

# 그래프 입력
for i in range(m):
    key, value = map(int, input().split())  #입력 받은 정수를 key, value로 각각 할당함.
    g[key].append(value)
    g[value].append(key)

keys = list(g.keys())

def BFS(g, s):
    vstd = []
    q = deque([s])  # 시작 노드 s를 큐 q에 넣기

    while q:
        u = q.popleft() # 큐 q에서 가장 왼쪽의 노드를 꺼내서 u라는 변수에 할당. 가장 오래된 노드를 우선적으로 방문
        if u not in vstd: # u가 vstd에 없으면 vstd에 u를 추가
            vstd.append(u) 
            q.extend(g[u])  # u의 인접 노드들을 큐 q에 추가. q : 다음에 방문할 노드 저장
    return vstd


count = 0 # count 변수를 0으로 초기화
while keys: # key 값이 비어있지 않은 경우
    a = BFS(g, keys[0]) # BFS 탐색
    count += 1  # 탐색 후 count 변수를 +1
    keys = [x for x in keys if x not in a]  # 기존 key 배열에서 BFS로 반환된 vstd 안의 노드들을 제외하여 업데이트
    

print(count)

