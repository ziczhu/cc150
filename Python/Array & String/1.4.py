#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#************************************
#              cc150
#  1.4 replace spaces
#
#************************************

import sys
from array import array
from urllib.parse import quote


def replaceSpaces1(string):

    listString = list(string)

    for index, char in enumerate(listString):
        if char == ' ':
            listString[index] = '%20'

    return ''.join(listString)


# Actually, this method is slower than normal join method, here it just aim at illustrating the algorithm
def replaceSpaces2(string):

    arr = array('u', string)
    oldArrLen = arr.buffer_info()[1]
    spaceCount = arr.count(' ')
    arr.fromunicode('  ' * spaceCount)
    newArrLen = oldArrLen + spaceCount * 2

    for x in reversed(range(oldArrLen)):
        if arr[x] == ' ':
            arr[newArrLen - 1] = '0'
            arr[newArrLen - 2] = '2'
            arr[newArrLen - 3] = '%'
            newArrLen -= 3
        else:
            arr[newArrLen - 1] = arr[x]
            newArrLen -= 1

    return arr.tounicode()


def replaceSpaces3(string):

    return quote(string)


def replaceSpaces4(string):

    return string.replace(' ', '%20')


if __name__ == '__main__':

    import timeit

    def testOne():
        return replaceSpaces1(sys.argv[1])

    def testTwo():
        return replaceSpaces2(sys.argv[1])

    def testThree():
        return replaceSpaces3(sys.argv[1])

    def testFour():
        return replaceSpaces4(sys.argv[1])

    if len(sys.argv) != 2:

        print('Usage: python3 1.1.py string.')
    else:

        print('Using python char join: ', testOne())
        print(timeit.timeit('testOne()', setup= 'from __main__ import testOne', number=10000))
        print('Using python array replace: ', testTwo())
        print(timeit.timeit('testTwo()', setup= 'from __main__ import testTwo', number=10000))
        print('Using python urllib parse: ', testThree())
        print(timeit.timeit('testThree()', setup= 'from __main__ import testThree', number=10000))
        print('Using python regex: ', testFour())
        print(timeit.timeit('testFour()', setup= 'from __main__ import testFour', number=10000))
