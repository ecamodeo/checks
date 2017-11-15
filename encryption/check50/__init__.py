from check50 import *

class encryption(Checks):

    @check()
    def exists(self):
        """encryption.c exists"""
        self.require("encryption.c")

    @check("exists")
    def compiles(self):
        """encryption.c compiles"""
        self.spawn("clang -o encryption encryption.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_seven(self):
        """Entering 154 and 209 passes"""
        self.spawn("./encryption").stdin("154").stdin("209").stdout("Success! Message was encrypted\n", "Success! Message was encrypted\n").exit(0)

    @check("compiles")
    def test_seven(self):
        """Entering 13 and 201 fails"""
        self.spawn("./encryption").stdin("13").stdin("201").stdout("Factors failed. Please try again later\n", "Factors failed. Please try again later\n").exit(1)
