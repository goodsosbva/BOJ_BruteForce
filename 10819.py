n = int(input())

nums = list(map(int, input().split(" ")))

res = 0

print(nums)


while True:
    if nums is None:
        break
    max = 0
    min = 10000
    for i in nums:
        # print(type(max))
        # print(max)
        if i > max:
            max = i

    if len(nums) == 0:
        break
    else:
        print(max)
        nums.remove(max)
        n = n - 1

    for j in nums:
        if j < min:
            min = j

    print(min)
    nums.remove(min)
    n = n - 1

    res += max - min
    max = 0

    for i in nums:
        # print(type(max))
        # print(max)
        if i > max:
            max = i

    res += abs(min - max)


print(res)
