#!/usr/bin/env python

import sys

oldIP = None
count = 0

# Loop around the data
# It will be in the format ip\count
#

#
# Question 5 - Find the number of hits on the server by each IP
#

# Count the number of times each IP address appears in the data

for line in sys.stdin:
    newIP = line.strip().split(" ")
    if len(newIP) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if oldIP and oldIP != newIP:
        print oldIP, "\t", count
        oldIP = newIP;
	    count = 0

    oldIP = newIP
    count += 1

if oldIP != None:
    print oldIP, "\t", count
