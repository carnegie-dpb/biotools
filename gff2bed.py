#!/usr/bin/python
#
# convert a GFF3 file to BED6 format, placing the desired attribute into the BED name column, or ID if that attribute is missing.

import sys
import datetime

if len(sys.argv)!=3:
    print "gff2bed.py <GFF3 file> <naming attribute>"
    sys.exit(0)

filename = sys.argv[1]
attribute = sys.argv[2].lower()

f = open(filename, 'rU')

for line in f:
    if not line.startswith("#"):
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
            if parts[0].lower()==attribute:
                name = parts[1].rstrip()
	    if parts[0].lower()=='id':
		id = parts[1]
        if name!="":
            print chrom+'\t'+str(start-1)+'\t'+str(end)+'\t'+name+'\t'+score+'\t'+strand
        else:
            print chrom+'\t'+str(start-1)+'\t'+str(end)+'\t'+id+'\t'+score+'\t'+strand

f.close()
