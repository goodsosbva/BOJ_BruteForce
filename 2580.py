import sys


def sudoku(row, col):

    if col == 9:
        sudoku(row + 1, 0)
        return

    if row == 9:  # row 는 8까지 있는데 9라는 건 다돌았따는 뜻을 의미
        for i in range(9):
            for j in range(9):
                print(numbers[i][j], end=" ")
            print()
        sys.exit(0)

    # 만약 해당 위치가 0 이라면 1 부터 9까지 가능한 수 탐색
    if numbers[row][col] == 0:
        for i in range(1, 10):
            if possible(row, col, i):
                numbers[row][col] = i
                sudoku(row, col + 1)

        numbers[row][col] = 0
        return
    # 0 없이 다채워져 있는 경우
    sudoku(row, col + 1)


def possible(row, col, value):
    for q in range(9):
        if numbers[row][q] == value:
            return False

    for w in range(9):
        if numbers[w][col] == value:
            return False

    # 3 * 3 칸에 원소가 중복되는지 검사
    set_row = int(row / 3) * 3
    set_col = int(col / 3) * 3

    for a in range(set_row, set_row + 3):
        for b in range(set_col, set_col + 3):
            if numbers[a][b] == value:
                return False

    return True


# numbers = []
visited = [[0] * 9 for _ in range(9)]
# for i in range(9):
#    i = list(map(int, input().split()))
#    numbers.append(i)
numbers = [[int(x) for x in input().split()]for y in range(9)]

# print(numbers[0][2])  # 5
# print(numbers[2][0])  # 0

# print(numbers)
sudoku(0, 0)

