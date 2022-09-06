game =[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def empty(gm):
    for i in range(len(gm)):             # ROW
        for j in range(len(gm)):         # COLUMN
            if gm[i][j] == 0:
                return (i,j)                 #(ROW, COLUMN)        # If no empty space is found, returns None
    return None



def print_game(gm):
    for i in range(len(gm)):
        for j in range(len(gm)):

            if j % 3 == 0 and j != 0:
                print(f'|', end=' ')

            if i % 3 == 0 and i != 0 and j == 0:
                print('---------------------')
                print(gm[i][j], end=' ')

            else:
                print(gm[i][j], end=' ')
                if j == 8:
                    print()


def validate(gm, num, pos):                                 # gm = sudoku board, num = chosen number, pos = tuple (i, j) - (row, column)
    #ROW
    for c in range(len(gm[0])):                            # Validate ROW: fixed ROW iterate through column
        if gm[pos[0]][c] == num and pos[1] != c:
            return False

    # COLUMN
    for c in range(len(gm)):                                # Validate Column: fixed column iterate through ROWs
        if gm[c][pos[1]] == num and pos[0] != c:
            return False

    # SQUARE
    X = pos[0] // 3                                         # 9 squares (0-8)
    Y = pos[1] // 3

    for i in range(X*3, X*3 + 3):           # i             # +3 (intervalo aberto no final)
        for j in range(Y*3, Y*3 + 3):       # j
            if gm[i][j] == num and (i, j) != pos:
                return False
    return True


def solver(gm):
    slot = empty(gm)
    if not empty(gm):

      return True
    else:
        row, column = slot                  #coordinates for empty position
    for i in range(1,10):
        if validate(gm, i, slot):
            gm[row][column] = i

            if solver(gm):
                return True

            gm[row][column] = 0

    return False


print_game(game)
print('      ---------')
solver(game)
print_game(game)

