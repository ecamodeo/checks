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

    @check("compiles")
    def test_10_and_5(self):
        """10 and 5 yeilds 15 and 50"""
        self.spawn("./sumprod").stdin("10").stdin("5").stdout("15\n", "15\n").stdout("50\n", "50\n").exit(0)

    @check("compiles")
    def test_non_ints(self):
        """rejects non ints"""
        self.spawn("./sumprod").stdin("L").reject().stdin("3.2").reject()
