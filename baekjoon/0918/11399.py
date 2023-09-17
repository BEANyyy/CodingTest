# ATM
# 정렬 + 누적합

import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))
people.sort()

P = [0] * n

for i in range(n):
    for j in range(i+1):
        P[i] += people[j]
        
print(sum(P))