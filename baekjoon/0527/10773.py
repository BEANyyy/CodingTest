import sys

k = int(sys.stdin.readline())

total = 0
arr = []
for _ in range(k):
    count = 0
    n = int(sys.stdin.readline())
    if n != 0:
        arr.append(n)
        count += 1
    else:
        arr.pop(count-1)

print(sum(arr))