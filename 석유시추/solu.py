# 위치: https://school.programmers.co.kr/learn/courses/30/lessons/250136
# 참고: https://velog.io/@seungjae/프로그래머스-PCCP-기출문제-2번-석유-시추-Python-BFS

# 해설: https://developing-kestrel.tistory.com/19

from collections import deque


def calculate_oil(land, i, j, visited, oil_amount):
    # oil_amount: 열 당 얻을 수 있는 석유의 총량
    # visited: 방문여부 확인
    
    oil = 0                          # 현재 석유덩어리에서 얻을 수 있는 석유량
    n, m = len(land), len(land[0])   # land의 행, 열 수 
    que = deque()                    # BFS 탐색에 필요
    que.append([i, j])               # 시작점을 deque에 넣기
    
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    l, r = j, j     # 현재 보는 석유 덩어리가 걸쳐있는 열
                   # l: 좌측 경계선
                   # r: 우측 경계선
    
    # 1) 석유량 산출
    # 2) 석유 덩어리가 있는 열 구하기
    while que:     # BFS 탐색
        x, y = que.popleft()
        
        if land[x][y] == 1 and visited[x][y] == False:  # 석유가 있고, 방문하지 않은 경우
            visited[x][y] = True   # 방문 처리
            oil += 1               # 석유량 증가
            
            l = min(l, y)    # l 갱신
            r = max(r, y)    # r 갱신
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx and nx < n) and (0 <= ny and ny < m):       # 영역을 벗어나지 않음
                    if land[nx][ny] == 1 and visited[nx][ny] == False:  # 석유가 있고, 방문하지 않은 경우
                        que.append([nx, ny])   
                    else:          # 그 외
                        continue   # 무시
    
    # 3) oil_amount 에서, 지금 본 석유덩어리가 걸쳐있는 열들에 oil 만큼 더하기
    for i in range(l, r+1):     # 열 구간 [l, r] 사이에서는 oil 만큼 석유를 더 얻을 수 있음
        oil_amount[i] += oil    # oil 만큼 석유량 증가
        
    return [oil, l, r]


def solution(land):
    visit_map = [[False for _ in range(len(land[0]))] for _ in range(len(land))]  # 방문여부 저장
    n, m = len(land), len(land[0])
    oil_amount = [0 for _ in range(m)]   # 각 열에서 얻을 수 있는 석유 총량
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visit_map[i][j] == False:        # 석유가 묻혀있고, 방문한 적이 없다면
                calculate_oil(land, i, j, visit_map, oil_amount)    # 석유량 구해서, 가로지르는 열 구간에 그만큼 더하기
    
    ans = max(oil_amount)   # 열별 얻을 수 있는 석유 총량 중 최댓값
    return ans