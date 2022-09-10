from args import The
from constants import BIG_S_OPTION, D_OPTION, E_OPTION, F_OPTION, H_OPTION, N_OPTION, SMALL_S_OPTION
from print import oo
import test_type


class TestThe(test_type.TestType):
  def test_the(self):
    self.params = The()

    oo(self.params.the)

    assert self.params.the[E_OPTION] == "nothing"
    assert not self.params.the[D_OPTION]
    assert self.params.the[F_OPTION] == "./data/auto93.csv"
    assert self.params.the[H_OPTION] == False
    assert self.params.the[N_OPTION] == 512
    assert self.params.the[SMALL_S_OPTION] == 10019
    assert self.params.the[BIG_S_OPTION] == ","