from check50 import *

class needle(Checks):

    @check()
    def exists(self):
        """needle.c exists"""
        self.require("needle.c")

    @check("exists")
    def compiles(self):
        """needle.c compiles"""
        self.spawn("clang -o needle needle.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_one(self):
        """1 is not found"""
        self.spawn("./needle").stdin("1").stdout("NO\n", "NO\n").exit(0)

    @check("compiles")
    def test_two(self):
        """23 is found"""
        self.spawn("./needle").stdin("23").stdout("YES\n", "YES\n").exit(0)
