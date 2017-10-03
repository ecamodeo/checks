from check50 import *

class Sumprod(Checks):

    @check()
    def exists(self):
        """sumprod.c exists"""
        self.require("sumprod.c")

    @check("exists")
    def compiles(self):
        """sumprod.c compiles"""
        self.spawn("clang -o sumprod sumprod.c -lcs50 -lm").exit(0)
