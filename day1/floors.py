


fin = open("input.txt", "r")
instructions = fin.read()
fin.close()

fl = 0
for i, c in enumerate(instructions):
	if c == '(':
		fl += 1
	elif c == ')':
		fl -= 1
	if fl == -1:
		print (i + 1)
