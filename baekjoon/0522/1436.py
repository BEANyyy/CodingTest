#n 입력받기
n = int(input())

#666숫자 정의
#어쨌든 666이 들어가는 수 중에 가장 작은 수부터 세면 됨

num = 0
arr = []
for i in range(2666800):
    if len(arr) == 10000:
        #print(i)     #어디까지 넣어야 n이 10000이 되는지 궁금해서 해봄.
        break
    else:
        if '666' in str(num):
          arr.append(num)
    num+=1

print(arr[n-1])
