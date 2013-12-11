# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 19:26:09 2013

@author: ahmed
"""

def humanizer(NUM):
    NUM = ''.join(reversed(str(NUM)))
    TEXT = u''
    n = [ 3*m for m in range( 3 ) ]
    basamaklar = ['','Bin','Milyon', 'Milyar', 'Trilyon']

    # ''.join ( reversed ( <STRING> ) )

    HUU = []
    for i in zip(n,basamaklar):
        p = NUM[ i[0]:i[0]+3 ][ ::-1 ].lstrip( '0' )
        if len(p) is 0:
            continue
        else:
            if p is '1' and i[1] is 'Bin':
                p = 'Bin'
            else:
                p = (p +  ' ' + i[1]).strip()
        HUU.insert(0, p.strip() )
    return HUU

if __name__ == '__main__':
    print humanizer(3000)