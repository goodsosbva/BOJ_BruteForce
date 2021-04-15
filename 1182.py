n, s = map(int, input().split())
numbers = list(map(int, input().split()))


def dfs(i, sum):

    global res
    if i == n:
        return
    if sum + numbers[i] == s:
        res += 1

    dfs(i + 1, sum)
    dfs(i + 1, sum + numbers[i])


res = 0
dfs(0, 0)
print(res)