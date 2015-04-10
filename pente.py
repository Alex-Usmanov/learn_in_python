#coding: utf-8

_empty_char = ' +'

def game_init_board(size=15):
	board = [[' +'] * size for i in range(size)]
	return board

def game_place_at(board, position, color):
	x, y = position
	# make sure position in board
	size = len(board)
	if 0 <= x < size and 0 <= y < size:
		if board[y][x] != _empty_char:
			return "can't place at ", position
		board[y][x] = color
	else:
		return "wrong position"

def _diagonal_line(board, position, direction):
	x, y = position
	size = len(board)
	minimum = min(position)
	maximum = max(position)

	# TODO, diagonal lines
	diagonal = []
	return diagonal

def game_check(board, position):
	# 复杂啰嗦的check
	x, y = position
	color = board[y][x]
	size = len(board)
	win = color * 5

	horizontal = ''.join(board[y])
	vertical = ''.join([board[i][x] for i in range(size)])
	diagonal1 = _diagonal_line(board, position, 1)
	diagonal2 = _diagonal_line(board, position, -1)

	lines = [horizontal, vertical, diagonal1, diagonal2]

	for i in lines:
		if win in i:
			print '——————Win——————\a'
			return True

def game_over(color):
	print 'winner is ', color

def game_display(board):
	size = len(board)
	print '   ' + ' '.join(map(lambda i: str(i).rjust(2), range(size)))
	for i in range(size):
		print str(i).rjust(2) + ' ' + ' '.join(board[i])

def game_input():
	command = raw_input()
	try:
		raw = command.split()
		instruction = (int(raw[0]), int(raw[1]))
		return instruction
	except Exception as e:
		return None

def game_show_instruction(color):
	# game help
	print 'input: x y'
	print 'example: 8 8'
	print 'player: ', color

def main():
	board = game_init_board()
	colors = ['●', '○']
	player = 0
	while True:
		color = colors[player]
		# display game board
		game_display(board)
		# show game instruction
		game_show_instruction(color)
		# user input
		instruction = game_input()
		if instruction is None:
			continue
		# place 
		status = game_place_at(board, instruction, color)
		if status is not None:
			print status
			continue
		# check game
		if game_check(board, instruction):
			game_over(color)
			break
		# switch player
		player = (player + 1) % 2


if __name__ == '__main__':
	import sys
	main()
