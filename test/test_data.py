import test_type
from data import Data
from print import oo,o

class TestData(test_type.TestType):
    def test_data(self):
        d = Data("../data/auto93.csv")
        for col in d.cols.y:
            oo(col)
        return True

    def test_stats(self):
        data = Data("../data/auto93.csv")

        def div(col):
            return col.div()

        def mid(col):
            return col.mid()
        
        print ("xmid", o( data.stats(1, data.cols.x, mid) ) )
        print ("xdiv", o( data.stats(3, data.cols.x, div) ) )
        print ("ymid", o( data.stats(2, data.cols.y, mid) ) )
        print ("ydiv", o( data.stats(3, data.cols.y, div) ) )

        return True






