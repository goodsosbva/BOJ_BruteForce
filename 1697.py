from collections import deque

cnt = 0


def BFS():
    q = deque()
    q.append(n)  # 5
    while q:
        x = q.popleft()
        if x == k:  # 동생을 찾았을 때
            print(dis[x])
            break
        for dx in (x - 1, x + 1, x * 2):  # 4, 6, 10
            if 0 <= dx <= MAX and not dis[dx]:  # 범위 밖을 나가지 않았는지 체크
                dis[dx] = dis[x] + 1  # 거리라기 보단 이동 횟수
                q.append(dx)  # 그방향 다시 탐색


MAX = 100000
n, k = map(int, input().split())
dis = [0] * (MAX + 1)

BFS()

