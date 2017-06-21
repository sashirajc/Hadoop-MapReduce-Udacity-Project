#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

#
# Question 2
# Find the highest individual sale by each store
#

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    # Ensure that list has 6 items
    if len(data) == 6:
        date, time, store, item, cost, payment = data

        # Print store name and cost of each sale
        print "{0}\t{1}".format(store, cost)