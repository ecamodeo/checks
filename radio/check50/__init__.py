from check50 import *

class radio(Checks):

    @check()
    def exists(self):
        """radio.c exists"""
        self.require("radio.c")

    @check("exists")
    def compiles(self):
        """radio.c compiles"""
        self.spawn("clang -o radio radio.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_christmas(self):
        """Entering December 25, 2018 returns 12/25/18"""
        self.spawn("./radio").stdin("12").stdin("25").stdin("2018").stdout("12/25/2018\n", "12/25/2018\n").exit(0)

    @check("compiles")
    def test_my_birthday(self):
        """Entering November 2, 1976 returns 11/2/76"""
        self.spawn("./radio").stdin("11").stdin("2").stdin("1976").stdout("11/2/1976\n", "11/2/1976\n").exit(0)

    @check("compiles")
    def test_month(self):
        """Entering invalid month"""
        self.spawn("./radio").stdin("154").reject()

    @check("compiles")
    def test_day(self):
        """Entering invalid day"""
        self.spawn("./radio").stdin("9").stdin("44").reject()
