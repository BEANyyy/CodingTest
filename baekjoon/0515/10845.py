#큐

import sys

n = int(sys.stdin.readline())
qu = []

for i in range (n):
  cm = sys.stdin.readline().split()

  if cm[0] == 'push':
    qu.insert(0, int(cm[1]))
  elif cm[0] == 'pop':
    if len(qu) > 0:
      print(qu[-1])
      qu.pop()
    else:
      print(-1)
  elif cm[0] == 'size':
    print(len(qu))
  elif cm[0] == 'empty':
    if len(qu) == 0:
      print(1)
    else:
      print(0)
  elif cm[0] == 'front':
    if len(qu) == 0:
      print(-1)
    else:
      print(qu[-1])
  elif cm[0] == 'back':
    if len(qu) == 0:
      print(-1)
    else:
      print(qu[0])
    