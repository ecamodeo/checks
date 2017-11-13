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

    @check("compiles")
    def test_one(self):
        """1 kid is incorrect"""
        self.spawn("./kids").stdin("1").stdout("That is incorrect!\n", "That is incorrect!\n").exit(0)

    @check("compiles")
    def test_two(self):
        """2 kids is correct"""
        self.spawn("./kids").stdin("2").stdout("That is correct!\n", "That is correct!\n").exit(0)

    @check("compiles")
    def test_non_ints(self):
        """Check for non-ints"""
        self.spawn("./kids").stdin("A").reject().stdin("-2").reject().stdin("1.2").reject()
