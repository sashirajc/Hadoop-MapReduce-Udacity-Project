#!/usr/bin/env python

import sys

popularFile = None
popularCount = 0

currentFile = None
currentCount = 0
# Loop around the data
# It only contains the filename
# The number of times the filename occurs is counted and printed when the filename changes

#
# Question 6 - Find the most popular file on the server and the number of occurrences of the said file on the log
#


for line in sys.stdin:
    file_name = line.strip().split(" ")
    if len(file_name) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if currentFile and currentFile != file_name:
        if currentCount > popularCount:
            popularFile = currentFile
            popularCount = currentCount

            currentCount = 0

    currentFile = file_name
    currentCount += 1

print "{0}\t{1}".format(popularFile,popularCount)
