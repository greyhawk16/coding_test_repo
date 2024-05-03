from collections import deque


def solution(board):
    ans = -1
    n, m = len(board), len(board[0])

    que = deque()
    dist = [[10**6] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                que.append([i, j, 0])
                break
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while que:
        x, y, dst = que.popleft()
        
        if board[x][y] == 'G':
            ans = dst
            break
            
        for i in range(4):
            nx, ny = x, y
            
            while (0 <= nx + dx[i] < n) and (0 <= ny + dy[i] < m) and (board[nx+dx[i]][ny+dy[i]] != 'D'):
                nx += dx[i]     # 장애물에 부딪히거나, 경계에 도달하기 까지 무조건 직진
                ny += dy[i]
                
            if dist[nx][ny] > dst + 1:
                dist[nx][ny] = dst + 1
                que.append([nx, ny, dst + 1])
    
    return ans


a = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(a))