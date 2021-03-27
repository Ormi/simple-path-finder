#!/usr/bin/env python3

# name parser.py
# author Michal Ormos (mi.ormos@gmail.com)
# date 27.3.2021
# license MIT

from array import *
import re

lines = []
array = []
filename='../test_input_files/config1.conf'

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
        with open(self.filename,'r') as fp:
            for line in fp:
                lines.append(line)
            return lines

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
