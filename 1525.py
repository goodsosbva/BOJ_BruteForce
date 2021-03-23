# print("ヾ(❀^ω^)ﾉﾞ")

import sys
from collections import deque

# 왼, 아래, 오, 위
dcol = [-1, 0, 1, 0]
drow = [0, -1, 0, 1]


def swap(s, n, k):
    l = s[n]
    m = s[k]
    s = s[:k] + l + s[k + 1:]
    s = s[:n] + m + s[n + 1:]
    return s


def isRange(row, col):
    if col >= 3 or col < 0:
        return False
    if row >= 3 or row < 0:
        return False


def bfs(puzzle_s):
    res = -1
    queue = deque()
    queue.append((puzzle_s, 0))
    visited[puzzle_s] = 1
    # print(visited)

    while queue:
        puzzle_c, cnt = queue.popleft()
        # print(puzzle_c, cnt)
        if puzzle_c == target:
            res = cnt
            break
        pos = puzzle_c.find("0")
        row = pos // 3
        col = pos % 3

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]

            if isRange(nrow, ncol) is False:
                continue

            puzzle_n = puzzle_c
            # print(nrow * 3 + ncol)
            puzzle_n = swap(puzzle_n, pos, nrow * 3 + ncol)

            if not visited.get(puzzle_n):
                visited[puzzle_n] = 1
                queue.append((puzzle_n, cnt + 1))

    return res


puzzle = ""
visited = dict()
for i in range(3):
    line = []
    line = list(map(int, sys.stdin.readline().split()))
    # print(line[0], line[1], line[2])
    puzzle += str(line[0]) + str(line[1]) + str(line[2])

target = "123456780"
res_m = 0
res_m = bfs(puzzle)
print(res_m)
