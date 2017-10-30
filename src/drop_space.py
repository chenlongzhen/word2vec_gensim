#!/usr/bin/python

import sys,re
S_PATH = sys.path[0]
D_PATH = S_PATH + "/../data/"

inf = sys.argv[1]
outf = D_PATH + "seg_end.data"

ifile = open(inf,'rb')
ofile = open(outf,'wb')
for line in ifile:
    line2 = line.replace('/','')
    new_line = ' '.join(line2.split()) + "\n"
    ofile.write(new_line)
ifile.close()
ofile.close()
