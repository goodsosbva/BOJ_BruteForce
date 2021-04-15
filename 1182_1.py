import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

res = 0
for num in range(1, n + 1):
    combi = combinations(numbers, num)
    for t in combi:
        if sum(t) == s:
            res += 1

print(res)