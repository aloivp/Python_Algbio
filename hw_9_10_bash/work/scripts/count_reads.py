#!/usr/bin/env python3
import gzip
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def count_reads(path):
    with gzip.open(path, "rt") as fh:
        lines = sum(1 for _ in fh)
    return path.name, lines // 4


if __name__ == "__main__":
    directory = Path(sys.argv[1])
    jobs = int(sys.argv[2]) if len(sys.argv) > 2 else os.cpu_count()
    files = sorted(directory.glob("*.fastq.gz"))

    print("file\treads")
    with ProcessPoolExecutor(max_workers=jobs) as pool:
        for name, n in pool.map(count_reads, files):
            print(f"{name}\t{n}")
