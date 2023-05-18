#세로 n, 가로 m, 인벤토리 블록 수 b 입력받기
ipt = input().split(' ')
ipt = [int(x) for x in ipt]   #자료형 정수로

n = ipt[0]
m = ipt[1]
b = ipt[2]

#파이썬은 1초에 2000만번 정도 연산이 가능하다곤 하는데
#여러 요인에 따라 다를 것 같아서 넉넉잡아 10억으로 초기 시간 설정
min_time = 1e9

#최종 높이 초기화
height = 0

#집터 구성
brd = [list(map(int, input().split())) for _ in range(n)]

#꼼수 부릴랬는데 그냥 다 확인하는 게 브루트포스 알고리즘(완전탐색)이라는 걸 깨달음.
#0층~256층까지 반복
for flr in range(257):
    pls, mns = 0, 0

    #brd 확인
    for i in range(n):
        for j in range(m):
            #블록이 현재 층수 flr 보다 크면
            if brd[i][j] >= flr:
                pls += brd[i][j] - flr
            else:
                #블록이 현재 층수 flr 보다 작으면
                mns += flr - brd[i][j]

    #원래 가지던 블록이 충분한지 확인
    if pls + b >= mns:
        #최저 시간 계산 : pls - 1, mns - 2
        tm = mns + (pls * 2)
        if tm <= min_time:
            min_time = tm #최저 시간 대입
            height = flr  #현재 층수 대입

print(min_time, height)