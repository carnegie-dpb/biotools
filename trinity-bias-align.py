#!/usr/bin/python
#
# Reverse complement Trinity contigs for which the "center of depth" (the base about which the total coverage is 50/50)
# is on the 3' end of the sequence. This orients the contigs correctly for a 3'-biased RNA-seq dataset.
# 
# The resulting orientation is often incorrect, however, since many transcripts will actually have more reads on the
# 5' end, especially contigs that lie near the 5' end of a gene and have low coverage. Furthermore, one often has a 
# gene which composes two Trinity contigs, say TR1000|c0_g1_i1 and TR1000|c1_g1_i1; this routine may reverse complement
# one of those (because it lies closer to the 3' end of the gene and has better stats) while not complementing the 
# other one. My experience is that Trinity will more often give those two contigs the same orientation, even though 
# it is wrong 50% of the time.
#
# input:  Trinity.fasta
#         bowtie.csorted.bam.depth (output from samtools depth bowtie.csorted.bam > bowtie.csorted.bam.depth)
#
# output: Trinity.bias-align.fasta
#
# Sam Hokin, shokin@carnegiescience.edu

import sys

from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

# assume file names (for now)
trinity_fasta_file = "Trinity.fasta"
bam_depth_file = "bowtie.csorted.bam.depth"

# I/O
trinity_fasta_handle = open(trinity_fasta_file, "rU")
bam_depth_handle = open(bam_depth_file, "rU")
trinity_bias_align_handle = open("Trinity.bias-align.fasta", "w")

# init
id = ""
depth_total = 0
base_depth = 0
count = 0

# each input contig sequence is loaded as a SeqRecord
for contig in SeqIO.parse(trinity_fasta_handle, "fasta") :
    description_parts = contig.description.split();
    length = int(description_parts[1].split("=")[1])
    # get corresponding depth lines
    for line in bam_depth_handle :
        parts = line.split('\t')
        id = parts[0]
        base = int(parts[1])
        depth = int(parts[2])
        if id==contig.id :
            count += 1
            depth_total += depth
            base_depth += base*depth
        else :
            # process contig
            if count>0 :
                center_of_depth = float(base_depth)/float(depth_total)
                if center_of_depth<float(length)/2.0 :
                    # reverse complement
                    contig = contig.reverse_complement(id=True, name=True, description=True, features=True, annotations=True, letter_annotations=True, dbxrefs=True)
            # output 
            SeqIO.write(contig, trinity_bias_align_handle, "fasta")
            # initialize values for next contig, assumed to match with the next one in Trinity.fasta
            count = 0
            depth_total = depth
            base_depth = base*depth
            break

# handle the very last one
if count>0 :
    center_of_depth = float(base_depth)/float(depth_total)
    if center_of_depth<float(length)/2.0 :
        contig = contig.reverse_complement(id=True, name=True, description=True, features=True, annotations=True, letter_annotations=True, dbxrefs=True)
SeqIO.write(contig, trinity_bias_align_handle, "fasta")

# wrap up
trinity_fasta_handle.close()
bam_depth_handle.close()
trinity_bias_align_handle.close()
