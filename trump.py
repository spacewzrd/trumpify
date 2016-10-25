#!/usr/bin/env python
import random

def trumpify(x):
    return '“Nobody %s more than me.” – Donald Trump' % x

if __name__ == "__main__":
    things = ['repects women', 'understands the horror of nuclear', 'reads the Bible', 'knows we all need to Cyber better',]
    print(trumpify(random.choice(things)))
    # for thing in things:
    #     print(trumpify(thing))
