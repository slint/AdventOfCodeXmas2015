import re
from collections import Counter

infile = "input.txt"

vowels = "aeiou"
disallowed = ["ab", "cd", "pq", "xy"]


def has_enough_vowels(s):
	return sum(Counter([c for c in s if c in vowels]).values()) >= 3

def contains_double_letter(s):
	return re.match(r'.*([a-z])\1.*', s)
	
def contains_disallowed_strings(s):
	return any([c for c in disallowed if c in s])


def contains_repeating_pair(s):
	return re.search(r'([a-z]{2}).*\1', s)


def contains_letter_something_letter(s):
	return re.search(r'([a-z]).\1', s)

def is_nice(s):
	vowels_check = has_enough_vowels(s)
	double_check = contains_double_letter(s)
	disallowed_check = not contains_disallowed_strings(s)
	nice = vowels_check and double_check and disallowed_check
	if nice: print s
	return nice

def is_nice_2(s):
	repeating_pair = contains_repeating_pair(s)
	l_s_l = contains_letter_something_letter(s)
	nice = repeating_pair and l_s_l
	if nice: print s
	return nice

if __name__ == '__main__':
	nice_string_count = 0
	with open(infile, "r") as fin:
		for line in fin:
			if is_nice_2(line.strip()):
				nice_string_count += 1
	print nice_string_count

