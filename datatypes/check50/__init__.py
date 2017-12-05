from check50 import *

class datatypes(Checks):

    @check()
    def exists(self):
        """datatypes.c exists"""
        self.require("datatypes.c")

    @check("exists")
    def compiles(self):
        """datatypes.c compiles"""
        self.spawn("clang -o datatypes datatypes.c -lcs50 -lm").exit(0)
