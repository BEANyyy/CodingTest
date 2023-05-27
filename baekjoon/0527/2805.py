import sys

n, m = map(int, sys.stdin.readline().split())           # 나무의 수 n, 필요한 길이 m
trees = list(map(int, sys.stdin.readline().split()))    # 나무 높이들
# 나무 높이의 중간값 계산하기 : 약간 이진탐색처럼 시도해보자
min_height, max_height = 0, max(trees)

# 나무 자르기
while min_height <= max_height:
  h = (min_height + max_height) // 2

  total = 0
  for tree in trees:
      if tree >= h:
        total += tree-h

  if total < m:
    max_height = h - 1
  else:
    min_height = h + 1
  
print(max_height)

