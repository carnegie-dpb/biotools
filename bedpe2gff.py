#!/usr/bin/python
#
# Condenses the huge merged semicolon-separated names resulting from a bedtools merge -nms. Typically they're similar, so we'll trim the variations off.
#

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
        if chr1!='.':
            print chr1+'\t'+source+'\t'+feature+'\t'+str(start1)+'\t'+str(end1)+'\t'+score+'\t'+strand1+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'
        if chr2!='.':
            print chr2+'\t'+source+'\t'+feature+'\t'+str(start2)+'\t'+str(end2)+'\t'+score+'\t'+strand2+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'
    f.close()

if __name__ == '__main__':
  main()

