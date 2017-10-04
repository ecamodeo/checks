from check50 import *

class Interest(Checks):

    @check()
    def exists(self):
        """interest.c exists"""
        self.require("interest.c")

    @check("exists")
    def compiles(self):
        """interest.c compiles"""
        self.spawn("clang -o interest interest.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_100_and_5_percent(self):
        """$100.00 and 5"%" yeilds $105.00"""
        self.spawn("./interest").stdin("100").stdin("0.05").stdout("Updated balance: 105.00\n", "Updated balance: 105.00\n").exit(0)

    @check("compiles")
    def test_213_and_7_percent(self):
        """$213.00 and 7"%" yeilds $227.91"""
        self.spawn("./interest").stdin("213").stdin("0.07").stdout("Updated balance: 227.91\n", "Updated balance: 227.91\n").exit(0)
