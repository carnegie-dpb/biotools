#!/usr/bin/python
#
# Creates a GTF representation of a multi-fasta file, one line per sequence, giving the name and length.
#
# Requires: BioPython

import sys
from Bio import SeqIO

if len(sys.argv)!=4:
    print "fasta2gft.py <fasta-file> <source> <feature>"
    sys.exit(0)
    
filename = sys.argv[1]
source = sys.argv[2]
feature = sys.argv[3]
    
for seq_record in SeqIO.parse(filename, "fasta"):
    print seq_record.id+'\t'+source+'\t'+feature+'\t'+"1"+'\t'+str(len(seq_record))+'\t.\t+\t.\t'+"gene_id "+seq_record.id+";"

