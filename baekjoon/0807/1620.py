# 포켓몬 마스터 이다솜 1620번

# Input
# 첫째 줄 : 도감에 수록되어 있는 포켓몬 개수 n, 맞춰야 하는 문제 개수 m
# 둘째 줄 : 1번~n번 포켓몬까지 한 줄에 하나씩 n개 입력됨.
#           포켓몬 이름은 모두 영어, 첫 글자만 대문자 나머지는 소문자.
#           *일부는 마지막 글자가 대문자
# 다음 줄 : 맞춰야 하는 문제 M줄

# Output
#           문제가 알파벳 = 번호, 숫자 = 문자 출력
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

# 도감
for i in range(n):
    dict[i] = input().rstrip()

dict_2 = {v:k for k,v in dict.items()}

# 문제
for j in range(m):
    prob = input().rstrip()
    # 자료형이 정수이면 해당 번째의 포켓몬 이름 출력
    if prob.isdigit():
        print(dict[int(prob)-1])
    # 자료형이 문자열이면 해당 포켓몬 이름에 해당하는 인덱스 번호 +1 출력
    else:
        print(dict_2[prob]+1)