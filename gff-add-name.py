#!/usr/bin/python
#
# Add the NAME attribute to a GFF file already containing ID attributes.

import sys
import datetime

if len(sys.argv)!=2:
    print "gff_add_name.py <GFF3 file>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')

for line in f:
    chunks = line.split('\t')
    seq = chunks[0]
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
        if parts[0].upper()=='ID':
            name = parts[1]
            # sometimes we have :subname, which we'll drop
            #subparts = fullname.split(":");
            #name = subparts[0]
    print seq+'\t'+source+'\t'+feature+'\t'+str(start)+'\t'+str(end)+'\t'+score+'\t'+strand+'\t'+phase+'\t'+"Name="+name+";"+attributes,

f.close()
