# 동전의 합 k
# 그리디 알고리즘

n, k = map(int, input().split())

coins = [0] * n
count = 0

for i in range(n):
    coins[i] = int(input())

# while k > 0 이랑 if k > coins[i]를 쓰면 틀렸다고 함.
for i in reversed(range(n)):
    count += k // coins[i]
    k = k % coins[i]
          

print(count)