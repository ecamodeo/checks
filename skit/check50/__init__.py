from check50 import *

class Skittles(Checks):

    @check()
    def exists(self):
        """skittles.c exists"""
        self.require("skittles.c")

    @check("exists")
    def compiles(self):
        """skittles.c compiles"""
        self.spawn("clang -o skittles skittles.c -lcs50 -lm").exit(0)
