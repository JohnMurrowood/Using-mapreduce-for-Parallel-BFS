#!/usr/bin/env python3
# Assignmnet 2 Parallel Breadth-First-Search Mapper
import sys

def reducer():
    dist_dict = {}
    for line in sys.stdin:
        try:
            node, dist = line.split(' ')
            if node in dist_dict.keys():
                if dist < dist_dict[node]:
                    dist_dict[node] = dist
            else:
                try:
                    int(node)
                    dist_dict[node] = dist
                except:
                    pass
        except:
            pass

    for key in dist_dict:
        print(key+': '+str(dist_dict[key]), end='')
            
            

if __name__ == "__main__":
    reducer()