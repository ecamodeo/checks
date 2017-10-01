from check50 import *

class quidditch(Checks):

    @check()
    def exists(self):
        """quidditch.c exists"""
        self.require("quidditch.c")

    @check("exists")
    def compiles(self):
        """quidditch.c compiles"""
        self.spawn("clang -o quidditch quidditch.c -lcs50 -lm").exit(0)

    @check("compiles")
    def five_quaffle_through_hoop_snitch(self):
        """5 Quaffles through the other team's hoops, got the snitch"""
        self.spawn("./quidditch").stdin("5").stdin("1").stdout("200\n", "200\n").exit(0)

    @check("compiles")
    def two_quaffle_through_hoop_no_snitch(self):
        """2 Quaffles through the other team's hoops, no snitch"""
        self.spawn("./quidditch").stdin("2").stdin("0").stdout("20\n", "20\n").exit(0)

    @check("compiles")
    def test_invalid_quaffles(self):
        """rejects non ints and bools"""
        self.spawn("./quidditch").stdin("L").reject().stdin("3").reject()

    @check("compiles")
    def test_invalid_quaffles2(self):
        """rejects non ints and bools"""
        self.spawn("./quidditch").stdin("1.2").reject().stdin("M").reject()

    @check("compiles")
    def test_invalid_integers(self):
        """rejects numbers < 1 or > 20"""
        self.spawn("./quidditch").stdin("-8").reject().stdin("35").reject().stdin("100").reject()
