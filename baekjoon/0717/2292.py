# 차수가 6인 등차수열

def find_min_rooms(N):
    if N == 1:  # N이 1인 경우는 별도 처리
        return 1

    start = 2  # 벌집 숫자 시작 값
    count = 1  # 시작 방(1번 방)은 이미 포함되어 있으므로 1로 초기화
    increment = 6  # 벌집 숫자가 6씩 증가하는 패턴을 가짐

    while start <= N:
        start += increment
        increment += 6
        count += 1

    return count

# 사용자 입력 받기
N = int(input())
min_rooms = find_min_rooms(N)
print(min_rooms)
