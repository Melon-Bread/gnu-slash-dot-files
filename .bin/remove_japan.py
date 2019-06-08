#!/usr/bin/env python3

import os

for file in os.listdir('./'):
    if '(Japan)' in file:
        print(f"Removing {file}...")
        os.remove(file)
    else:
        print(f"Skipping {file}...")
