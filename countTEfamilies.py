#!/usr/bin/python
#
# Count the net bases covered per TE family in a Cufflinks isoforms.fpkm_tracking file

import sys

# assume local file for now
filename = "isoforms.fpkm_tracking"


f = open(filename, 'rU')
    
line_num = 0
last_TE_family = ""
total_bases = 0

for line in f:
    line_num += 1
    if line_num>1:
        chunks = line.split('\t')
        # cufflinks isoforms.fpkm_tracking fields
        tracking_id = chunks[0]
        class_code = chunks[1]
        nearest_ref_id = chunks[2]
        gene_id = chunks[3]
        gene_short_name = chunks[4]
        tss_id = chunks[5]
        locus = chunks[6]
        length = int(chunks[7])
        coverage = float(chunks[8])
        FPKM = float(chunks[9])
        FPKM_conf_lo = float(chunks[10])
        FPKM_conf_hi = float(chunks[11])
        FPKM_status = chunks[12]
        # parse TE family
        locus_parts = locus.split("_")
        TE_family = locus_parts[0]
        if TE_family!=last_TE_family:
            if total_bases>0: print last_TE_family+'\t'+str(total_bases)
            last_TE_family = TE_family
            total_bases = length*coverage
        else:
            total_bases += length*coverage

print last_TE_family+"\t"+str(total_bases)

f.close()
