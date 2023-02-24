#!/usr/bin/env python3
# reader function to check if output and input are the same
from mapper import getDistances

def checkDistances(distance, distance1):
    diff = 1
    for key in distance:
        if distance[key] != distance1[key]:
            diff = 0
    if diff == 1:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    distance = getDistances('distance.txt')
    distance1 = getDistances('distance1.txt') 

    checkDistances(distance, distance1)