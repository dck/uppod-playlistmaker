#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def usage():
    s = ("Usage: {} <folder> <file>\n"
        "folder - the directory where mp3 files are located\n"
        "file - output file")
    print s.format(sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)