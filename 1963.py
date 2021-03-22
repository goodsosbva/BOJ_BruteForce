import copy
from collections import deque


# 기본적인 소수 판별 방법(2부터 n-1까지 돌려보기)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인
    for i in range(2, x):
        # x가 해당 수로 나누어떨어지면
        if x % i == 0:
            return False
    return True


def bfs(a, b):

    q = deque([[list(str(a)), 0]])
    # print(q)
    visited = {a}

    while True:
        val, cnt = q.popleft()
        if int("".join(map(str, val))) == b:
            return cnt
        else:
            for i in range(4):
                for j in range(10):
                    if val[i] == str(j):  # 같은 숫자는 바꾸는게 의미가 없으므로
                        continue
                    else:
                        temp = copy.deepcopy(val)
                        temp[i] = str(j)  # 숫자 바꾸기
                        temp_value = int("".join(map(str, temp)))
                        # 조건에 맞게 확인
                        if temp_value not in visited and temp_value >= 1000 and is_prime_number(temp_value):
                            visited.add(temp_value)
                            q.append([temp, cnt + 1])


TestCase = int(input())
for _ in range(TestCase):
    a, b = map(int, input().split())
    print(bfs(a, b))
