# https://school.programmers.co.kr/learn/courses/30/lessons/250125 

def solution(board, h, w):
    ans = 0
    n, m = len(board), len(board[0])
    color = board[h][w]
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):
    	# 1) 탐색할 곳의 좌표 파악
        nx = h + dx[i]
        ny = w + dy[i]
        
        # 2) 좌표가 탐색범위를 벗어나지 않고, 색깔이 같은 지 판단
        if -1 < nx < n and -1 < ny < m and board[nx][ny] == color:
            ans += 1
    
    return ans