from check50 import *

class pokemon(Checks):

    @check()
    def exists(self):
        """pokemon.c exists"""
        self.require("pokemon.c")

    @check("exists")
    def compiles(self):
        """pokemon.c compiles"""
        self.spawn("clang -o pokemon pokemon.c -lcs50 -lm").exit(0)
