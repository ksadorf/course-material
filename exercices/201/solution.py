import re


def is_alpha(s):
    if re.match('\A[a-zA-Z]+\Z', s):
        return True
    return False
