#!/usr/bin/env python3

# name finder.py
# Description find path between start and end in the arrray given from parser
# author Michal Ormos (mi.ormos@gmail.com)
# date 27.3.2021
# license MIT

import sys
from src.parser import array

# TODO hanlde expections and errors
def findPath(start,end):
    # print("I am finding path from " + start + " to " + end + " in the envinroment")
    # print(array)

    # TODO improve and rewrite to recursion style
    # TODO it will be more elegant and performance better
    for x in range(len(array)):
        for y in range(len(array[x])):
            if (array[x][y].lower()) == start.lower():
                startX = x
                startY = y
            if (array[x][y].lower()) == end.lower():
                endX = x
                endY = y

    print("You are in " + start)
    for i in reversed(range(startY)):
        # If objects in array are equal skip them, because we are standing
        # already in that position
        if array[startX][i] != array[endX][i]:
            print("Go to the " + array[startX][i])
    for z in range(endY):
        # If objects in array are equal skip them, because we are standing
        # already in that position
        if array[startX][z] != array[endX][z]:
            print("Go to the " + array[endX][z])
    print("Get the " + array[endX][endY])

# read arguments and prepare variables
if len(sys.argv) == 4:
    if sys.argv[1] == 'path-to-object':
        start = sys.argv[2]
        end = sys.argv[3]
    findPath(start, end)
else:
    print("Error: not enough input arguments\n\
        Usage:\n\
        python3 app.py path-to-object Basement knife")