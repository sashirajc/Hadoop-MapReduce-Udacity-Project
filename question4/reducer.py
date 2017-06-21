#!/usr/bin/env python

import sys

oldFile = None
count = 0

#
# Question 4 - Find the number of hits on each file on the server
#

#
# Loop around the data
# It will be in the format file\count
# Where file is the file name on server, count is the number of hits on that particular file
#


for line in sys.stdin:
    newFile = line.strip().split(" ")
    if len(newFile) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if oldFile and oldFile != newFile:

        # Print filename and hit count
        print oldFile, "\t", count
        oldFile = newFile;
        count = 0

    oldFile = newFile
    count += 1

if oldFile != None:
    print oldFile, "\t", count
