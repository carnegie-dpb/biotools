#!/usr/bin/python
#
# Converts a BEDPE file to GFF3 format, taking some static values on the command line and splitting the reads into two consecutive features
# Only features with chromosome!='.' are output.
#
# - If the BEDPE has 16 columns, it is assumed to be from molpopgen/pecnv and those extra six columns are appended as attributes.

import sys
import datetime

def main():

    if len(sys.argv)!=5:
        print "bedpe2gff.py <bedpe-file> <source> <assembly> <feature>"
        sys.exit(0)

    filename = sys.argv[1]
    source = sys.argv[2]
    assembly = sys.argv[3]
    feature = sys.argv[4]

    f = open(filename, 'rU')

    print "##gff-version 3"
    print "##written by bedpe2gff.py from a BEDPE file at "+datetime.datetime.now().isoformat()

    for line in f:
        chunks = line.rstrip().split('\t')
        chr1 = chunks[0]
        start1 = int(chunks[1]) + 1
        end1 = int(chunks[2])
        chr2 = chunks[3]
        start2 = int(chunks[4]) + 1
        end2 = int(chunks[5])
        name = chunks[6]
        score = chunks[7]
        strand1 = chunks[8]
        strand2 = chunks[9]
        # add pecnv extra attributes
        extras = ''
        if len(chunks)==16:
            extras = extras + 'nplus='+chunks[10]+';'
            extras = extras + 'minus='+chunks[11]+';'
            extras = extras + 'pdist='+chunks[12]+';'
            extras = extras + 'pin='+chunks[13]+';'
            extras = extras + 'mdist='+chunks[14]+';'
            extras = extras + 'min='+chunks[15]+';'
        if chr1!='.':
            print chr1+'\t'+source+'\t'+feature+'\t'+str(start1)+'\t'+str(end1)+'\t'+score+'\t'+strand1+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'+extras
        if chr2!='.':
            print chr2+'\t'+source+'\t'+feature+'\t'+str(start2)+'\t'+str(end2)+'\t'+score+'\t'+strand2+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'+extras
    f.close()

if __name__ == '__main__':
  main()

