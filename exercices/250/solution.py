def draw_n_squares(n):
    fLine='+' + '---+' * n
    print(fLine)
    nline='|' + '   |' * n + '\n' + fLine
    for i in range(0, n):
        print(nline)
