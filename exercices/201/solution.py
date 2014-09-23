import re


def is_alpha(s):
    if re.match('[a-zA-Z]+', s):
        return True
    return False
