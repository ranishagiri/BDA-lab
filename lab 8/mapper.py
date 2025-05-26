#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    words = re.findall(r'\w+', line.lower())  # normalize case
    for word in words:
        print(f"{word}\t1")
