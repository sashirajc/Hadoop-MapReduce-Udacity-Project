#!/usr/bin/python

# Format of each line is:
# Client IP\Client identity\Client username\server time\client request\status code/size
#

#
# Question 6 - Find the most popular file on the server and the number of occurrences of the said file on the log
#

import sys
import re

for line in sys.stdin:

    data = line.strip().split(' ')
    if len(data) == 10:
        ip,client,usn,time,zone,method,file_name,proto,status,size = data
        cleanFile = re.sub(r'^http://www.the-associates.co.uk','',file_name)
	    print file_name
