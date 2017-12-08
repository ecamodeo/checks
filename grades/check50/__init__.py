from check50 import *

class grades(Checks):

    @check()
    def exists(self):
        """grades.c exists"""
        self.require("grades.c")

    @check("exists")
    def compiles(self):
        """grades.c compiles"""
        self.spawn("clang -o grades grades.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_grades(self):
        """Grades of 64, 88, 91 result in an average of 81"""
        self.spawn("./grades").stdin("64").stdin("88").stdin("91").stdout("81\n", "81\n").exit(0)

    @check("compiles")
    def test_bad_values(self):
        """Check for bad values"""
        self.spawn("./grades").stdin("A").reject().stdin("-2").reject().stdin("102").reject()
