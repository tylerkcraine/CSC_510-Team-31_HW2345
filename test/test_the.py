from args import The
from print import oo
import test_type


class TestThe(test_type.TestType):
  def test_the(self):
    self.params = The()

    oo(self.params.the)

    assert self.params.the["e"] == "nothing"
    assert not self.params.the["d"]
    assert self.params.the["f"] == "../test/sample.csv"
    assert self.params.the["h"] == False
    assert self.params.the["n"] == 512
    assert self.params.the["s"] == 10019
    assert self.params.the["S"] == ","