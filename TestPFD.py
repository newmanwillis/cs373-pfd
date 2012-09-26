'''
Created on Sep 23, 2012

@author: Administrator
'''
#!/usr/bin/env python

# -------------------------------
# projects/PFD/TestPFD.py
# Copyright (C) 2012
# Thomas Preli & Newman Willis
# -------------------------------

"""
To test the program:
    % python TestPFD.py >& TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import PFD_read_parameters, PFD_read_node, PFD_no_prereqs, PFD_remove_tasks, PFD_eval, PFD_print, PFD_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read_parameters
    # ----

    def test_read_parameters_1 (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = PFD_read_parameters(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        
    def test_read_parameters_2 (self) :
        r = StringIO.StringIO("5 4\n")
        a = [0, 0]
        b = PFD_read_parameters(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  5)
        self.assert_(a[1] == 4)
        
    def test_read_parameters_3 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = PFD_read_parameters(r, a)
        self.assert_(b    == False)
        
    def test_read_parameters_4 (self) :
        r = StringIO.StringIO("100 100\n")
        a = [0, 0]
        b = PFD_read_parameters(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  100)
        self.assert_(a[1] == 100)
        
    # ----    
    # read_node    
    # ----
        
    def test_read_node_1 (self) :
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        a = [5, 4]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        self.assert_(cache[3][1] == 1)
        self.assert_(cache[3][5] == 1)
        self.assert_(cache[2][5] == 1)
        self.assert_(cache[2][3] == 1)
        self.assert_(cache[4][3] == 1)
        self.assert_(cache[5][1] == 1)
        
    def test_read_node_2 (self) :
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n20 1 6\n98 1 100")
        a = [5, 6]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        self.assert_(cache[3][1] == 1)
        self.assert_(cache[3][5] == 1)
        self.assert_(cache[2][5] == 1)
        self.assert_(cache[2][3] == 1)
        self.assert_(cache[4][3] == 1)
        self.assert_(cache[5][1] == 1)
        
    def test_read_node_3 (self) :
        r = StringIO.StringIO("3 4 1 5 4 2\n")
        a = [5, 1]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        self.assert_(cache[3][1] == 1)
        self.assert_(cache[3][2] == 1)
        self.assert_(cache[3][3] == 0)
        self.assert_(cache[3][4] == 1)
        self.assert_(cache[3][5] == 1) 
        
    # ----
    # no_prereqs
    # ----
    
    def test_no_prereqs_1 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        v = PFD_no_prereqs(1, 5, cache)
        self.assert_(v)             
 
    def test_no_prereqs_2 (self) :
        cache = [[1 for x in xrange(6)] for x in xrange(6)]
        v = PFD_no_prereqs(1, 5, cache)
        self.assert_(not v)  
        
    def test_no_prereqs_3 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        cache[1][5] = 1
        v = PFD_no_prereqs(1, 5, cache)
        self.assert_(not v)   
        
    # ----
    # remove_tasks
    # ----
    
    def test_remove_tasks_1 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        PFD_remove_tasks(1, 5, cache)
        self.assert_(cache[1][1] == 0)
        self.assert_(cache[2][1] == 0)
        self.assert_(cache[3][1] == 0)
        self.assert_(cache[4][1] == 0)
        self.assert_(cache[5][1] == 0)      
        
    def test_remove_tasks_2 (self) :
        cache = [[1 for x in xrange(6)] for x in xrange(6)]
        PFD_remove_tasks(1, 5, cache)
        self.assert_(cache[1][1] == 0)
        self.assert_(cache[2][1] == 0)
        self.assert_(cache[3][1] == 0)
        self.assert_(cache[4][1] == 0)
        self.assert_(cache[5][1] == 0) 
        self.assert_(cache[1][2] == 1)       
        
    def test_remove_tasks_3 (self) :
        cache = [[0 for x in xrange(6)] for x in xrange(6)]
        cache[3][1] = 1
        PFD_remove_tasks(1, 5, cache)
        self.assert_(cache[1][1] == 0)
        self.assert_(cache[2][1] == 0)
        self.assert_(cache[3][1] == 0)
        self.assert_(cache[4][1] == 0)
        self.assert_(cache[5][1] == 0)            
        
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        r = StringIO.StringIO("3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        a = [5, 4]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        v = PFD_eval(a[0], cache)
        self.assert_(v[0] == 1)
        self.assert_(v[1] == 5)
        self.assert_(v[2] == 3)
        self.assert_(v[3] == 2)
        self.assert_(v[4] == 4)
        
    def test_eval_2 (self) :
        r = StringIO.StringIO("3 2 1 2\n2 1 1\n")
        a = [3, 2]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        v = PFD_eval(a[0], cache)
        self.assert_(v[0] == 1)
        self.assert_(v[1] == 2)
        self.assert_(v[2] == 3)
        
    def test_eval_3 (self) :
        r = StringIO.StringIO("10 1 9\n9 1 8\n8 1 7\n7 1 6\n6 1 5\n5 1 4\n4 1 3\n3 1 2\n2 1 1\n75 1 9\n")
        a = [10, 10]
        cache = [[0 for x in xrange(a[0] + 1)] for x in xrange(a[0] + 1)]
        PFD_read_node(r, a, cache)
        v = PFD_eval(a[0], cache)
        self.assert_(v[0] == 1)
        self.assert_(v[1] == 2)
        self.assert_(v[2] == 3)
        self.assert_(v[3] == 4)
        self.assert_(v[4] == 5)
        self.assert_(v[5] == 6) 
        self.assert_(v[6] == 7) 
        self.assert_(v[7] == 8) 
        self.assert_(v[8] == 9) 
        self.assert_(v[9] == 10)     

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        PFD_print(w, (1, 3, 4, 5, 2))
        self.assert_(w.getvalue() == "1 3 4 5 2\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        PFD_print(w, (1, 2))
        self.assert_(w.getvalue() == "1 2\n")
        
    def test_print_3 (self) :
        w = StringIO.StringIO()
        PFD_print(w, (15, 11, 1, 4, 6, 9, 14, 12, 8, 3, 10, 2, 5, 7, 13))
        self.assert_(w.getvalue() == "15 11 1 4 6 9 14 12 8 3 10 2 5 7 13\n")     

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n")
        
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 0\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1\n")

    def test_solve_3 (self) :
        r = StringIO.StringIO("2 1\n2 1 1\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 2\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."