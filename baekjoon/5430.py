from collections import deque

t = int(input())

for _ in range(t):
  p = input()
  n = int(int(input()))
  arr = input()[1:-1].split(',')

  qu = deque(arr)

  flag = 0

  if n == 0:
    qu = []

  for i in p:
    if i == 'R':
      flag+=1
    elif i == 'D':
      if len(qu) == 0:
        print("error")
        break
      else:
        if flag % 2 == 0:
          qu.popleft()
        else:
          qu.pop()
  else:
    if flag % 2 == 0:
      print("[" + ",".join(qu) + "]")
    else:
      qu.reverse()
      print("[" + ",".join(qu) + "]")

