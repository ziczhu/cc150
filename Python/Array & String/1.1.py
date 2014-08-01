#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#************************************
#              cc150
#  1.1 judge unique chars in a string
#  Assume the string is ASCII
#
#************************************

import sys


def isUniqueChars(string):

	string = string.replace(" ", "")

	if len(string) > 256:
		return False

	char_set = [False] * 256
	for char in string:
		index = ord(char)
		if index < 256:
			if char_set[index]:
				return False
			char_set[index] = True
		else:
			raise Exception('Only support ASCII string.')

	return True


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print('Usage: python3 1.1.py string.')
	else:
		print(isUniqueChars(sys.argv[1]))



