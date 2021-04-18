import sys
from itertools import combinations
from collections import defaultdict

n, s = map(int, sys.stdin.readline().split())
m = list(map(int, sys.stdin.readline().split()))

left = m[:n // 2]
right = m[n // 2:]

leftTotal = defaultdict(int)
rightTotal = defaultdict(int)
leftTotal[0] = 1
rightTotal[0] = 1

for i in range(1, len(left) + 1):
    print(list(combinations(left, i)))
    for com in combinations(left, i):
        leftTotal[sum(com)] += 1

for i in range(1, len(right) + 1):
    for com in combinations(right, i):
        rightTotal[sum(com)] += 1

# 계산할때는 키만 이용할거기 때문에
leftSumNum = sorted(leftTotal.keys())
rightSumNum = sorted(rightTotal.keys())

print(leftTotal)

res = 0
left = 0
right = len(rightSumNum) - 1
while left < len(leftSumNum) and right >= 0:
    if leftSumNum[left] + rightSumNum[right] == s:
        res += (leftTotal[leftSumNum[left]] * rightTotal[rightSumNum[right]])  # value * value 형식
        left += 1
        right -= 1
    elif leftSumNum[left] + rightSumNum[right] > s:
        right -= 1
    else:
        left += 1

if s == 0:
    res -= 1

print(res)
