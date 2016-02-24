#!/usr/bin/python
#
# list out the unique features contained in a GFF3 file

import sys
import datetime

if len(sys.argv)!=2:
    print "gff-list-features.py <GFF3 file>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')

featureList = []

for line in f:
    if line[0]!="#":
        chunks = line.split('\t')
        seqid = chunks[0]
        source = chunks[1]
        feature = chunks[2]
        start = chunks[3]
        end = chunks[4]
        score = chunks[5]
        strand = chunks[6]
        phase = chunks[7]
        attributes = chunks[8]
        if feature not in featureList:
            print feature
            featureList.append(feature)

f.close()
