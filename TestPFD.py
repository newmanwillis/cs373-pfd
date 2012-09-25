'''
Created on Sep 23, 2012

@author: Administrator
'''
#!/usr/bin/env python

# -------------------------------
# projects/PFD/TestPFD.py
# Copyright (C) 2012
# Glenn P. Downing
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

from PFD import PFD_read_parameters, PFD_read_node, PFD_eval, PFD_print, PFD_solve

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
        b = PFD_read_node(r, a, cache)
        self.assert_(b    == True)
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
        b = PFD_read_node(r, a, cache)
        self.assert_(b    == True)
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
        b = PFD_read_node(r, a, cache)
        self.assert_(b    == True)
        self.assert_(cache[3][1] == 1)
        self.assert_(cache[3][2] == 1)
        self.assert_(cache[3][3] == 0)
        self.assert_(cache[3][4] == 1)
        self.assert_(cache[3][5] == 1)       
        
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = PFD_eval(1, 10)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = PFD_eval(100, 200)
        self.assert_(v == 125)




    

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO.StringIO()
        PFD_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
        
    def test_print_2 (self) :
        w = StringIO.StringIO()
        PFD_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
        

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO.StringIO("1 1\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 1 1\n")






# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."