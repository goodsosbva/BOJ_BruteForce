import copy


def dfs(start, cnt, word, conso, vowel):

    if cnt == l:
        if conso >= 1 and vowel >= 2:
            print(''.join([str(ch) for ch in word]))
            # print(word)

    else:
        for i in range(start, c):
            if not visit[i]:
                visit[i] = 1

                copycy = copy.deepcopy(word)
                copycy.append(words[i])
                # print(copycy)

                if words[i] in consonant:
                    dfs(i, cnt + 1, copycy, conso + 1, vowel)
                else:
                    dfs(i, cnt + 1, copycy, conso, vowel + 1)
                # print(visit, visit[i])
                visit[i] = 0


consonant = ["a", "e", "i", "o", "u"]
l, c = map(int, input().split())  # 만들어진 숫자의 수(l), 주어질 숫자의 수(c)
visit = [0] * c
words = list(map(str, input().split()))
words.sort()

# print(words)
dfs(0, 0, [], 0, 0)  # start, cnt, word, conso, vowel




