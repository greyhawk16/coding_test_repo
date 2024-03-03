# 위치: https://school.programmers.co.kr/learn/courses/30/lessons/250137

from collections import deque


def solution(bandage, health, attacks):
    ans = health
    que = deque()
    cool_time = bandage[2]
    
    for i in range(len(attacks)):
        que.append(attacks[i])
        
    for i in range(1, attacks[-1][0] + 1):
        
        if que[0][0] == i:
            x = que.popleft()
            ans -= x[1]
            cool_time = bandage[0]
            
            if ans <= 0:
                return -1
            
        else:
            ans += bandage[1]
            cool_time -= 1
            
            if cool_time == 0:
                ans += bandage[2]
                cool_time = bandage[0]
            
            ans = min(ans, health)
        
    return ans