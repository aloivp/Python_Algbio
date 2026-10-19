#!/usr/bin/env bash

dir=$1

for f in "$dir"/*.fastq.gz; do
    lines=$(gzip -dc "$f" | wc -l)
    echo "$(basename "$f") $((lines / 4))"
done