import sys
sys.setrecursionlimit(10**6)


#입력이 있을 때까지만 입력받기
nodes = []
while True:
  try:
    nodes.append(int(sys.stdin.readline()))
  except:
     break

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


postorder = postorder(nodes)

for node in postorder:
   print(node)