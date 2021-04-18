import sys
from collections import deque

t, r = map(int, sys.stdin.readline().split())
matrix = []

for i in range(r):
    matrix.append(sys.stdin.readline())

visited = [[-1] * t for _ in range(r)]
visited[0][0] = 0
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue.append([0, 0])

while queue:
    x, y = queue.popleft()
    # print(x, y)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < t:
            if visited[nx][ny] == -1:
                if matrix[nx][ny] == '0':
                    queue.appendleft([nx, ny])
                    # print(nx, ny)
                    visited[nx][ny] = visited[x][y]
                elif matrix[nx][ny] == '1':
                    queue.append([nx, ny])
                    # print(nx, ny)
                    visited[nx][ny] = visited[x][y] + 1

print(visited[r - 1][t - 1])
