# Using-mapreduce-for-Parallel-BFS

This is a mapreduce program done in python to perform a parallel Breadth-First-Search on a given graph which finds the distance of each node from a source node. 

Files:

graph.txt: contains and example graph.
distance.txt: contains and example of the distance of every node from the source.
mapper.py: Python code for mapper
reducer.py: Python code for reducer
reader.py: python code to check for termination condition for while loop in run.sh
run.sh: File used to run code in hadoop
hadoop-streaming-3.1.4.jar: hadoop streaming file


