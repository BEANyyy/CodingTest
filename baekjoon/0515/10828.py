#스택

import sys

n = int(sys.stdin.readline()) #input은 시간초과라서 sys 활용
st = []

for i in range (n):
  cm = sys.stdin.readline().split()

  if cm[0] == 'push':
    st.append(int(cm[1]))
  elif cm[0] == 'top':
    if len(st) == 0:
      print(-1)
    else:
      print(st[-1])
  elif cm[0] == 'size':
    print(len(st))
  elif cm[0] == 'empty':
    if len(st) == 0:
      print(1)
    else:
      print(0)
  elif cm[0] == 'pop':
    if len(st) > 0:
      print(st[-1])
      st.pop(-1)
    else:
      print(-1)