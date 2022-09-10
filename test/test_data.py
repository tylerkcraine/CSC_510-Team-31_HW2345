import test_type
from data import Data
from print import oo,o
from args import The
from constants import BIG_S_OPTION
from fileutils import read_file

class TestData(test_type.TestType):
    def test_data(self):
        temp_the = The()
        d = Data(read_file(temp_the),temp_the.the[BIG_S_OPTION])
        for col in d.cols.y:
            oo(col)
        return True

    def test_stats(self):
        temp_the = The()
        data = Data(read_file(temp_the),temp_the.the[BIG_S_OPTION])

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()
        
        print ("xmid", o( data.stats(1, data.cols.x, mid) ) )
        print ("xdiv", o( data.stats(3, data.cols.x, div) ) )
        print ("ymid", o( data.stats(2, data.cols.y, mid) ) )
        print ("ydiv", o( data.stats(3, data.cols.y, div) ) )

        return True






