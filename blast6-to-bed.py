#!/usr/bin/python
#
# convert a blastn outfmt=6 file to BED6 format.

import sys
import datetime

if len(sys.argv)!=2:
    print "blast6-to-bed.py <blast-fmt6-file>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')
    
for line in f:
    chunks = line.split('\t')
    name = chunks[0]
    chromosome = chunks[1]
    if int(chunks[8])<int(chunks[9]):
        strand = '+'
        sstart = int(chunks[8])-1
        send = int(chunks[9])
    else:
        strand = '-'
        sstart = int(chunks[9])-1
        send = int(chunks[8])
    evalue = chunks[10]
    print chromosome+'\t'+str(sstart)+'\t'+str(send)+'\t'+name+'\t'+evalue+'\t'+strand

f.close()
