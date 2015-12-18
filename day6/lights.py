
infile = "input.txt"

def turn_on(light_value):
	return 1

def turn_off(light_value):
	return 0

def toggle(light_value):
	return (light_value + 1) % 2

on_str = "turn on "
off_str = "turn off "
toggle_str = "toggle "
through_str = " through "

commands = {}
commands[on_str] = turn_on
commands[off_str] = turn_off
commands[toggle_str] = toggle

X = 1000
Y = 1000


class Instruction(object):
	def __init__(self, cmd, start, end):
		super(Instruction, self).__init__()
		self.cmd = cmd
		self.start = start
		self.end = end

	def __str__(self):
		return "<Instruction cmd:%s start:%s end:%s>" % (self.cmd.__name__, self.start, self.end)

	def __repr__(self):
		return "<Instruction cmd:%s start:%s end:%s>" % (self.cmd.__name__, self.start, self.end)


def parse_instruction(s):
	command = None

	for prefix, cmd in commands.items():
		if prefix in s:
			s = s.replace(prefix, "")
			command = cmd
			break
	start, end = [tuple([int(v) for v in pair.split(",")]) for pair in s.split(through_str)]

	return Instruction(command, start, end)


def get_instructions(fname):
	instructions = []

	with open(fname, "r") as fin:
		for line in fin:
			instructions.append(parse_instruction(line.strip()))

	return instructions

def get_grid(x, y):
	return [[0 for i in range(y)] for i in range(x)] 

def apply_instructions(instructions, grid):
	for instruction in instructions:
		print instruction
		for i in range(instruction.start[0]



if __name__ == '__main__':
	light_grid = get_grid(X, Y)
	instructions =  get_instructions(infile)
	apply_instructions(instructions, light_grid)

