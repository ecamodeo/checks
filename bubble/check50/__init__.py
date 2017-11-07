from check50 import *

class Bubble(Checks):

    @check()
    def exists(self):
        """bubble.c exists"""
        self.require("bubble.c")

    @check("exists")
    def compiles(self):
        """bubble.c compiles"""
        self.spawn("clang -o bubble bubble.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_bubble_sort(self):
        """Sorts as 4 8 15 16 23 42 50 108"""
        self.spawn("./bubble").stdout("4 15 16 50 8 23 42 108\n") \
                                 .stdout("4 8 15 16 23 42 50 108\n)
