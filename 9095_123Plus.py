import sys

test_n = int(sys.stdin.readline())
# sx = 2 * n

dp = [0, 1, 2, 4]

for i in range(4, 11):
    dp.append((dp[i - 2]) + (dp[i - 1]) + dp[i - 3])

for _ in range(test_n):
    print(dp[int(input())])
