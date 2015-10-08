#!/usr/bin/python
#
# Outputs unique sequences from a FASTQ file to a FASTA file.
#
# Requires: BioPython

import sys
from Bio import SeqIO

if len(sys.argv)!=2:
    print "fastq2fasta.py <fastq-file>"
    sys.exit(0)
    
filename = sys.argv[1]
seq_list = []
    
for seq_record in SeqIO.parse(filename, "fastq"):
    if not str(seq_record.seq) in seq_list:
        seq_list.append(str(seq_record.seq))
        print '>'+seq_record.id+'\n'+str(seq_record.seq)

