# 1이 있는 위치를 받아 블롭수를 세는 문제
import sys

sys.setrecursionlimit(10000)

def count_blobs(grid):
      def dfs(x, y):
          # 그리드 범위 안에서 0이 아닌 셀(1인 셀)을 탐색
          if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
              return
          
          # dfs
          grid[x][y] = 0 # 방문하면 0
          dfs(x + 1, y)  # 이웃 셀 방문 : 상하좌우(대각선은 아님)
          dfs(x - 1, y)
          dfs(x, y + 1)
          dfs(x, y - 1)

      count = 0 # 블롭수 저장
      for i in range(len(grid)):
          for j in range(len(grid[0])):
              if grid[i][j] == 1:
                  count += 1
                  dfs(i, j)

      return count


T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  grid = [[0 for _ in range(M)] for _ in range(N)]

  for _ in range(K):
      x, y = map(int, input().split())
      grid[y][x] = 1
  
  result = count_blobs(grid)
  print(result)
