import re
def startwiths(s,beg):
    if re.match('\A'+beg, s):
        return True
    return False
