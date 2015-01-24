#! /usr/bin/python
#
# file read test
#

def fileRead(fileName) :
    fr = open(fileName)
    for line in fr :
        print line

if __name__ == "__main__" :
    fileRead("abalone.data")
