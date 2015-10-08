#!/usr/bin/python
#
# Extract a GFF3 file from a PSL file, usually created by blat.
# Each block is written as a separate GFF feature.
#

import sys
import datetime

if len(sys.argv)!=5:
    print "psl2gff.py <psl-file> <source> <assembly> <feature>"
    sys.exit(0)

filename = sys.argv[1]
source = sys.argv[2]
assembly = sys.argv[3]
feature = sys.argv[4]

f = open(filename, 'rU')

print "##gff-version 3"

for line in f:
    chunks = line.rstrip().split('\t')
    if chunks[0].isdigit() and len(chunks)==21:
        matches = int(chunks[0])
        misMatches = int(chunks[1])
        repMatches = int(chunks[2])
        nCount = int(chunks[3])
        qNumInsert = int(chunks[4])
        qBaseInsert = int(chunks[5])
        tNumInsert = int(chunks[6])
        tBaseInsert = int(chunks[7])
        strand = chunks[8]
        qName = chunks[9]
        qSize = int(chunks[10])
        qStart = int(chunks[11]) + 1
        qEnd = int(chunks[12])
        tName = chunks[13]
        tSize = int(chunks[14])
        tStart = int(chunks[15]) + 1
        tEnd = int(chunks[16])
        blockCount = int(chunks[17])
        blockSizes = chunks[18]
        qStarts = chunks[19]
        tStarts = chunks[20]
        # score covers the whole PSL record, repeated for each block output
        score = (float(matches)+float(repMatches))/(float(matches)+float(misMatches)+float(repMatches))*100
        # write out the blocks without the empty inserts, these are comma-separated with a final comma
        blockSizeChunks = blockSizes.split(',');
        tStartChunks = tStarts.split(',');
        for i in range(blockCount):
            # output a GFF line for this block
            blockTStart = int(tStartChunks[i]) + 1
            blockTEnd = int(tStartChunks[i]) + int(blockSizeChunks[i])
            print tName+'\t'+source+'\t'+feature+'\t'+str(blockTStart)+'\t'+str(blockTEnd)+'\t'+str(score)+'\t'+strand+'\t'+'.'+'\t'+'Name='+qName+';assembly_name='+assembly+';'

f.close()
