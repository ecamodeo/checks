from check50 import *

class kids(Checks):

    @check()
    def exists(self):
        """kids.c exists"""
        self.require("kids.c")

    @check("exists")
    def compiles(self):
        """kids.c compiles"""
        self.spawn("clang -o kids kids.c -lcs50 -lm").exit(0)

    
