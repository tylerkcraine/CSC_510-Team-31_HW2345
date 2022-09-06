import sys

class The:
  def __init__(self):
    self.the = {
      "e": "nothing",
      "d": False,
      "f": "../test/sample.csv",
      "h": False,
      "n": 512,
      "s": 10019,
      "S": ","
    }
    if len(sys.argv) > 1:
      param = sys.argv[1]
      if param == "-e":
          self.the["e"] = sys.argv[2]
      elif param == "-d":
          self.the["d"] = sys.argv[2]
      elif param == "-f":
          self.the["f"] = sys.argv[2]
      elif param == "-h":
          self.the["h"] = sys.argv[2]
      elif param == "-n":
          self.the["n"] = 512
          if len(sys.argv) > 2:
              self.the["n"] = sys.argv[2]
      elif param == "-s":
          self.the["s"] = 10019
      elif param == "-S":
          self.the["S"] = ","
          if len(sys.argv) > 2:
              self.the["S"] = sys.argv[2]
