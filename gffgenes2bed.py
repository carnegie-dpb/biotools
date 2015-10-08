#!/usr/bin/python
#
# Selects the lines with protein-coding genes from the input GFF file on stdin and outputs the chr, start and end, tab separated (so, first three columns of a BED file). 
#

import sys

for line in sys.stdin:
    chunks = line.rstrip().split('\t')
    if len(chunks)>=5:
        if chunks[1]=="protein_coding" and chunks[2]=="gene":
            print chunks[0]+"\t"+chunks[3]+"\t"+chunks[4]






