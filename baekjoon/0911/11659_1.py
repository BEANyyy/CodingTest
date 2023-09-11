import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pfs = list(map(int,input().split()))

for i in range(n-1):
    pfs[i+1] += pfs[i]
#print(pfs)
pfs = [0] + pfs
#print(pfs)

for _ in range(m):
    a,b = map(int,input().split())
    print(pfs[b]-pfs[a-1])