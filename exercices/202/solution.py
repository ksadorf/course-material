import re


def starts_with(s, beg):
    if re.match('\A'+beg, s):
        return True
    return False
