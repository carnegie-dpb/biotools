#!/usr/bin/python
#
# cull only the best (lowest e-value) hit from each query in a blastn outfmt=6 file. Assumes that
# blast file has best match first, as it normally does.

import sys
import datetime

if len(sys.argv)!=2:
    print "blastcull.py <blast-outfmt6>"
    sys.exit(0)

filename = sys.argv[1]

f = open(filename, 'rU')

queries = list()

for line in f:
    chunks = line.split('\t')
    query = chunks[0]
    if query not in queries:
        queries.append(query)
        print line,

f.close()
