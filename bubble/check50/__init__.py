from check50 import *

class Bubble(Checks):

    @check()
    def exists(self):
        """bubble.c exists"""
        self.require("bubble.c")
        self.add("bubble.txt")

    @check("exists")
    def compiles(self):
        """bubble.c compiles"""
        self.spawn("clang -o bubble bubble.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_bubble_sort(self):
        """Sorts as 4 8 15 16 23 42 50 108"""
        #out = self.spawn("./bubble").stdout(File("bubble.txt")).exit(0)
        self.spawn("./bubble").stdout("4 15 16 50 8 23 42 108 \n4 8 15 16 23 42 50 108 \n", "4 15 16 50 8 23 42 108 \n4 8 15 16 23 42 50 108 \n").exit(0)
