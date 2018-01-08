from check50 import *

class loops(Checks):

    @check()
    def exists(self):
        """loops.c exists"""
        self.require("loops.c")

    @check("exists")
    def compiles(self):
        """loops.c compiles"""
        self.spawn("clang -o loops loops.c -lcs50 -lm").exit(0)

    @check("compiles")
    def value_of_17(self):
        """17 produces 17, 34, 51, 68, ..., 170"""
        self.spawn("./loops").stdin("17").stdout("17\n34\n51\n68\n85\n102\n119\n136\n153\n170\n", "17\n34\n51\n68\n85\n102\n119\n136\n153\n170\n").exit(0)

    @check("compiles")
    def test_invalid_entries(self):
        """rejects invalid entries"""
        self.spawn("./loops").stdin("L").reject().stdin("300").reject().stdin("0").reject().stdin("-7").reject()
