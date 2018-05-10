#!/bin/bash

for ((I=0; I<$1; I++))
do
	SEED=$( echo $SEED$(date)$2 | md5sum )
	./keytest.py $SEED >> out.txt
done
