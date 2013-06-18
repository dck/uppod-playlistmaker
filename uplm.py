#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

allowedExt = [".mp3"]

def getMusicFileIter(allowedExt):
    def iterFunc(dir):
        for r, dirs, files in os.walk(dir):
            for f in files:
                if os.path.splitext(f)[1] in allowedExt:
                    yield os.path.abspath(f)
    return iterFunc


def usage():
    s = ("Usage: {} <folder> <file>\n"
        "folder - the directory where mp3 files are located\n"
        "file - output file")
    print s.format(sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    iterMusicFiles = getMusicFileIter(allowedExt)
    for f in iterMusicFiles(sys.argv[1]):
        print f
