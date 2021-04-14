from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global cnt
    q = set([(x, y, maps[x][y])])
    # print(q)
    while q:
        x, y, same_string = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] not in same_string:  # 경로내 타당한 좌표인지, 중복 알파벳이 아닌지 확인
                # if maps[nx][ny] == 1 and visited[nx][ny] == 0 and maps[nx][ny] not in samestr:
                q.add((nx, ny, same_string + maps[nx][ny]))  # 집합에 추가!
                cnt = max(cnt, len(same_string) + 1)


r, c = map(int, input().split())

visited = [[0] * r for _ in range(c)]
# maps = []

maps = [list(map(str, input().strip())) for _ in range(r)]

# print(maps)
q = deque()
cnt = 1
bfs(0, 0)
print(cnt)

