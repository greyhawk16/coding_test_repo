# 위치: https://school.programmers.co.kr/learn/courses/30/lessons/250137

from collections import deque


def solution(bandage, health, attacks):
    ans = health    # 현재 체력
    que = deque()   # 공격 정보
    cool_time = bandage[0]   # 추가회복 쿨타임

    for i in range(len(attacks)):
        que.append(attacks[i])    # 공격 정보를 que에 담음
                                  # 공격이 있을 때마다, que의 맨 앞 요소를 pop 한다
        
    for i in range(1, attacks[-1][0] + 1):  # 공격이 끝나는 시각까지 체크
        # i: 현재 시각

        if que[0][0] == i:             # 현재 시각이 공격이 들어오는 시각일 경우
            x = que.popleft()          # 공격 정보 획득
            ans -= x[1]                # 현재 체력에서 공격력 x[1] 만큼 빼기
            cool_time = bandage[0]     # 쿨타임 초기화

            if ans <= 0:         # 체력이 0 이하가 되는 경우
                return -1        # -1 반환

        else:                          # 공격이 들어오지 않는 시각
            ans += bandage[1]          # 1초 마다 bandage[1]만큼 체력 회복
            cool_time -= 1             # 쿨타임 1초 감소

            if cool_time == 0:            # 쿨타임 다 찬 경우
                ans += bandage[2]         # 추가 회복량만큼 체력 회복
                cool_time = bandage[0]    # 쿨타임 초기화

            ans = min(ans, health)      # 현재 체력 ans는 주어진 최대 체력 health를 넘어갈 수 없음

    return ans     # 현재까지 남은 체력 반환