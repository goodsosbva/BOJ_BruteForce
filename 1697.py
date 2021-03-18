from collections import deque

cnt = 0


def BFS():
    q = deque()
    q.append(n)  # 5
    while q:
        x = q.popleft()
        if x == k:
            print(dis[x])
            break
        for dx in (x - 1, x + 1, x * 2):  # 4, 6, 10
            if 0 <= dx <= MAX and not dis[dx]:
                dis[dx] = dis[x] + 1
                q.append(dx)


MAX = 100000
n, k = map(int, input().split())
dis = [0] * (MAX + 1)

BFS()
