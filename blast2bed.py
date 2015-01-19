#!/usr/bin/python
#
# convert a blastn outfmt=6 file to BED format, taking some static values on the command line

import sys
import datetime

def main():

    if len(sys.argv)!=2:
        print "blast2bed.py <blast-file>"
        sys.exit(0)

    filename = sys.argv[1]

    f = open(filename, 'rU')

    for line in f:
        chunks = line.split('\t')
        name = chunks[0]
        chromosome = chunks[1]
        match = chunks[2]
        if int(chunks[8])<int(chunks[9]):
            strand = '+'
            sstart = int(chunks[8]) - 1
            send = int(chunks[9])
        else:
            strand = '-'
            sstart = int(chunks[9]) - 1
            send = int(chunks[8])
        evalue = chunks[10]
        print chromosome+'\t'+str(sstart)+'\t'+str(send)+'\t'+name+'\t'+match+'\t'+strand
        
    f.close()

if __name__ == '__main__':
    main()
