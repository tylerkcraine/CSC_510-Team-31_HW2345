from cols import Cols
from row import Row
from parse import parser
from utils import rnd

# def csv():
#     return None

class Data: 
    # pass the

    def __init__(self,src,separator):
        self.cols = None
        self.rows = []
        if type(src) == str:
            # to be changed?
            parser(src, self.function,separator)
        else:
            for row in (src or []):
                self.add(row)

    def function(self,row):
        print ("row",row)
        # self.add(row)
        self.add([[i,temp] for i,temp in enumerate(row)])
    
    def add(self,xs):
        if not self.cols:
            print ("xs:",xs)
            self.cols = Cols(xs)
        else:
            # cell to cells in row.py
            row = self.rows.append(xs.cell and xs or Row(xs))
            for todo in [self.cols.x, self.cols.y]:
                for col in todo:
                    col.add(row.cells[col.at])
        # return None

    def stats(self, places=2, show_cols="data.cols.x", fun='mid'):
        show_cols, fun = show_cols or self.cols.y, fun or "mid"
        t= {}
        for col in show_cols:
            v = fun(col)
            v = type(v)==int and rnd(v,places) or v
            t[col.name] = v
        return t


















