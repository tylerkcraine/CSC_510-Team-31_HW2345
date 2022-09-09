from unicodedata import name

from sym import Sym
from num import Num

class Cols:
    def __init__(self, names):
        self.names=names
        self.all=[]
        self.klass=None
        self.x={}
        self.y={}
        for c,s in names:
            col=[]
            if s.find("^[A-Z]*")>0:
                self.all.append(Num(c,s))
            else:
                self.all.append(Sym(c,s))
            col=self.all[-1]
            if s.find(":$")!=-1:
                if s.find("[!+-]"):
                    self.y=col 
                else:
                    self.x=col
                   
                if s.find("!$"):
                    self.klass=col