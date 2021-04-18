from collections import defaultdict


def dfs(idx, end_idx, subtotal, direction):
    global ans
    print("----------------")
    print("ans, idx, end_idx, suntotal: ", ans, idx, end_idx, subtotal)
    print("left", left)
    if idx == end_idx:
        if direction == "right":
            print("if, idx, s - subtotal, left[s - subtotal]: ", idx, s - subtotal, left[s - subtotal])
            ans += left[s - subtotal]
        else:
            print("else", idx, subtotal)
            left[subtotal] += 1
        return

    dfs(idx + 1, end_idx, subtotal, direction)
    dfs(idx + 1, end_idx, subtotal + numbers[idx], direction)


ans = 0
n, s = map(int, input().split())
numbers = list(map(int, input().split()))
left = defaultdict(int)

#print(left)
dfs(0, n//2, 0, "left")
dfs(n//2, n, 0, "right")
print(left)
print(ans)
print(ans if s != 0 else ans - 1)

