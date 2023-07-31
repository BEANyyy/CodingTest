#n을 입력 받아 1이 될 때까지의 최소 연산 수를 구하는 문제

n = int(input())

def make_one(n):
    arr = [0] * (n + 1)

    for i in range(2, n + 1):
      arr[i] = arr[i - 1] + 1 # 1을 뺀 경우

      if i % 3 == 0:
          arr[i] = min(arr[i], arr[i // 3] + 1)

      if i % 2 == 0: # elif로 하면 모든 조건을 검사하지 않으니까 if로만 적어야함.
          arr[i] = min(arr[i], arr[i // 2] + 1)
    
    return arr[n]

print(make_one(n))