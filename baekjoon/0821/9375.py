# 해빈이가 가진 의상으로 만들 수 있는 조합의 수

# 테스트 케이스의 수
t = int(input())

# 테스트 케이스 수만큼 반복
for i in range(t):
  # 딕셔너리로 종류를 구분하여 옷 저장
  closet = dict()

  # 해빈이가 가진 의상의 수
  n = int(input())

  for j in range(n):    
    # 옷장 구성
    value, key = input().split()  #입력 받은 정수를 key, value로 각각 할당함
    
    # 딕셔너리에 해당 키가 없을 경우 집합으로 만들어주고 추가
    if closet.get(key) == None:
      closet[key] = set()
    closet[key].add(value)
    
  # 조합 계산 (indent 때문에 오답처리 된 거였음)
  result = 1
  # 딕셔너리의 각 key에 대한 값의 길이를 result에 1을 더해 곱하기
  for key in closet.keys():
    result *= len(closet[key]) +1    
  print(result-1)
