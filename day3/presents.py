
from collections import defaultdict
from itertools import cycle

default_input_file = "input.txt"

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'

def get_data(fname):
	
	instructions = []
	with open(fname, "r") as fin:
		instructions = list(fin.read())
	return instructions

def update_position(position, instruction):
	
	if instruction == UP:
		position[1] += 1
	elif instruction == DOWN:
		position[1] -= 1
	elif instruction == LEFT:
		position[0] -= 1
	elif instruction == RIGHT:
		position[0] += 1


def count_visited_houses(data):
	
	santa_position = [0, 0]
	robo_santa_position = [0, 0]

	visited_houses = defaultdict(int)
	visited_houses[tuple(santa_position)] += 1
	visited_houses[tuple(robo_santa_position)] += 1

	santas = cycle([santa_position, robo_santa_position])

	for instruction in data:
		current_santa = santas.next()
		update_position(current_santa, instruction)
		visited_houses[tuple(current_santa)] += 1
	
	return len(visited_houses)

if __name__ == '__main__':
	data = get_data(default_input_file)
	print count_visited_houses(data)
