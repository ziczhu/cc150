#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#************************************
#              cc150
#  1.3 judge anagram string
#  Assume the string is ASCII
#  No space or capital
#
#************************************

import sys


def permutation(string1, string2):

	string1 = string1.replace(" ", "").lower()
	string2 = string2.replace(" ", "").lower()

	if len(string1) != len(string2):
		return False

	char_set = [0] * 128

	for char in string1:
		index = ord(char)
		char_set[index] += 1

	for char in string2:
		index = ord(char)
		char_set[index] -= 1
		if char_set[index] < 0:
			return False

	return True


if __name__ == '__main__':

	if len(sys.argv) != 3:
		print('Usage: python3 1.1.py string1 string2.')
	else:
		print(permutation(sys.argv[1], sys.argv[2]))