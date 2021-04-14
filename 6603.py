import itertools

while True:
    k, *lotto = list(map(int, input().split()))
    print(k, lotto)

    if k == 0:
        break
    lotto.sort()

    ans = itertools.combinations(lotto, 6)  # 수학기호 lotto 콤비네이션 6 라고 생각하시면 됩니다.
    for i in ans:
        for j in list(i):
            print(j, end=" ")
        print()
    print()






