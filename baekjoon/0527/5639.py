# ***시간 초과가 뜬다면 PyPy3로, 재귀를 사용하여 메모리 초과가 뜬다면 Python3***
# for문으로 바꾸려고 고민하다가 python3 쓰라는 말 듣고 수정해서 제출했더니 성공 ^___^;

import sys
#RecursionError 수정
sys.setrecursionlimit(100000)

#입력이 있을 때까지만 입력받기
nodes = []
# while True:
#   try:
#     nodes.append(int(sys.stdin.readline()))
#   except:
#      break

#ValueError 수정
while True:
    node = sys.stdin.readline().strip()  # 개행 문자 제거
    if not node:  # 빈 문자열인 경우 입력 종료
        break
    nodes.append(int(node))


def postorder(preorder):
    if not preorder:  # 빈 리스트인 경우
        return []

    root = preorder[0]  # 전위 순회 결과의 첫 번째 값은 루트
    left_subtree = []  # 왼쪽 서브트리의 전위 순회 결과
    right_subtree = []  # 오른쪽 서브트리의 전위 순회 결과

    for i in range(1, len(preorder)):
        if preorder[i] < root:
            left_subtree.append(preorder[i])  # 루트보다 작은 값은 왼쪽 서브트리에 추가
        else:
            right_subtree.append(preorder[i])  # 루트보다 크거나 같은 값은 오른쪽 서브트리에 추가

    # 왼쪽 서브트리, 오른쪽 서브트리를 재귀적으로 후위 순회한 결과를 구함
    left_postorder = postorder(left_subtree)
    right_postorder = postorder(right_subtree)

    # 후위 순회 결과를 반환 (왼쪽 서브트리, 오른쪽 서브트리, 루트 순서)
    return left_postorder + right_postorder + [root]


result = postorder(nodes)

for node in result:
   print(node)