#!/usr/bin/python
#
# convert a GFF3 file to BED6 format, placing the attribute Name into the BED name column.

import sys
import datetime

if len(sys.argv)!=2:
    print "gff2bed.py <GFF3 file>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')

for line in f:
    chunks = line.split('\t')
    chrom = chunks[0]
    source = chunks[1]
    feature = chunks[2]
    start = int(chunks[3])
    end = int(chunks[4])
    score = chunks[5]
    strand = chunks[6]
    phase = chunks[7]
    attributes = chunks[8]
    pieces = attributes.split(';')
    name = ""
    for piece in pieces:
        parts = piece.split('=')
        if parts[0].lower()=='name':
            name = parts[1]
    if name!="":
        print chrom+'\t'+str(start-1)+'\t'+str(end)+'\t'+name+'\t'+score+'\t'+strand
    else:
        print chrom+'\t'+str(start-1)+'\t'+str(end)+'\t'+"."+'\t'+score+'\t'+strand

f.close()
