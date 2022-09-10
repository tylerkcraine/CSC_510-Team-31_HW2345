from constants import N_OPTION
from num import Num
from args import The
from print import oo
import test_type


class TestNum(test_type.TestType):
    def test_num(self):
        self.num_test = Num()
        self.test_the = The()
        for each_num in range(1, 101):
            self.num_test.add(each_num, self.test_the.the[N_OPTION])
        median, st_dev = self.num_test.mid(), self.num_test.div()

        oo({"mid": median, "div": st_dev})
        assert 50 <= median and median <= 52 and 30.5 < st_dev and st_dev < 32

    def test_bignum(self):
        self.num_test = Num()
        self.test_the = The()
        self.test_the.the["n"] = 32
        for i in range(1, 1001):
            self.num_test.add(i, self.test_the.the["n"])

        oo(self.num_test.nums())
        assert 32 == len(self.num_test._has)
