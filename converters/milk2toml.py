#!/bin/python

import sys
import re


def milk2toml():
    entries = {}

    line_re = re.compile("((?P<field>.*?)(?P<number>[0-9]*)\s*=(?P<content>.*))|(\[(?P<header>.*)\])")

    for line in sys.stdin.readlines():
        m = line_re.match(line)
        field, number, content, header = m.group('field', 'number', 'content', 'header')

        if header:
            entries[header]=None
        elif len(number) > 0 and field.find("code") == -1:
            # note: find('code') above is to handle shapecode_r2
            entries.setdefault(field, []).append(content)
        else:
            entries[field] = content

    for k,v in entries.items():
        if v == None:
            print(f"[{k}]")
        elif isinstance(v, list):
            print(f"{k}='''")
            for l in v:
                print(f"    {l}")
            print(f"'''")
        else:
            print(f"{k}={v}")

if __name__ == '__main__':
    milk2toml()
