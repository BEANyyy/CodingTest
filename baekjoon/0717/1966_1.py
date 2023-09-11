#테스트 케이스 개수
t = int(input()) 
arr = []

for _ in range(t):
  #n, m : 현재 테스트 케이스의 문서 개수, 궁금 문서의 인덱스
  n, m = map(int, input().split())

  # (인덱스, 중요도) 형태의 튜플을 가지는 리스트 arr에 저장
  arr = list(enumerate(list(map(int, input().split()))))

  # v : 궁금한 문서의 (인덱스, 중요도) 튜플이 할당
  v = arr[m]
  idx = 0 # 몇 번째로 인쇄되는지 카운트하는 변수

  while len(arr):
    max_v = max([i[1] for i in arr])  # 중요도가 가장 큰 값을 찾아 max_v에 할당
    
    if arr[0][1] == max_v:
      now = arr.pop(0)
      idx += 1
      if now == v:
        print(idx)
        break
    else: # 중요도가 가장 큰 문서가 아닌 경우
      now = arr.pop(0)
      arr.append(now) # arr의 끝에 추가하고 다음 문서를 처리하기 위해 반복문을 계속