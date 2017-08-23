from check50 import *

class eric(Checks):

    @check()
    def exists(self):
        """eric.c exists."""
        self.require("eric.c")

    @check("exists")
    def compiles(self):
        """eric.c compiles."""
        self.spawn("clang -o eric eric.c").exit(0)

    @check("compiles")
    def prints_eric(self):
        """prints "Hello, world!\\n" """
        expected = "Hello, world!\n"
        actual = self.spawn("./eric").stdout()
        if expected != actual:
            err = Error(Mismatch(expected, actual))
            if actual == "Hello, world!":
                err.helpers = "Did you forget a newline (\"\\n\") at the end of your printf string?"
            raise err
