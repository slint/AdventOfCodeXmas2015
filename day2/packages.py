
from operator import mul

def get_data(fname):
	package_sizes = []
	with open(fname, "r") as fin:
		package_sizes = [tuple(int(d) for d in line.split("x")) for line in fin.readlines() if len(line) > 0]
	return package_sizes

def box_side_areas(l, w, h):
	first = l * w
	second = w * h
	third = h * l
	return (first, second, third)
	
def calculate_package_paper(dimensions):
	areas = box_side_areas(*dimensions)
	return 2 * sum(areas) + min(areas)

def calculate_package_ribbon(dimensions):
	first_smallest, second_smallest = sorted(dimensions)[:2]
	package_area = reduce(mul, dimensions, 1)
	return 2 * ( first_smallest + second_smallest) + package_area
	
	
if __name__ == "__main__":
	package_dims = get_data("input.txt")
	
	total_paper = 0
	total_ribbon = 0
	for dims in package_dims:
		total_paper += calculate_package_paper(dims)
		total_ribbon += calculate_package_ribbon(dims)
	

	print (total_paper, total_ribbon)