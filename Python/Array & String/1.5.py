#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#************************************
#              cc150
#  1.5 compress string
#
#************************************


import string
import sys
from io import StringIO


def compress(st):

    p = 0
    first = st[0]
    count = 1
    newSt = ''
    for p in range(1, len(st)):
        if st[p] == first:
            count += 1
        else:
            newSt += first + str(count)
            first = st[p]
            count = 1
        p += 1
    newSt += first + str(count)
    if len(st) <= len(newSt):
        return st
    return newSt


def compressTwo(st):

    ls = list(st)
    first = ls[0]
    newLs = []
    count = 0
    for char in ls:
        if char == first:
            count += 1
        else:
            newLs.append(first)
            newLs.append(str(count))
            first = char
            count = 1
    newLs.append(first)
    newLs.append(str(count))
    if len(st) <= len(newLs):
        return st
    return ''.join(newLs)


def compressThree(st):

    file_str = StringIO()
    p = 0
    first = st[0]
    count = 1
    for p in range(1, len(st)):
        if st[p] == first:
            count += 1
        else:
            file_str.write(first + str(count))
            first = st[p]
            count = 1
        p += 1
    file_str.write(first + str(count))
    newSt = file_str.getvalue()
    if len(st) <= len(newSt):
        return st
    return newSt



if __name__ == '__main__':

    import timeit

    def testOne():
        return compress(sys.argv[1])

    def testTwo():
        return compressTwo(sys.argv[1])

    def testThree():
        return compressThree(sys.argv[1])

    if len(sys.argv) != 2:
        print('Usage: python3 1.1.py string.')
    else:
        print('Using python char: ', testOne())
        print(timeit.timeit('testOne()', setup= 'from __main__ import testOne', number=10000))

        print('Using python list: ', testTwo())
        print(timeit.timeit('testTwo()', setup= 'from __main__ import testTwo', number=10000))

        print('Using python StringIO: ', testThree())
        print(timeit.timeit('testThree()', setup= 'from __main__ import testThree', number=10000))
