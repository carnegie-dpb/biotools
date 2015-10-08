#!/usr/bin/python
#
# Selects the lines with protein-coding genes from the input GFF file on stdin and outputs the chr, start and end, tab separated (so, first three columns of a BED file). 
#

import sys

if len(sys.argv)!=2:
    print "gffstats.py <gff-file>"
    sys.exit(0)

filename = sys.argv[1]
f = open(filename, 'rU')

d = dict()

for line in f:
    chunks = line.rstrip().split('\t')
    if len(chunks)>=5:
        seqname = chunks[0]
        source = chunks[1]
        feature = chunks[2]
        start = int(chunks[3])
        end = int(chunks[4])
        length = end - start + 1;
        key = seqname+'.'+source+'.'+feature;
        if key in d:
            d[key] += length
        else:
            d[key] = length

f.close()

for key, value in sorted(d.items()): # Note the () after items!
    print key+":"+str(value)



