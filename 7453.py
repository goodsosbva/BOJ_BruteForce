import sys
from itertools import combinations

n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab = []
cd = []
for i in range(n):
    for j in range(n):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()

# print(ab, cd)

ans = 0
left = 0
right = len(cd) - 1
while left < len(ab) and right >= 0:
    if ab[left] + cd[right] > 0:
        right -= 1
    elif ab[left] + cd[right] < 0:
        left += 1
    else:
        # 같은 숫자가 나왔을 때 한 쪽만 옮겨서 같은 수가 나올 확률도 있으니 조사해 보는 것
        # print(ab[left], cd[right])
        a_size = 1
        b_size = 1
        while left < len(ab) - 1 and ab[left + 1] == ab[left]:
            left += 1
            a_size += 1
        while right > 0 and cd[right - 1] == cd[right]:
            right -= 1
            b_size += 1
        ans += (a_size * b_size)
        left += 1
        right -= 1

print(ans)