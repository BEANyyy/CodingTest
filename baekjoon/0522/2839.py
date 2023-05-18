n = int(input())
count = 0

#꼭 5를 먼저 뺄 필요가 없음.
while n >= 0:
  if n % 5 == 0:
    count += n // 5
    print(count)
    break
  
  n -= 3
  count += 1
  
else:
  print(-1)