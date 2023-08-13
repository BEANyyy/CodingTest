# 듣보잡


n, m = map(int, input().split())

lis = [0] * n
see = [0] * m

for i in range(n):
    lis[i] = input()


for j in range(m):
    see[j] = input()

lis_see = list(set(lis) & set(see))
lis_see.sort()  # 사전순 정렬

print(len(lis_see))

for k in range(len(lis_see)):
    print(lis_see[k])

    