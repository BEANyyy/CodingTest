# 파도반 수열
# 1 1 1 2 2 3 4 5 7 9
# P(n) = P(n-2) + P(n-3)

import sys
input = sys.stdin.readline

t = int(input())

def padovan(n):
  if n == 1 or n == 2 or n == 3:
    return 1
  else:
    return padovan(n-2) + padovan(n-3)
  
for i in range(t):
  n = int(input())
  print(padovan(n))





