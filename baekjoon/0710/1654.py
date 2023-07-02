k, n = map(int, input().split())

arr = []

for _ in range(k):
    i = int(input())
    arr.append(i)

# 이분탐색 렛츠고

start = 1
end = max(arr)

while (start <= end):
    mid = (start + end) // 2
    sum = 0
    for i in range(k):
        sum += arr[i] // mid
    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)