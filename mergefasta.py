#!/usr/bin/python
#
# Strip headers from a multi-FASTA file, resulting in a single sequence. Each
# original sequence is separated by SEPARATOR.
#
# Also outputs a GFF file listing the locations of the original sequences in the merged FASTA file.
#
# input: a FASTA file
# output: merged.fasta
#         merged.gff

import sys

from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# Separator uses nine Ns, so as not to disrupt frame (if that mattered)
separator = "NNNNNNNNN" 

if len(sys.argv)!=3:
    print "mergefasta.py <accession id> <multi-fasta-file>"
    sys.exit(0)

accession = sys.argv[1]
input_fasta = sys.argv[2]

# initialize the big merged sequence and separator
merged_seq = Seq("", IUPAC.unambiguous_dna)
separator_seq = Seq(separator, IUPAC.unambiguous_dna)

# initialize the GFF stuff
separator_length = len(separator);
end = 0;
gff = open("merged.gff", "w")
gff.write("##gff-version 3\n");

# each input sequence is loaded as a SeqRecord and added to the merged sequence while outputting a GFF line
input_handle = open(input_fasta, "rU")
for record in SeqIO.parse(input_handle,"fasta") :
##    merged_seq += separator_seq + record.seq
    # GFF record
    start = end + separator_length + 1
    end = start + len(record.seq) - 1
    attributes = "Name="+record.id+";"
    gff_record = accession + '\t' + "source" + '\t' + "type" + '\t' + str(start) + '\t' + str(end) + '\t' + "." + '\t' + "+" + '\t' + "." + '\t' + attributes
    gff.write(gff_record+'\n')
input_handle.close()
gff.close()

# merged sequence record
##merged_record = SeqRecord(merged_seq, id=accession, name="name here", description="description here")

# output the merged sequence
##output_handle = open("merged.fasta", "w")
##SeqIO.write(merged_record, output_handle, "fasta")
##output_handle.close()

