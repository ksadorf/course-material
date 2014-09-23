def draw_n_squares(n):
    fLine = '+' + '---+' * n
    res = fLine+'\n'
    nline = '|' + '   |' * n + '\n' + fLine
    for i in range(0, n-1):
        res += nline + '\n'
    res += nline
    return res
