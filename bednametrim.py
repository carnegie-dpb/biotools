#!/usr/bin/python
#
# Condenses the huge merged semicolon-separated names resulting from a bedtools merge -nms. Typically they're similar, so we'll trim the variations off.
# Name parts are concatenated with "|" because a semicolon conflicts with conversion to GFF3.
#
# bed|gff = output file format; if gff, source and feature will be set to "source" and "feature", update them yourself later

import sys
import datetime

import itertools


def main():

    if len(sys.argv)!=3:
        print "bednametrim.py <bed|gff> <input-bed-file>"
        sys.exit(0)

    outfmt = sys.argv[1]
    filename = sys.argv[2]

    f = open(filename, "rU")

    # need a counter to make sure GFF IDs are unique
    count = 0
    
    for line in f:
        count = count + 1
        chunks = line.rstrip().split("\t")
        # mandatory fields
        chrom = chunks[0]
        start = int(chunks[1])
        end = int(chunks[2])
        # optional fields, but the whole point of this is to condense names, so they better be there!
        name = chunks[3]
        if len(chunks)>4:
            score = round(float(chunks[4]),1)
        if len(chunks)>5:
            strand = chunks[5]
            # GFF only allows +/-/. for strand value, BED doesn't care
            if outfmt=="gff" and strand!="+" and strand!="-":
                strand = "."
        # find the common part of the names
        names = name.rstrip().split(";")
        if len(names)==1:
            name = names[0]
        else:
            name = names[0]
            for i in range(1,len(names)):
                name = ''.join(el[0] for el in itertools.takewhile(lambda t: t[0]==t[1], zip(name, names[i])))
            if len(name)<3:
                # we've got too little in common, switch to concatenating unique first three letters separated by pipes
                savedParts = list()
                for i in range(0, len(names)):
                    part = names[i][:3]
                    if len(part)>0 and part not in savedParts:
                        savedParts.append(part)
                    name = "|".join(savedParts)
            # trim trailing underscore
            if name[-1:]=="_":
                name = name[:-1]
            # OK, really picky now: trim trailing _AC
            if name[-3:]=="_AC":
                name = name[:-3]
        # output to BED or GFF file
        if outfmt=="bed":
            if len(chunks)==4:
                print chrom+"\t"+str(start)+"\t"+str(end)+"\t"+name
            elif len(chunks)==5:
                print chrom+"\t"+str(start)+"\t"+str(end)+"\t"+name+"\t"+str(score)
            else:
                print chrom+"\t"+str(start)+"\t"+str(end)+"\t"+name+"\t"+str(score)+"\t"+strand
        elif outfmt=="gff":
            print chrom+"\t"+"source"+"\t"+"feature"+"\t"+str(start+1)+"\t"+str(end)+"\t"+str(score)+"\t"+strand+"\t"+"."+"\t"+"ID="+str(count)+";Name="+name
    f.close()

if __name__ == "__main__":
    main()

