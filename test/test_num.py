from num import Num 
from args import The
from print import oo

class TestNum():
    def test_num(self):
        self.num_test = Num()
        self.test_the = The()
        for each_num in [1,5,3,4,5,2,7,6]:
            self.num_test.add(each_num,self.test_the.the)
        median, st_dev = self.num_test.mid(), self.num_test.div()

        oo({"mid": median, "div": st_dev})
        assert median == 4 and 2.32<=st_dev and st_dev<=2.33


if __name__ =="__main__":
    t= TestNum()
    t.test_num()










