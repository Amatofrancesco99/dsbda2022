#!/usr/bin/env python3

import sys

sep = '$'

appid = None

for line in sys.stdin:
    # Remove the newline character at the end of the line and split the line to
    # get the values of its fields
    line = line.rstrip()
    fields = line.split('\t')

    # Also split the first combined field that contains both appid and steamid
    fields = fields[0].split(sep) + fields[1:]

    if fields[1] == '-':
        # This is a line of the preprocessed games dataset
        appid = fields[0]
        game_data = '\t'.join(fields[3:])
    elif fields[0] == appid:
        # This is a line of the projected reviews dataset and its appid is the
        # same of the latest encountered line of the preprocessed games dataset
        print('\t'.join(fields[:3]) + '\t' + game_data)
