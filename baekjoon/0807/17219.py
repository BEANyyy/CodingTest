# 비밀번호 찾기

# Input
# 첫 줄 : 사이트 주소의 수 n, 찾으려는 사이트 주소 m
# 사이트 주소 / 비밀번호 n줄
# 찾으려는 사이트 주소 m줄

# Output
# m개의 사이트 주소에 해당하는 비밀번호

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

# 사이트 주소와 비밀번호
for _ in range(n):
    key, value = map(str, input().split())
    dict[key] = value


# 문제
for j in range(m):
    prob = input().rstrip()
    # 사이트 값을 받아 비밀번호 출력
    print(dict[prob])