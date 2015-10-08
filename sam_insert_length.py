#!/usr/bin/python
#
# Calculates the mean insert length for left and right reads fully mapped to the reference in the SAM file on stdin
#

import sys
import time

if len(sys.argv)<3:
    print "bam_insert_length.py <readbp> <minMAPQ> < bamfile"
    sys.exit(0)

readbp = int(sys.argv[1])
minMAPQ = int(sys.argv[2])

countPlus = 0
countMinus = 0
minTLENPlus = 1000000
maxTLENPlus = 0
minTLENMinus = 1000000
maxTLENMinus = 0
totalTLENPlus = 0
totalTLENMinus = 0

goodCIGAR = str(readbp)+"M"

for line in sys.stdin:
    chunks = line.rstrip().split('\t')
    if len(chunks)>=11:
        MAPQ = int(chunks[4])
        CIGAR = chunks[5]
        if CIGAR==goodCIGAR and MAPQ>minMAPQ:
            TLEN = int(chunks[8])
            if TLEN>0:
                countPlus += 1
                totalTLENPlus += TLEN
                if TLEN>maxTLENPlus: maxTLENPlus = TLEN
                if TLEN<minTLENPlus: minTLENPlus = TLEN
            if TLEN<0:
                countMinus += 1
                totalTLENMinus += TLEN
                if abs(TLEN)>maxTLENMinus: maxTLENMinus = abs(TLEN)
                if abs(TLEN)<minTLENMinus: minTLENMinus = abs(TLEN)
        if countPlus%10000==0 and countPlus>0:
            print '\r',
            time.sleep(0.3)
            print str(countPlus)+" qualified reads",
            sys.stdout.flush()

print ""
print "Forward matches:"+str(countPlus)+"\tAve TLEN="+str(float(totalTLENPlus)/float(countPlus))+"\tMax TLEN="+str(maxTLENPlus)+"\tMin TLEN="+str(minTLENPlus)
print "Reverse matches:"+str(countMinus)+"\tAve TLEN="+str(float(-totalTLENMinus)/float(countMinus))+"\tMax TLEN="+str(maxTLENMinus)+"\tMin TLEN="+str(minTLENMinus)


