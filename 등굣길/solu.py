# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42898


def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]   # 0으로 padding 추가 -> 경계 벗어날 우려 예방, puddles의 좌표 그대로 사용가능
    dp[1][1] = 1   # dp 탐색 시작 위치
        
    for i in range(1, n+1):         # 행 방향
        for j in range(1, m+1):     # 열 방향
            if ([j, i] in puddles) or (i == 1 and j == 1):  # 웅덩이거나, 시작위치라면 -> 무시
                continue
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD  # 경우의 수 계산
    
    ans = dp[-1][-1]
    return ans


# m = 4
# n = 3
# puddles = [[2, 2]]
# print(solution(m, n, puddles))