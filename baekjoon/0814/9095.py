# 1, 2, 3 더하기

# n(1) = 1
# n(2) = 2
# n(3) = 4
# n(4) = 7
# n(5) = 13
# .
# .
# .

# = 피보나치랑 유사한데, 얘는 3개씩 더함.


n = int(input())

arr = [0] * 11
arr[1] = 1
arr[2] = 2
arr[3] = 4

# 1부터 10까지 수열에 맞는 값 입력하기
for i in range(4, 11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

# 정수 n 입력받고 출력
for j in range(n):
    num = int(input())
    print(arr[num])

