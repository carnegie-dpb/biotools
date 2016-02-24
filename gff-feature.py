#!/usr/bin/python
#
# extract a single feature from a GFF file presumably containing many features

import sys

if len(sys.argv)!=4:
    print "gff_feature.py file.gff source feature"
    sys.exit(0)

filename = sys.argv[1]
source = sys.argv[2]
feature = sys.argv[3]

print "##gff-version 3"

f = open(filename, 'rU')
for line in f:
    chunks = line.split('\t')
    if len(chunks)==9 and chunks[1]==source and chunks[2]==feature: print line,

f.close()
