# 18870번 : 좌표 압축

# 1. 중복 제거
# 2. 오름차순 정렬
# 3. 정렬된 상태에서의 값에 해당하는 인덱스를 출력


import sys
input = sys.stdin.readline

# input
n = int(input())
arr = list(map(int, input().split()))

# 중복 제거 후 리스트형 변환
arr1 = list(set(arr))

# 오름차순 정렬
arr1.sort()

# 순서와 값을 저장할 딕셔너리
index = dict()
for i in range(len(arr1)):
    index[i] = arr1[i]

# 순서랑 값 바꿔서 저장 : 효율성을 위해서
index = {v:k for k,v in index.items()}

# 최종 출력 리스트
result = [0] * n
for i in range(n):
    result[i] = index.get(arr[i])

print(*result)

