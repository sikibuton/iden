#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      usa
#
# Created:     26/06/2013
# Copyright:   (c) usa 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import math

def f(x):
    y = -x*x
    return y


def main():
    N = 6
    G = 100
    n = []
    for i in range(N):
        n.append(random.uniform(-100,100))
    n_c = n
    print "n="
    print n
    i=0
    j=0
    k=0
    while j<G:
        m = []
        for i in range(N):
            m.append((f(n[i])))
        for k in range (3):
            a = max(xrange(len(m)), key=lambda i: m[i])
            n[k] = n[a]
            m[a] = min(m)
        print n
        n[3] = random.uniform(-100,100)
        n[4] = (n[0]+n[1])/2
        n[5] = (n[0]+n[2])/2
        print n
        j = j+1
    m = []
    for i in range(N):
        m.append(f(n[i]))
    a = max(xrange(len(m)), key=lambda i: m[i])
    print n[a]




if __name__ == '__main__':
    main()