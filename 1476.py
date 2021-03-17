e, s, m = map(int, input().split())

E, S, M = 1, 1, 1
n = 0

while True:

    if E == e and S == s and M == m:
        n += 1
        break
    if E < 15:
        E += 1
    else:
        E = 1
    if S < 28:
        S += 1
    else:
        S = 1
    if M < 19:
        M += 1
    else:
        M = 1
    n += 1

print(n)
