#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import os
import json

allowedExt = [".mp3"]

def getMusicFileIter(allowedExt):
    def iterFunc(dir):
        for r, dirs, files in os.walk(dir):
            for f in files:
                if os.path.splitext(f)[1] in allowedExt:
                    fileName = os.path.join(r, f)
                    yield (f, os.path.abspath(fileName))
    return iterFunc


def usage():
    s = ("Usage: {} <folder> <file>\n"
        "folder - the directory where mp3 files are located\n"
        "file - output file")
    print(s.format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    jsonObj = {"playlist": []}
    iterMusicFiles = getMusicFileIter(allowedExt)
    for name, path in iterMusicFiles(sys.argv[1]):
        d = {
            "comment": name,
            "file": path
        }
        jsonObj["playlist"].append(d)

    try:
        with open(sys.argv[2], "w") as fh:
            json.dump(jsonObj, fh, indent=4, ensure_ascii=False)
    except IOError:
        sys.stderr.write("Error. Can't write to {}\n".format(sys.argv[2]))
        
