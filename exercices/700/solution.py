import numpy as np
import random


def randGridPlace():
    return random.randint(0, 3), random.randint(0, 3)


def init_grid():
    m = np.zeros((4, 4), dtype=int)
    u, v = randGridPlace()
    uu, vv = u, v
    m[u, v] = 2
    while uu == u and vv == v:
        uu, vv = randGridPlace()
    m[uu, vv] = 2
    return m


def add_new(grid):
    available = np.where(grid == 0)
    places = zip(available[0], available[1])
    if len(available[0]) == 0:
        return grid
    pick = random.randint(0, len(available[0]) - 1)
    u, v = available[0][pick], available[1][pick]
    if random.random() <= 0.8:
        grid[u, v] = 2
    else:
        grid[u, v] = 4
    return grid


def rollin_row(r):
    base = 0
    indice = 1
    changed = False
    while base < len(r) - 1 and indice < (len(r)):
        while indice < len(r) and r[indice] == 0:
            indice += 1
        if indice == len(r):
            return changed

        if r[base] == r[indice]:  # merge
            r[base] += r[indice]
            r[indice] = 0
            changed = True
            base += 1
            indice = base + 1
        else:
            if r[base] == 0 and r[indice] != 0:
                r[base] = r[indice]
                r[indice] = 0
                changed = True
            else:
                base += 1
                indice = base + 1
    return changed


def rollin(grid, direction):
    changed = False
    if direction == 'l':
        for r in grid:
            changed |= rollin_row(r)
    elif direction == 'r':
        for r in grid:
            changed |= rollin_row(r[:: - 1])
    elif direction == 'u':
        for r in grid.T:
            changed |= rollin_row(r)
    elif direction == 'd':
        for r in grid.T:
            changed |= rollin_row(r[:: - 1])
    if changed:
        add_new(grid)
    return grid


def movePossible(grid):
    for i in range(0, len(grid) - 1):
        for j in range(0, len(grid[i]) - 1):
            if grid[i, j] == 0:
                return True
            if grid[i, j] == grid[i + 1, j] or grid[i, j] == grid[i, j + 1]:
                return True
    for j in range(0, len(grid) - 1):
        if grid[-1, j] == 0:
            return True
        if grid[-1, j] == grid[-1, j + 1]:
            return True
    for i in range(0, len(grid) - 1):
        if grid[i, -1] == 0:
            return True
        if grid[i, -1] == grid[i + 1, -1]:
            return True
    return False


def state(grid):
    win = np.where(grid == 2048)
    if len(win[0]) == 1:
        return 'win'
    if not movePossible(grid):
        return 'fail'
    return 'normal'


def play(grid, direction):
    rollin(grid, direction)
    s = state(g)
    if s == 'fail':
        stdscr.addstr(6, 0, 'You failed the game.')
        return False
    elif s == 'win':
        stdscr.addstr(6, 0, 'You beat the game. Keep playing')
    return True


def cprint(screen, g):
    for i, r in enumerate(g):
        l = ''.join('{:^4}'.format(str(el)) for el in r)
        screen.addstr(i, 0, l)


import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
curses.curs_set(0)
stdscr.addstr(6, 0, "Hit 'q' to quitor space to restart")
stdscr.refresh()
g = init_grid()
cprint(stdscr, g)
stdscr.addstr(5, 0, 'This is your grid. Goog luck!')
key = ''
playable = True
while key != ord('q'):
    key = stdscr.getch()
    curses.setsyx(0, 0)
    stdscr.clear()
    stdscr.refresh()
    if key == ord(' '):
        g = init_grid()
        stdscr.addstr(5, 0, "C'est faible de recommencer")
    if playable:
        if key == curses.KEY_UP or key == ord('u'):
            playable = play(g, 'u')
            stdscr.addstr(5, 0, 'Direction used:' + chr(8593))
        if key == curses.KEY_DOWN or key == ord('d'):
            playable = play(g, 'd')
            stdscr.addstr(5, 0, 'Direction used:' + chr(8595))
        if key == curses.KEY_RIGHT or key == ord('r'):
            playable = play(g, 'r')
            stdscr.addstr(5, 0, 'Direction used:' + chr(8594))
        if key == curses.KEY_LEFT or key == ord('l'):
            playable = play(g, 'l')
            stdscr.addstr(5, 0, 'Direction used:' + chr(8592))
    else:
        stdscr.addstr(6, 0, 'You failed the game.')
        stdscr.addstr(7, 0, "Hit 'q' to quit or space to restart")
    cprint(stdscr, g)
curses.endwin()
