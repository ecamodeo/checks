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
    def test_1(self):
        """Input of 1 outputs That is correct!""""
        self.spawn("./kids").stdin("1").stdout("That is incorrect!\n", "That is incorrect!\n").exit(0)

    @check("compiles")
    def test_2(self):
        """Input of 2 outputs That is correct!"""
        self.spawn("./kids").stdin("2").stdout("That is correct!\n", "That is correct!\n").exit(0)

    @check("compiles")
    def test_non_ints(self):
        """rejects negatives and non-ints"""
        self.spawn("./kids").stdin("-1").reject().stdin("L").reject().stdin("3.4").reject()
