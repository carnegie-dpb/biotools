#!/usr/bin/python
#
# count hits per target in a BED file

import sys
import datetime

if len(sys.argv)!=2:
    print "bed-counter.py <BED6 file>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')

lastName = ""
count = 0
for line in f:
    chunks = line.split('\t')
    name = chunks[0]
    start = int(chunks[1])
    end = int(chunks[2])
    source = chunks[3]
    score = chunks[4]
    strand = chunks[5]
    if name!=lastName:
        if lastName!="": print lastName+'\t'+str(count)
        lastName = name
        count = 1
    else:
        count += 1

# last one
print lastName+'\t'+str(count)

f.close()
