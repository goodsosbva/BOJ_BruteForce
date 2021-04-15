n, m = map(int, input().split())
numbers = list(map(int, input().split()))

left = 0
right = 0
sum = 0
res = 0

# 순서가 있어야 하는 이유가 있다. while 문이 종료되는 시점을 고려하면 이해 가능
while True:
    if sum >= m:
        sum -= numbers[left]
        left += 1

    # print(right, left)
    elif n == right:
        break

    else:
        sum += numbers[right]
        right += 1

    if sum == m:
        res += 1


print(res)