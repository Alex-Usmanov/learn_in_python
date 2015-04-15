# coding:utf-8
_empty_char = '+'
# _default_size = input("please input the size of the chess map : ")

def game_init_board(size=15):
    board = [['+'] * size for i in range(size)]
    return board


def game_place_at(board, position, color):
    size = len(board)
    x, y = position
    if 0 <= x < size and 0 <= y < size:
        # if position[0]<size and position[1]<size:
        if board[y][x] is _empty_char:
            board[y][x] = color
        else:
            return "can't place at this position", position
    else:
        return "wrong position."

'''
def _diagonal_line0(board, position):
    # (6,4)(7,3)(8,2)(9,1)(10,0)
    x0, y0 = position
    z0 = x0 + y0
    global diagonal
    x = 0
    y = 0
    for hor in board:
        for ver in hor:
            z = x + y
            if z is z0:
                diagonal = ''.join(board[y][x])
            x += 1
        y += 1
    return diagonal


def _diagonal_line1(board, position):
    # (0,0)(1,1)(2,2)(3,3)(4,4)
    size = len(board)
    x0, y0 = position
    global diagonal
    z0 = x0 - y0 + size
    x = 0
    y = 0
    for hor in board:
        for ver in hor:
            z = x - y + size
            if z is z0:
                diagonal = ''.join(board[y][x])
            x += 1
        y += 1
    return diagonal
'''

def game_check(board, position):
    x, y = position
    color = board[y][x]
    size = len(board)
    win = color * 5

    horizontal = ''.join(board[y])
    vertical = ''.join(board[i][x] for i in range(size))
    # diagonal1 = _diagonal_line0(board, position)
    # diagonal2 = _diagonal_line1(board, position)
    mini=min((x+y),size)
    diagonal1=''.join(board[i][x+y-i] for i in range(mini))
    if y<=x:
        diagonal2=''.join(board[i][x+i-y] for i in range(size+y-x))
        # (0,1)(1,2)(2,3)(3,4)(4,5)
    else:
        diagonal2=''.join(board[y-x+i][i] for i in range(size+x-y))
        # (1,0)(2,1)(3,2)(4,3)(5,4)

    '''
    for hor in board:
        for ver in hor:
            if (x0 + y0)==(x + y):
                diagonal1 = ''.join(board[y0][x0])
            x0 += 1
        y0 += 1

    for hor in board:
        for ver in hor:
            if (x0 - y0) ==(x - y):
                diagonal2 = ''.join(board[y0][x0])
            x0 -= 1
        y0 -= 1
    '''
    lines = [horizontal, vertical, diagonal1, diagonal2]
    for i in lines:
        if win in i:
            print("__________你赢了，真是太聪明了·(づ￣ 3￣)づ__________")
            return True


def game_over(color):
    print("胜利者属于 " + color)


def game_display(board):
    size = len(board)
    print('  ' + ''.join(map(lambda i: str(i).rjust(3), range(size))))
    for i in range(size):
        print(str(i).rjust(2) + '  ' + '  '.join(board[i]))


def game_input():
    command = raw_input()
    try:
        raw = command.split()
        position = (int(raw[0]), int(raw[1]))
        return position
    except Exception as e:
        return None

def game_show_instruction(color):
    print("input: x y ")
    print("example: 8 8")
    print("player: " + color)

def main():
    board = game_init_board()
    colors = ['●', '○']
    player = 0
    while True:
        color = colors[player]

        game_display(board)
        # print(board[4][4])
        game_show_instruction(color)

        position = game_input()
        if position is None:
            continue

        status = game_place_at(board, position, color)
        if status is not None:
            print status
            continue

        if game_check(board, position):
            game_display(board)
            game_over(color)
            break

        player = (player + 1) % 2


if __name__ == '__main__':
    import sys

    main()
