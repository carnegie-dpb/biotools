#!/usr/bin/env python
#
# Counts the bases for each sequence in a FASTA file and spits them out along with the sequence record id, tab separated.
#
# Requires: BioPython

import sys
from Bio import SeqIO

def main():

    if len(sys.argv)!=2:
        print "countbases.py <fasta-file>"
        sys.exit(0)

    for seq_record in SeqIO.parse(sys.argv[1], "fasta"):
        print seq_record.id+"\t"+str(len(seq_record))

if __name__ == '__main__':
    main()
