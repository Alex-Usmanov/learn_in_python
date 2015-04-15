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

def game_check(board, position):
    x, y = position
    color = board[y][x]
    size = len(board)
    win = color * 5

    horizontal = ''.join(board[y])
    vertical = ''.join(board[i][x] for i in range(size))

    if x+y<size:
        diagonal1=''.join(board[i][x+y-i] for i in range(x+y))
        # (0,14)(1,13)(2,12)(3,11)(4,10)
    else:
        diagonal1=''.join(board[x+y-i][i] for i in range(x+y-size+1,size))
        # (2,14)(3,13)(4,12)(5,11)(6,10)
        # 如果用diagonal1=''.join(board[x+y-i][i] for i in range(min(x+y,size))) 会溢出

    if y<=x:
        diagonal2=''.join(board[i][x+i-y] for i in range(size+y-x))
        # (0,1)(1,2)(2,3)(3,4)(4,5)
    else:
        diagonal2=''.join(board[y-x+i][i] for i in range(size+x-y))
        # (1,0)(2,1)(3,2)(4,3)(5,4)11

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
