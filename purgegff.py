#!/usr/bin/python
#
# Purge a particular source:feature combination from a GFF file.
#

import sys

if len(sys.argv)!=4:
    print "purgegff.py <gff-file> <source> <feature>"
    sys.exit(0)

filename = sys.argv[1]
source = sys.argv[2]
feature = sys.argv[3]

f = open(filename, 'rU')

for line in f:
    chunks = line.rstrip().split('\t')
    if len(chunks)==9:
        if chunks[1]!=source and chunks[2]!=feature:
            print line,
    else:
        print line,

f.close()
        
