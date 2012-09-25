#!/usr/bin/env python

# ---------------------------
# projects/PFD/PFD.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# PFD_read
# ------------


def PFD_read_parameters (r, a) :
    """
    reads two ints that represent tasks and rules into a[0] and a[1]
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

def PFD_read_node (r, a, cache) :
    """
    modifies cache based on rules of successive lines of r
    r is a  reader
    a is an array of int
    cache is a 2 dimensional array of int
    return true if that succeeds, false otherwise
    """
    
    for i in range(0, a[1]) :
        s = r.readline()
        l = s.split()
        task = int(l[0])
        if(task <= a[0]) :
            rules = int(l[1])
            for j in range (0, rules) :
                independent = int(l[2 + j])
                cache[task][independent] = 1              
    assert a[0] > 0
    assert a[1] > 0 
          
          

# ------------
# PFD_eval
# ------------

def PFD_eval (tasks, cache) :
    """
    tasks is an int
    cache is a 2 dimsensional array
    return array containing tasks in output order 
    """
    assert tasks > 0
    # <your code>
    
    
    
    
def PFD_no_prereqs (job, tasks, cache) :
    """
    job is an int
    tasks is an int
    cache is a 2 dimensional array
    returns true if no tasks point to job
    """
    assert job > 0
    for x in range(1, tasks + 1) :
        if(cache[job][x] == 1) :
            return False
    return True
        

# -------------
# PFD_print
# -------------

def PFD_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# PFD_solve
# -------------

def PFD_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    a = [0, 0]
    while PFD_read_parameters(r, a) :
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        v = PFD_eval(a[0], a[1])
        PFD_print(w, a[0], a[1], v)