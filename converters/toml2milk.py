import toml

import sys

def dumpmilk(d):
    for k,v in d.items():
        if isinstance(v,dict):
            print(f"[{k}]")
            dumpmilk(v)
        elif isinstance(v, str):
            for i,l in enumerate(v.split('\n')[0:-1]):
                print(f"{k}{i+1}={l}")
        elif isinstance(v,float):
            print(f"{k}={v:.6f}")
        else:
            print(f"{k}={v}")

def toml2milk():
    dumpmilk(toml.load(sys.stdin))

if __name__ == '__main__':
    toml2milk()

