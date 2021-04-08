import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
w = [list(map(int, input().split())) for i in range(n)]
visit = [0] * n
m = 1e10


def goSalesman(N, C):
    # print(N, C)
    global n, w, visit, m
    if C < m:  # else 의 경우는 이제 까지의 비용의 합인 m 값보다  C가 더 크다면 볼필요도 없는 경우!
        # 파이썬 all 함수는 iterable한 객체의 모든 값이 참일 때 참을 반환 하는 함수 입니다.
        # 즉, 모드 순회하고, n == 0 으로 다시 돌아온 경우에 그 값을 반환 하는 것 입니다.
        if all(visit) and N == 0:
            m = min(m, C)
            print(visit)
            # print(m)
        # 재귀를 통한 가중치 계산
        for i in range(n):
            if w[N][i] > 0 and not visit[i]:
                visit[i] += 1
                goSalesman(i, C + w[N][i])
                # else 로 빠져 나온 경우.
                visit[i] -= 1


goSalesman(0, 0)
print(m)
