#!/bin/bash
i=1
while :
do
	hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=1 \
    -D mapred.text.key.partitioner.options=-k1 \
    -file distance.txt \
    -file ./mapper.py \
    -mapper ./mapper.py \
    -file ./reducer.py \
    -reducer ./reducer.py \
    -input /graph.txt \
    -output /mapreduce-output$i \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
        
    rm -f distance1.txt
    hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance1.txt
	
    seeiftrue=`python reader.py` 
	
	if [ $seeiftrue = 1 ]
	then
		rm distance.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance.txt
		break
	else
		rm distance.txt
		hadoop fs -copyToLocal /mapreduce-output$i/part-00000 distance.txt
	fi
	i=$((i+1))
done

