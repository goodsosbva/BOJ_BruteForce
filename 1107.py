n = int(input())
m = int(input())
buttons = {str(i) for i in range(10)}
newbutton = []

if m != 0:
    errbuttons = list(map(str, input().split(" ")))
    for i in buttons:
        if i not in errbuttons:
            newbutton.append(i)
else:
    newbutton = buttons


# print(newbutton)
# +,- 로 이동했는데 최소값일 경우
minCount = abs(100 - n)

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        # print(j)
        if num[j] not in newbutton:
            break
        # j 가 len(num) - 1 이 된다는 경우는 원하는 수에 대해 리모콘이 다눌러졌다는 뜻
        elif j == len(num) - 1:
            minCount = min(minCount, abs(n - int(num)) + len(str(num)))

print(minCount)
