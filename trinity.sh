#!/bin/sh
export JAVA_HOME=/usr/java/default
export PATH=$JAVA_HOME/bin:$PATH
~/trinityrnaseq/Trinity --seqType fq --max_memory 32G --CPU 6 --left $1  --right $2
