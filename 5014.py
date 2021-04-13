from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([s])
    print(q)
    dp[s] = 1
    while q:
        start = q.popleft()
        if start == g:
            print(dp[g] - 1)  # 1 부터 시작하니까 끝날 때는 -1을 해주는 것
            return

        up = start + u
        down = start - d
        if up <= f and not dp[up]:
            q.append(up)
            dp[up] = dp[start] + 1
        if down > 0 and not dp[down]:
            q.append(down)
            dp[down] = dp[start] + 1

    else:
        print("use the stairs")
        return


f, s, g, u, d = map(int, input().split())
dp = [0] * (f + 1)
bfs()

