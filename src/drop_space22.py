#!/usr/bin/python

import sys
S_PATH = sys.path[0]
D_PATH = S_PATH + "/../data/"

inf = sys.argv[1]
outf = D_PATH + "seg_end.data"

with open(inf,'r') as ifile ,open(outf,'w') as ofile:
    for line in ifile:
        ofile.write(' '.join(line.split() + "\n")
