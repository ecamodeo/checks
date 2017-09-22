from check50 import *

class Room(Checks):

    @check()
    def exists(self):
        """room.c exists"""
        self.require("room.c")

    @check("exists")
    def compiles(self):
        """room.c compiles"""
        self.spawn("clang -o room room.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_A_and_7(self):
        """Letter A, room 7 yeilds A7"""
        self.spawn("./room").stdin("A").stdin("7").stdout("A7\n", "A7\n").exit(0)

    @check("compiles")
    def test_invalid_letters(self):
        """rejects letters beyond G"""
        self.spawn("./room").stdin("L").reject().stdin("M").reject()

    @check("compiles")
    def test_invalid_integers(self):
        """rejects numbers < 1 or > 20"""
        self.spawn("./room").stdin("-8").reject().stdin("35").reject().stdin("100").reject()
