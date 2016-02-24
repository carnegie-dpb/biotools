#!/usr/bin/python
#
# rename a given seqid to a new seqid in a GFF3 file

import sys
import datetime

if len(sys.argv)!=4:
    print "gff-rename-seq.py <GFF3 file> <old_seqid> <new_seqid>"
    sys.exit(0)

filename = sys.argv[1]
old_seqid = sys.argv[2]
new_seqid = sys.argv[3]

f = open(filename, 'rU')

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
        if seqid==old_seqid:
            seqid=new_seqid
        print seqid+'\t'+source+'\t'+feature+'\t'+start+'\t'+end+'\t'+score+'\t'+strand+'\t'+phase+'\t'+attributes,
    else:
        print line,

f.close()
