#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

#
# Question 1
# Get the sales breakdown by product category
#

import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    # Ensure there are 6 items on the list
    if len(data) == 6:
        date, time, store, item, cost, payment = data

        # Print only product category(item) and cost
        print "{0}\t{1}".format(item, cost)
