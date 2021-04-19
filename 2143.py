import sys
from collections import defaultdict

input = sys.stdin.readline

target = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_sum = defaultdict(int)
b_sum = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        print(sum(a[i: j + 1]))
        a_sum[sum(a[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        b_sum[sum(b[i:j + 1])] += 1

answer = 0
print(a_sum, b_sum)

for key in a_sum.keys():
    answer += b_sum[target - key] * a_sum[key]
    # print(B_sum[T - key])
#print(a_sum.keys())
print(answer)