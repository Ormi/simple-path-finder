#!/usr/bin/env python3

# name parser.py
# description Parse config files based on their structure for further processing
# author Michal Ormos (mi.ormos@gmail.com)
# date 27.3.2021
# license MIT

from array import *
import re

lines = []
array = []
filename='configs/config1.conf'

# TODO hanlde expections and errors

# TODO may be wiser tu use list in the future which is more python thing, than 2D array
# TODO which is more memory/cpu consuming to iterate through
class Parser:
    def __init__(self, array, lines, filename):
        self.array = array
        self.lines = lines
        self.filename = filename

    # count lines and prepare array size needed
    def prepareDataTypes(self):
        count = len(open(self.filename).readlines(  ))
        for i in range(count):
            array.append([])

    # split by new lines
    def lineSplit(self):
        try:
            with open(self.filename,'r') as fp:
                for line in fp:
                    lines.append(line)
                return lines
        except:
            print(e)

    # split by words
    def wordSplit(self):
        lineNumber = 0
        for entry in self.lines:
            # get rid of end of the line
            entry = entry.strip('\n')
            line = re.findall(r"[\w']+", entry)
            array[lineNumber] = line
            lineNumber = lineNumber + 1

parser = Parser(array, lines, filename)
parser.prepareDataTypes()
lines = parser.lineSplit()
parser.wordSplit()