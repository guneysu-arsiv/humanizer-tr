# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:26:09 2013

@author: ahmed
"""
from nums import data

def randomizer(pow):
    from random import random
    return long(10**pow + (10**pow) * random())

def prettizer( humandata ):
    t = ''
    for item in humandata:
        t += item + '\n'
    return t

def humanizer(NUM):
    NUM = ''.join(reversed(str(NUM)))
    TEXT = u''
    n = [ 3*m for m in range( 5 ) ]

    HUU = []
    for i in data[:len(NUM)/3 + 1]:
        p = NUM[ i[0]:i[0] + i[2] ][ ::-1 ].lstrip( '0' ) ## BUG NOT i+3,
        if len(p) is 0:
            continue
        elif p is '1' and i[1] == 'Bin':
            p = 'Bin'
        else:
            p = (p +  ' ' + i[1]).strip()
        HUU.insert(0, p.strip() )
    return HUU

if __name__ == '__main__':

    for t in range(1,10):
        print humanizer(randomizer(t))