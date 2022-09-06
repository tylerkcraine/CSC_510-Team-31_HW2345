import sys
import math, random

from sym import Sym
from utils import per


class Num(Sym):
  def __init__(self, c = 0, s = ""):
    super().__init__(c, s)
    self.n = 0
    self.at = c or 0
    self.name = s or ""
    self._has = {}
    self.lo = sys.maxsize
    self.hi = -sys.maxsize
    self.isSorted = True
    self.w = -1 if (s or "").find("$") == -1 else 1

  def nums(self):
    if not self.isSorted: 
      dict(sorted(self._has.items(), key=lambda item: item[1]))
      self.isSorted = True
    return self._has
    
  # v is a number -> value like key, value
  def add(self, v, the):
    pos = 0
    if v!="?":
      self.n = self.n +1
      self.lo = min(v, self.lo)
      self.hi = max(v,self.hi)

      if len(self._has) < the["n"]/self.n:
        pos = 1 + len(self._has)

      elif random.random() < the["n"]/self.n:
        # generate random int b/w 1, len of _has. As mentioned in csv.luna
        pos = random.randint(1, len(self._has))

      if pos:
        self.isSorted = False
        self._has[pos] = float(v)
  
  def div(self):
    a = self.nums()
    return (per(a,.9) - per(a,0.1))/2.58

  def mid(self):
    return per(self.nums(),.5)







