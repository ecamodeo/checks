from check50 import *

class arrays(Checks):

    @check()
    def exists(self):
        """arrays.c exists"""
        self.require("arrays.c")

    @check("exists")
    def compiles(self):
        """arrays.c compiles"""
        self.spawn("clang -o arrays arrays.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_arrays(self):
        """Values of 4, 13, 18, 22, 0, 1, -4, 19, 100, 11 produces 6"""
        self.spawn("./arrays").stdin("4").stdin("13").stdin("18")..stdin("22").stdin("0").stdin("1").stdin("-4").stdin("19").stdin("100").stdin("11")\
        .stdout("Greater than 10: 6\n", "Greater than 10: 6\n").exit(0)

    @check("compiles")
    def test_more_values(self):
        """Values of 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 produces 0"""
        self.spawn("./arrays").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdin("6").stdin("-7").stdin("8").stdin("9").stdin("0")\
        .stdout("Greater than 10: 0\n", "Greater than 10: 0\n").exit(0)
