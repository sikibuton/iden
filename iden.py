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

def max_value_i(l):
    a = max(l)
    i=0
    for i in range(len(l)):
        if l[i] == a :
           n = i
    return n

def main():
    N = 6
    G = 3
    n = []
    for i in range(N):
        n.append(random.uniform(-100,100))
    n_c = n
    print "first n="
    print n
    i=0
    j=0
    k=0
    while j<G:
        print "j="
        print j
        m = []
        i=0
        for i in range(N):
            m.append((f(n[i])))
        print"m="
        print m
        k=0
        for k in range (3):
            a = max_value_i(m)
            m[a] = min(m)
            n[k] = n[a]
            print "k="
            print k
            print m
        n[3] = random.uniform(-100,100)
        n[4] = abs((n[0]-n[1])/2)
        n[5] = abs((n[0]+n[1])/2)
        print"new n="
        print n
        j = j+1
    m = []
    i=0
    for i in range(N):
        m.append(f(n[i]))
    a = max_value_i(m)
    print n[a]




if __name__ == '__main__':
    main()