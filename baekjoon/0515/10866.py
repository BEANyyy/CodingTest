#덱

import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()

for i in range (n):
  cm = sys.stdin.readline().split()

  if cm[0] == 'push_front':
    deq.insert(0, int(cm[1]))
  elif cm[0] == 'push_back':
    deq.append(int(cm[1]))
  elif cm[0] == 'pop_front':
    if len(deq) > 0:
      print(deq.popleft())
    else:
      print(-1)
  elif cm[0] == 'pop_back':
    if len(deq) > 0:
      print(deq.pop())
    else:
      print(-1)
  elif cm[0] == 'size':
    print(len(deq))
  elif cm[0] == 'empty':
    if len(deq) == 0:
      print(1)
    else:
      print(0)
  elif cm[0] == 'front':
    if len(deq) == 0:
      print(-1)
    else:
      print(deq[0])
  elif cm[0] == 'back':
    if len(deq) == 0:
      print(-1)
    else:
      print(deq[-1])
    