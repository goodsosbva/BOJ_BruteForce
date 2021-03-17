import itertools

n = int(input())

nums = list(map(int, input().split(" ")))

res = 0
numbers = itertools.permutations(nums, n)

for num in numbers:
    listn = list(num)
    sum = 0
    for i in range(n - 1):
        sum += abs(listn[i] - listn[i + 1])
    res = max(sum, res)

print(res)