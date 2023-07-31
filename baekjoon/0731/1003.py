# 피보나치 함수에서 0과 1을 각각 몇 번 리턴했는지 개수를 세는 문제
# 재귀로 하면 시간초과라서 다이나믹 프로그래밍 기법을 활용하였음.
# 0 호출 횟수 수열과 1 호출 횟수 수열이 n이 2 이상일 때부터 같은 패턴이라는 점을 이용
# T : 테스트 케이스 개수
T = int(input())

#N : 40보다 작거나 같은 자연수 또는 0
for _ in range(T):
    n = int(input())
    # 0과 1이 출력되는 횟수를 저장할 배열
    count = [1, 0]
    for i in range(n):
      count[0], count[1] = count[1], count[0] + count[1]
    print(count[0], count[1])


