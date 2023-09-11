def construct_postorder(preorder, start, end):
    if start > end:
        return

    root = preorder[start]  # 전위 순회 결과의 첫 번째 값은 루트
    index = start + 1

    while index <= end and preorder[index] < root:
        index += 1

    # 왼쪽 서브트리 재귀적으로 후위 순회
    construct_postorder(preorder, start + 1, index - 1)

    # 오른쪽 서브트리 재귀적으로 후위 순회
    construct_postorder(preorder, index, end)

    # 현재 노드 출력 (후위 순서)
    print(root)


# 입력 받기def construct_postorder(preorder, start, end):
    if start > end:
        return

    root = preorder[start]  # 전위 순회 결과의 첫 번째 값은 루트
    index = start + 1

    while index <= end and preorder[index] < root:
        index += 1

    # 왼쪽 서브트리 재귀적으로 후위 순회
    construct_postorder(preorder, start + 1, index - 1)

    # 오른쪽 서브트리 재귀적으로 후위 순회
    construct_postorder(preorder, index, end)

    # 현재 노드 출력 (후위 순서)
    print(root)


# 입력 받기
preorder = []
while True:
    node = input()
    if node == '':
        break
    preorder.append(int(node))

# 후위 순회 결과 출력
construct_postorder(preorder, 0, len(preorder) - 1)

preorder = []
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

# 후위 순회 결과 출력
construct_postorder(preorder, 0, len(preorder) - 1)
