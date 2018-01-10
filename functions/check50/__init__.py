from check50 import *

class functions(Checks):

    @check()
    def exists(self):
        """functions.c exists"""
        self.require("functions.c")

    @check("exists")
    def compiles(self):
        """functions.c compiles"""
        self.spawn("clang -o functions functions.c -lcs50 -lm").exit(0)

    @check("compiles")
    def good(self):
        """Values of 120 and -109 equal 11"""
        self.spawn("./functions").stdin("120").stdin("-109").stdin("11").stdout("correct!\n", "correct!\n").exit(0)

    @check("compiles")
    def bad(self):
        """Values of 1432 and 90 equal 189"""
        self.spawn("./functions").stdin("1432").stdin("90").stdin("189").stdout("incorrect!\n", "incorrect!\n").exit(0)

    @check("compiles")
    def test_invalid_entries(self):
        """rejects invalid entries"""
        self.spawn("./functions").stdin("L").reject()
