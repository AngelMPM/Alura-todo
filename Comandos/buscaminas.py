board = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

mines = [(2, 3), (5, 6), (8, 1), (1, 5), (7, 3)]

# populate the board with the number of mines in the surrounding squares
for i in range(10):
    for j in range(10):
        if (i, j) in mines:
            board[i][j] = 'X'
        else:
            mines_around = 0
            for x in range(max(0, i - 1), min(9, i + 2)):
                for y in range(max(0, j - 1), min(9, j + 2)):
                    if (x, y) in mines:
                        mines_around += 1
            board[i][j] = str(mines_around)

# print the board
for row in board:
    print(' '.join(row))
