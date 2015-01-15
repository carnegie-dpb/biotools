#!/usr/bin/python
#
# convert a blastn outfmt=6 file to GFF3 format, taking some static values on the command line

import sys
import datetime

def main():

    if len(sys.argv)!=5:
        print "blast2gff.py <blast-file> <source> <assembly> <feature>"
        sys.exit(0)

    filename = sys.argv[1]
    source = sys.argv[2]
    assembly = sys.argv[3]
    feature = sys.argv[4]

    f = open(filename, 'rU')

    print "##gff-version 3"
    print "##written by blast2gff.py from BLAST outfmt=6 file at "+datetime.datetime.now().isoformat()
    
    for line in f:
        chunks = line.split('\t')
        name = chunks[0]
        chromosome = chunks[1]
        if chunks[8]<chunks[9]:
            strand = '+'
            sstart = chunks[8]
            send = chunks[9]
        else:
            strand = '-'
            sstart = chunks[9]
            send = chunks[8]
        evalue = chunks[10]
        print chromosome+'\t'+source+'\t'+feature+'\t'+sstart+'\t'+send+'\t'+evalue+'\t'+strand+'\t'+'.'+'\t'+'Name='+name+';assembly_name='+assembly+';'
    f.close()

if __name__ == '__main__':
  main()
