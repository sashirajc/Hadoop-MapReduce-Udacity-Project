#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

#
# Get total number of sales and total sales value from all stores
#

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    # Ensure there are 6 items on the list
    if len(data) == 6:
        date, time, store, item, cost, payment = data

        # Print only store and cost
        print "{0}\t{1}".format(store, cost)
