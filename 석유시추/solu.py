# 위치: https://school.programmers.co.kr/learn/courses/30/lessons/250136
# 참고: https://velog.io/@seungjae/프로그래머스-PCCP-기출문제-2번-석유-시추-Python-BFS

from collections import deque


def calculate_oil(land, i, j, visited, oil_amount):
    oil = 0
    n, m = len(land), len(land[0])
    que = deque()
    que.append([i, j])
    
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    l, r = j,j
    
    while que:
        x, y = que.popleft()
        
        if land[x][y] == 1 and visited[x][y] == False:
            visited[x][y] = True
            oil += 1
            
            l = min(l, y)
            r = max(r, y)
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx and nx < n) and (0 <= ny and ny < m):
                    if land[nx][ny] == 1 and visited[nx][ny] == False:
                        que.append([nx, ny])
                    else:
                        continue
                        
    for i in range(l, r+1):
        oil_amount[i] += oil
        
    return [oil, l, r]
    

def solution(land):
    visit_map = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    n, m = len(land), len(land[0])
    oil_amount = [0 for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visit_map[i][j] == False:
                calculate_oil(land, i, j, visit_map, oil_amount)
    
    ans = max(oil_amount)
    return ans