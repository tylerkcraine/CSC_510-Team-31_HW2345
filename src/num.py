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
    self._has = []
    self.lo = sys.maxsize
    self.hi = -sys.maxsize
    self.isSorted = True
    self.w = -1 if (s or "").find("$") == -1 else 1

  def nums(self):
    if not self.isSorted: 
      self._has.sort()
      self.isSorted = True
    return self._has
    
  # v is a number -> value like key, value
  def add(self, v, the):
    if v!="?":
      self.n = self.n +1
      self.lo = min(v, self.lo)
      self.hi = max(v, self.hi)

      if len(self._has) < the["n"]:
        self.isSorted = False
        self._has.append(float(v))

      elif random.random() < the["n"]/self.n:
        # generate random int b/w 1, len of _has. As mentioned in csv.luna
        self.isSorted = False
        pos = random.randint(0, len(self._has)-1)        
        self._has[pos] = float(v)
  
  def div(self):
    a = self.nums()
    return (per(a,.9) - per(a,0.1))/2.58

  def mid(self):
    return per(self.nums(),.5)







