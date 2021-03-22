from collections import deque


def bfs(a, b):
    savekey = ""
    q = deque([[a, savekey]])
    visited = [0] * 10000
    visited[a] = True

    while True:
        val, key = q.popleft()
        if val == b:
            return key

        # D
        if not visited[val * 2 % 10000]:
            visited[val * 2 % 10000] = True
            q.append([val * 2 % 10000, key + "D"])
        # S
        if not visited[(val - 1) % 10000]:
            visited[(val - 1) % 10000] = True
            q.append([(val - 1) % 10000, key + "S"])
        # R
        if not visited[(val % 10) * 1000 + val // 10]:
            visited[(val % 10) * 1000 + val // 10] = True
            q.append([(val % 10) * 1000 + val // 10, key + "R"])
        # L
        if not visited[(val % 1000) * 10 + val // 1000]:
            visited[(val % 1000) * 10 + val // 1000] = True
            q.append([(val % 1000) * 10 + val // 1000, key + "L"])


TestCase = int(input())
for _ in range(TestCase):
    a, b = map(int, input().split())
    print(bfs(a, b))

