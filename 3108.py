from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 2000 and 0 <= ny <= 2000:
                if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())
maps = [[0] * 2001 for _ in range(2001)]
visited = [[0] * 2001 for _ in range(2001)]
start = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 500
    y1 += 500
    x2 += 500
    y2 += 500
    #x1 *= 2
    #y1 *= 2
    #x2 *= 2
    #y2 *= 2
    start.append([x1, y1])
    # 마킹하는 작업
    for i in range(x1, x2 + 1):

        if i == x1 or i == x2:

            for j in range(y1, y2 + 1):

                maps[i][j] = 1
        else:
            maps[i][y1] = 1
            maps[i][y2] = 1

# 첫 예제로 어떻게 마킹되는 보여주기 위해 첨가한 이중 for 문
for i in range(500, 520):
    for j in range(500, 520):
        print(maps[i][j], end=" ")
    print("\n")

q = deque()
ans = 0
for i in range(len(start)):
    x, y = start[i]
    if visited[x][y] == 0:
        bfs(x, y)
        ans += 1

if maps[1000][1000] == 1:
    ans -= 1

print(ans)
