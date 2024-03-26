"""
    - 문제 위치: https://school.programmers.co.kr/learn/courses/30/lessons/178870
    - 참고 풀이: https://velog.io/@sugyeonghh/프로그래머스-연속된-부분-수열의-합Python 
"""


def solution(sequence, k):
    ans = []
    l, r = 0, 0
    n = len(sequence)
    tmp = sequence[0]
    
    while l <= r and r <= n :
        # 1) 부분합 < 목표값인 경우
        if tmp < k:
            r += 1        # 우측 경계를 오른쪽으로 한칸 이동
            if r == n:      # 부분 수열이 끝에 도달하면
                break       # 탐색 종료
            else:           
                tmp += sequence[r]  # sequence[r] 만큼 부분합에 더해주기
        # 2) 부분합 >= 목표값인 경우
        else:
            if tmp == k:    # 부분합 == 목표값
                if len(ans) == 0 or (len(ans) != 0 and (ans[1] - ans[0]) > (r - l)):
                    # 답을 못찾았거나, 이전에 찾은 답보다 길이가 짧다면
                    ans = [l, r]
            
            tmp -= sequence[l]  # 부분합에서, 부분수열의 맨 왼쪽 숫자만큼 빼기
            l += 1  # # 부분수열 범위를 왼쪽에서 한칸 줄이기
            
    return ans