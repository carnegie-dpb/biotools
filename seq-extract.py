#!/usr/bin/python
#
# Extract the desired sequence from a fasta file.
#
# Requires: BioPython

import sys
from Bio import SeqIO


if len(sys.argv)!=3:
    print "seq-extract.py <fasta-file> <seqid>"
    sys.exit(0)

seqid = sys.argv[2]

for record in SeqIO.parse(sys.argv[1], "fasta"):
    if record.id==seqid:
        print record.format("fasta")
        sys.exit(0)


