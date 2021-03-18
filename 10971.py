import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
visit = [0] * n
m = 1e10


def goSalesman(N, C):
    # print(N, C)
    global n, w, visit, m
    if C < m:
        if all(visit) and N == 0:
            m = min(m, C)
            # print(m)
        for i in range(n):
            if w[N][i] > 0 and not visit[i]:
                visit[i] += 1
                goSalesman(i, C + w[N][i])
                visit[i] -= 1


goSalesman(0, 0)
print(m)
