#!/usr/bin/env python

import sys
import csv
class Mapper(object):

    def __init__(self, stream, sep ="\t"):
        self.stream =stream
        self.sep = sep

    def emit(self, key, key1,key2,key3, value):
        sys.stdout.write("%s%s%s%s%s%s\n" % (key,key1,key2,key3, self.sep, value))
    def map(self):
        reader = csv.reader(self.stream)
        for row in reader:
                self.emit(row[6],row[5],row[4],row[3],row[0])
if __name__ == '__main__':
    mapper = Mapper(sys.stdin)
    mapper.map()
