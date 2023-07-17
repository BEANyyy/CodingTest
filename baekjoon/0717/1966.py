from collections import deque

def find_print_order(N, M, priorities):
    # 큐에 문서와 인덱스를 함께 저장 : 중요도랑 인덱스를 (인덱스, 중요도) 튜플로 구성
    # enumerate(priorities) : priorities 리스트의 각 요소에 대해 인덱스와 값을 가져옴.
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0 # 몇 번째로 인쇄되는지 카운트되는 변수
    # 결과를 저장하는 배열
    result = []

    while queue:
        front = queue.popleft()
        # 현재 문서의 중요도보다 큰 중요도를 가진 문서가 있는지 확인
        if any(front[1] < q[1] for q in queue):
            queue.append(front)
        else: # 없으면
            count += 1
            # 궁금한 문서가 출력되었을 때의 count 값을 반환
            if front[0] == M:
                result.append(count)

    return result

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # 문서의 개수와 궁금한 문서의 인덱스 n, m
    N, M = map(int, input().split())
    # 문서의 중요도 입력받기
    priorities = list(map(int, input().split()))
    # 문서의 출력 순서를 출력 : 배열 값을 하나씩 출력하려면 *를 사용할 수 있음.
    print(*find_print_order(N, M, priorities))
