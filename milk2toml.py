#!/bin/python

import sys
import re
import toml


def milk2toml():
    entries = {}

    line_re = re.compile("((?P<field>.*?)(?P<number>[0-9]*)\s*=(?P<content>.*))|(\[(?P<header>.*)\])")

    for line in sys.stdin.readlines():
        m = line_re.match(line)
        field, number, content, header = m.group('field', 'number', 'content', 'header')

        if header:
            entries[header]=None
        elif len(number) > 0:
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

def dumpmilk(d):
    for k,v in d.items():
        if isinstance(v,dict):
            print(f"[{k}]")
            dumpmilk(v)
        elif isinstance(v, str):
            for i,l in enumerate(v.split('\n')[0:-1]):
                print(f"{k}{i+1}={l.strip()}")
        elif isinstance(v,float):
            print(f"{k}={v:.6f}")
        else:
            print(f"{k}={v}")

def toml2milk():
    dumpmilk(toml.load(sys.stdin))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--decode':
        toml2milk()
    else:
        milk2toml()
