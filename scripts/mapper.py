#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Remove the newline character at the end of the line and split the line to get the values of
    # its fields
    line = line.rstrip()
    fields = line.split('\t')

    if len(fields) == 3:
        # This is a line of the projected reviews dataset
        out_line = line + '\t-' * 29
    else:
        # This is a line of the preprocessed games dataset
        out_line = fields[0] + '\t-\t-\t' + '\t'.join(fields[1:])

    print(out_line)
