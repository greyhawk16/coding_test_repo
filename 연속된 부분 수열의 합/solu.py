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
        if tmp < k:
            r += 1
            if r == n:
                break
            else:
                tmp += sequence[r]
        else:
            if tmp == k:
                if len(ans) == 0 or (len(ans) != 0 and (ans[1] - ans[0]) > (r - l)):
                    ans = [l, r]
            tmp -= sequence[l]
            l += 1
            
    return ans