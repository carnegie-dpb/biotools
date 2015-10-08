#!/usr/bin/python
#
# convert a BED6 file to GFF3 format, taking the source, assembly and feature for the GFF file from the command line.

import sys
import datetime

if len(sys.argv)!=5:
    print "bed2gff.py <BED6 file> <source> <assembly> <feature>"
    sys.exit(0)

filename = sys.argv[1]
source = sys.argv[2]
assembly = sys.argv[3]
feature = sys.argv[4]

f = open(filename, 'rU')

print "##gff-version 3"

lastStart = 0
lastEnd = 0
lastName = ""
for line in f:
    chunks = line.split('\t')
    chrom = chunks[0]
    start = int(chunks[1])
    end = int(chunks[2])
    name = chunks[3]
    score = chunks[4]
    strand = chunks[5]
    if start!=lastStart or end!=lastEnd or name!=lastName:
        print chrom+'\t'+source+'\t'+feature+'\t'+str(start+1)+'\t'+str(end)+'\t'+score+'\t'+strand+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'
    # save name, start, end since often have multiple lines, hopefully sorted
    lastStart = start
    lastEnd = end
    lastName = name
f.close()
