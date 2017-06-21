#!/usr/bin/python

# Format of each line is:
# Client IP\Client identity\Client username\server time\client request\status code/size
#

#
# Question 5 - Find the number of hits on the server by each IP
#

#
# We want only 1 item - IP address
# We need to print the IP address from the log, reducer will count the number of hits

import sys

for line in sys.stdin:

    data = line.strip().split(' ')
    if len(data) == 10:
        ip,client,usn,time,zone,method,file_name,proto,status,size = data
	print ip
