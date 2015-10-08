#!/usr/bin/python
#
# Converts a pecnv-output BEDPE file to GFF3 format containing estimated TE breakpoints.
#
# minreads = the minimum value of both nplus and nminus to warrent output to GFF3. Default=3 (Cottrell value).
#

import sys
import datetime

def main():

    if len(sys.argv)<5:
        print "pecnv2gff.py <pecnv-teclust-output> <source> <assembly> <feature> [minreads;3]"
        sys.exit(0)

    filename = sys.argv[1]
    source = sys.argv[2]
    assembly = sys.argv[3]
    feature = sys.argv[4]
    if len(sys.argv)==6:
        minreads = int(sys.argv[5])
    else:
        minreads = 3

    f = open(filename, "rU")

    print "##gff-version 3"

    for line in f:
        chunks = line.rstrip().split('\t')
        # standard BEDPE fields
        pchr = chunks[0]
        pfirst = int(chunks[1]) + 1
        plast = int(chunks[2])
        mchr = chunks[3]
        mfirst = int(chunks[4]) + 1
        mlast = int(chunks[5])
        name = chunks[6]
        score = chunks[7]
        strand1 = chunks[8]
        strand2 = chunks[9]
        # pecnv extra fields
        nplus = int(chunks[10])
        nminus = int(chunks[11])
        if (nplus>=minreads and nminus>=minreads):
            pdist = int(chunks[12])
            pin = int(chunks[13])
            mdist = int(chunks[14])
            mmin = int(chunks[15])
            # estimate the breakpoint
            if (not pin) and mmin:
                chrom = pchr
                breakpoint = plast + pdist - 1
            elif pin and (not mmin):
                chrom = mchr
                breakpoint = mfirst - mdist - 1
            elif (not pin) and (not mmin):
                chrom = pchr
                breakpoint = (plast+mfirst)/2
            else:
                breakpoint = 0
            # output if we got it
            if breakpoint>0:
                # put pecnv extras into GFF attributes
                extras = ""
                extras = extras + "nplus="+str(nplus)+";"
                extras = extras + "nminus="+str(nminus)+";"
                extras = extras + "pdist="+str(pdist)+";"
                extras = extras + "pin="+str(pin)+";"
                extras = extras + "mdist="+str(mdist)+";"
                extras = extras + "min="+str(mmin)+";"
                print chrom+'\t'+source+'\t'+feature+'\t'+str(breakpoint)+'\t'+str(breakpoint)+'\t'+score+'\t'+"."+'\t'+"."+'\t'+"ID="+name+";Name="+name+";assembly_name="+assembly+";"+extras

    f.close()

if __name__ == "__main__":
    main()

