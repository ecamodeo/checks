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
    def first_honors(self):
        """Grades of 98, 90, and 94 result in First Honors"""
        self.spawn("./conditionals").stdin("98").stdin("90").stdin("94").stdout("First Honors\n", "First Honors\n").exit(0)

    @check("compiles")
    def second_honors(self):
        """Grades of 93, 88, and 77 result in Second Honors"""
        self.spawn("./conditionals").stdin("93").stdin("88").stdin("77").stdout("Second Honors\n", "Second Honors\n").exit(0)

    @check("compiles")
    def third_honors(self):
        """Grades of 82, 84, and 80 result in Third Honors"""
        self.spawn("./conditionals").stdin("82").stdin("84").stdin("80").stdout("Third Honors\n", "Third Honors\n").exit(0)

    @check("compiles")
    def no_honors(self):
        """Grades of 65, 50, and 70 result in Not good enough!"""
        self.spawn("./conditionals").stdin("65").stdin("50").stdin("70").stdout("Not good enough!\n", "Not good enough!\n").exit(0)

    @check("compiles")
    def test_invalid_entries(self):
        """rejects invalid entries"""
        self.spawn("./conditionals").stdin("L").reject().stdin("300").reject().stdin("-7").reject()
