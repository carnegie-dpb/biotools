# biotools
Scripts and other software written for bioinformatics work at the Carnegie Institution for Science Department of Plant Biology

bedpe2gff3.py - converts a BEDPE file to GFF3, splitting the paired reads into consecutive lines. Supports the extra 6 columns provided by the molpopgen/pecnv workflow. The source, assembly and feature values are entered on the command line.

blast2gff3.py - converts a BLASTN output file in outfmt=6 format into a GFF3 file. The source, assembly and feature values are entered on the command line.
