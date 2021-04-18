from collections import deque
from sys import stdin

t, r = map(int, stdin.readline().split())
matrix = []

for i in range(r):
    matrix.append(stdin.readline())

# 방문경로 배열
visited = [[-1] * t for _ in range(r)]
visited[0][0] = 0
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue.append([0, 0])

# bfs
while queue:
    x, y = queue.popleft()
    # print(x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < t:
            if visited[nx][ny] == -1:
                if matrix[nx][ny] == '0':
                    queue.appendleft([nx, ny])
                    visited[nx][ny] = visited[x][y]
                elif matrix[nx][ny] == '1':
                    queue.append([nx, ny])
                    # print(nx, ny)
                    visited[nx][ny] = visited[x][y] + 1


print(visited[r - 1][t - 1])



