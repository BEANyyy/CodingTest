import sys
input = sys.stdin.readline

S = set()
n = int(input())

for _ in range(n):
  text = input().strip().split()
  func = text[0]

  if len(text) == 1:
    if func == 'all':
      S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif func == 'empty':
      S= set()
    continue
  
  x = int(text[1])

  if func == 'add':
    S.add(x)
  elif func == 'check':
    if x in S:
      print(1)
    else:
      print(0)

  elif func == 'remove':
    S.discard(x)

  elif func == 'toggle':
    if x in S:
      S.discard(x)
    else:
      S.add(x)
  




