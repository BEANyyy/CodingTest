a, k = map(int, input().split())
count = 0

while 1:
    if a == k:
        print(count)
        break
    elif k % 2 == 0 and k >= a*2:
        k = k/2
    else:
        k -= 1
    count+=1

