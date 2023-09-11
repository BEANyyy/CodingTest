# 파도반 수열
# 1 1 1 2 2 3 4 5 7 9
# P(n) = P(n-2) + P(n-3)

import sys
input = sys.stdin.readline

t = int(input())

arr = [0] * 101
arr[1] = 1
arr[2] = 1
arr[3] = 1

for i in range(4, 101):
  arr[i] = arr[i-2] + arr[i-3]

for i in range(t):
  n = int(input())
  print(arr[n])





