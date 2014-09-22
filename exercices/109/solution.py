def sets_common(l):
    if len(l) == 0:
        return set()
    r = l[0]
    for s in l:
        r &= s
    return r
