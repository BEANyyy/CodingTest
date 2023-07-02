# 입력 받기
l = int(input())
string = list(input())

# 해시 함수 만들기
r = 31
m = 1234567891

def hashing(arr):
    func_number = 0
    for i in range(l):
        func_number += (ord(arr[i])-96) * (r ** i)
  
    return func_number

print(hashing(string) % m)
