#!/usr/bin/env python3
# Assignmnet 2 Parallel Breadth-First-Search Mapper

import sys
# get initial centroids from a txt file and add them in an array
def getDistances(filepath):
    dictionary = {}
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    line = line.strip()
                    cord = line.split(':')
                    dictionary[cord[0]] = cord[1].strip()
                except:
                    break
            else:
                break
            line = fp.readline()
    fp.close()
    return dictionary

def mapper(dictionary):
    for line in sys.stdin:
        line = line.strip()
        cord = line.split(':')
        try:
            c = cord[1].strip()
            node = cord[0]
            print("Source: "+node)
            print(node, dictionary[node])
            if c != 'none':
                children = c.split(' ')
                if int(dictionary[node]) < 9999:
                    for c in children:
                        print(c, int(dictionary[node]) + 1)
                else:
                    for c in children:
                        print(c, dictionary[c])
            else:
                pass
        except:
            pass

if __name__ == "__main__":
    distances = getDistances('distance.txt')
    mapper(distances)

