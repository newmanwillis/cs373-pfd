#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = [0] * 1000000

def PFD_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

    

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    global cache
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <your code>

    if( i > j) :
        temp = i
        i = j
        j = temp
   
    if(i < j / 2) :
        i = j / 2
   
    maxCycleLength = 0
    
    for x in range(i, j + 1) :
        num = x
        currentCycleLength = 1
        
        while(num != 1) :
            if(num < 1000000 and cache[num] != 0) :
                currentCycleLength += cache[num] - 1
                break
            elif(num & 1 == 1) :
                num = num + (num >> 1) + 1
                currentCycleLength += 2
            else :
                num >>= 1
                currentCycleLength += 1
                
            """ if(num % 2 == 0) :
                num = num / 2
            else :
                num = num * 3 + 1"""
            """currentCycleLength = currentCycleLength + 1"""
            
        if (currentCycleLength > maxCycleLength) :
            maxCycleLength = currentCycleLength
        if(num < 1000000) :
            cache[x] = currentCycleLength   

    assert maxCycleLength > 0
    return maxCycleLength

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)