# 2630 색종이 만들기

import sys

input = sys.stdin.readline

#  input
n = int(input())
brd = [list(map(int, input().split())) for _ in range(n)]

# initialize
w = 0
b = 0

# cut and count function
def cut_and_count(x, y, n):
  global w, b
  cur_color = brd[x][y]
  for i in range(x, x + n):
    for j in range(y, y + n):
      if cur_color != brd[i][j]:
        cut_and_count(x, y, n//2)
        cut_and_count(x, y+n//2, n//2)
        cut_and_count(x+n//2, y, n//2)
        cut_and_count(x+n//2, y+n//2, n//2)

        return 
      
  if cur_color == 0:
    w += 1
  else:
    b += 1

cut_and_count(0, 0, n)
print(w)
print(b)


