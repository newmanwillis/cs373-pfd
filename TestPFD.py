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

from PFD import PFD_read, PFD_eval, PFD_print, PFD_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 10\n")
        a = [0, 0]
        b = PFD_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
        


    # ----
    # eval
    # ----s

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