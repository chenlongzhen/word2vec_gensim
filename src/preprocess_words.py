#!/usr/bin/env python
#encoding=utf-8
import re
import sys

input = sys.argv[1]
output = sys.argv[2]

with open(input,'r') as infile, open(output,'w') as outfile:
    for index,line in enumerate(infile):
        if index % 100000 == 0:
            print("processing {} line...".format(index))
        m = re.findall(u'[\w+]',line) # 去除字符
        new_line = ''.join(m)
        new_line = new_line.replace('nbsp','') # 去除nbsp
        new_line = new_line.lower()
        outfile.write(new_line.strip()+'\n')

#python preprocess_words.py ../data/article ../data/out
