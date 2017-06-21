#!/usr/bin/python

# Format of each line is:
# Client IP\Client identity\Client username\server time\client request\status code/size
#

#
# Question 4 - Find the number of hits on each file on the server
#

#
# We only need the filename
# We need to print the filename, the reducer can count the number of times the filename appears
#

import sys

for line in sys.stdin:

    data = line.strip().split(' ')
    if len(data) == 10:
        ip,client,usn,time,zone,method,file_name,proto,status,size = data
	print file_name
