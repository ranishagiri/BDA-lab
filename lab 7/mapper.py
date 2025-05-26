#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    parts = line.split()
    date, temp = parts

    temp = float(temp)
    print(f"{date}\t{temp}")
