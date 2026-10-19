#!/usr/bin/env bash
set -euo pipefail

dir=$1
jobs=${2:-$(nproc)}

count_one() {
    local f=$1 lines
    lines=$(gzip -dc "$f" | wc -l)
    printf '%s\t%d\n' "$(basename "$f")" $((lines / 4))
}
export -f count_one

printf 'file\treads\n'
printf '%s\0' "$dir"/*.fastq.gz | parallel -0 -j "$jobs" count_one {} | sort
