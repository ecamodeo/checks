from check50 import *

class multiples(Checks):

    @check()
    def exists(self):
        """multiples.c exists"""
        self.require("multiples.c")

    @check("exists")
    def compiles(self):
        """multiples.c compiles"""
        self.spawn("clang -o multiples multiples.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_1(self):
        """1 yeilds 1, 2, 3, 4, ..., 100"""
        self.spawn("./multiples").stdin("1").stdout("1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100\n", "1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100\n").exit(0)

    @check("compiles")
    def test_16(self):
        """16 yeilds 16  32  48  64  80  96"""
        self.spawn("./multiples").stdin("16").stdout("16  32  48  64  80  96\n", "16  32  48  64  80  96\n").exit(0)

    @check("compiles")
    def test_100(self):
        """100 yeilds 100"""
        self.spawn("./multiples").stdin("100").stdout("100\n", "100\n").exit(0)

    @check("compiles")
    def test_invalid_numbers(self):
        """rejects values outside range"""
        self.spawn("./multiples").stdin("-3").reject().stdin("102").reject()

    @check("compiles")
    def test_invalid_entry(self):
        """rejects non ints"""
        self.spawn("./multiples").stdin("3.2").reject().stdin("A").reject()
