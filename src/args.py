import sys
import re
from constants import *
from print import oo
from utils import coerce


def populate_coerce(t: dict, m: re.Match):
    t[m.group(1)] = coerce(m.group(2))


class The:
    def __init__(self):
        self.the = {}

        re.sub(
            "\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+=([\S]+)",
            lambda match: populate_coerce(self.the, match),
            HELP_STRING,
        )

        if len(sys.argv) > 1:
            csv_args = {}
            for i in range(1, len(sys.argv), 2):
                if i + 1 < len(sys.argv):
                    csv_args[sys.argv[i]] = sys.argv[i + 1]
                else:
                    csv_args[sys.argv[i]] = True
                for slot, v in self.the.items():
                    v = str(v)
                    for k, x in csv_args.items():
                        if (k == "-" + slot[0:1]) or (k == "--" + slot):
                            v = (
                                "True"
                                if v == "False"
                                else "False"
                                if v == "True"
                                else x
                            )
                    self.the[slot] = coerce(v)


if __name__ == "__main__":
    testthe = The()
    oo(testthe.the)

