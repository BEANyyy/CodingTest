import sys
input = sys.stdin.readline

S = set()
n = int(input())

for _ in range(n):
  text = input().strip().split()
  func = text[0]

  if func == 'add':
    x = int(text[1])
    S.add(x)

  elif func == 'check':
    x = int(text[1])
    if x in S:
      print(1)
    else:
      print(0)

  elif func == 'remove':
    x = int(text[1])
    S.discard(x)

  elif func == 'toggle':
    x = int(text[1])
    if x in S:
      S.discard(x)
    else:
      S.add(x)
  elif func == 'all':
    S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
  elif func == 'empty':
    S= set()




