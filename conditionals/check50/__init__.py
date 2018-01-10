from check50 import *

class conditionals(Checks):

    @check()
    def exists(self):
        """conditionals.c exists"""
        self.require("conditionals.c")

    @check("exists")
    def compiles(self):
        """conditionals.c compiles"""
        self.spawn("clang -o conditionals conditionals.c -lcs50 -lm").exit(0)

    @check("compiles")
    def value_of_17(self):
        """Grades of 93, 88, and 77 result in Second Honors and average of 86.0"""
        self.spawn("./conditionals").stdin("17").stdout("Average: 86.0\nSecond Honors\n", "Average: 86.0\nSecond Honors\n").exit(0)

    @check("compiles")
    def value_of_17(self):
        """Grades of 93, 88, and 77 result in Second Honors and average of 86.0"""
        self.spawn("./conditionals").stdin("17").stdout("Second Honors\n", "Second Honors\n").exit(0)

    @check("compiles")
    def test_invalid_entries(self):
        """rejects invalid entries"""
        self.spawn("./conditionals").stdin("L").reject().stdin("300").reject().stdin("-7").reject()
