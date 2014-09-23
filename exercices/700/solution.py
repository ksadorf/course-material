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
    while base < len(r) - 1 and indice < (len(r)):
        while indice < (len(r)-1) and r[indice] == 0:
            indice += 1
        if r[base] == r[indice]:
            r[base] += r[indice]
            r[indice] = 0
            base += 1
            indice = base + 1
        else:
            if r[base] == 0:
                r[base] = r[indice]
                r[indice] = 0
            else:
                base += 1
                indice = base + 1
    return r


def rollin(grid, direction):
    if direction == 'l':
        for r in grid:
            rollin_row(r)
    elif direction == 'r':
        for r in grid:
            rollin_row(r[:: - 1])
    elif direction == 'u':
        for r in grid.T:
            rollin_row(r)
    elif direction == 'd':
        for r in grid.T:
            rollin_row(r[:: - 1])
    add_new(grid)
    cprint(stdscr, grid)
    return grid


def cprint(screen, g):
    for i, r in enumerate(g):
        screen.addstr(i, 0, str(r))

import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
curses.curs_set(0)
stdscr.addstr(6, 0, "Hit 'q' to quit")
stdscr.refresh()
g = init_grid()
cprint(stdscr, g)
stdscr.addstr(5, 0, 'This is your grid. Goog luck!')
key = ''
while key != ord('q'):
    key = stdscr.getch()
    curses.setsyx(0, 0)
    stdscr.clear()
    stdscr.refresh()
    if key == curses.KEY_UP or key == ord('u'):
        g = rollin(g, 'u')
        stdscr.addstr(5, 0, 'Direction used: UP')
    if key == curses.KEY_DOWN or key == ord('d'):
        g = rollin(g, 'd')
        stdscr.addstr(5, 0, 'Direction used: DOWN')
    if key == curses.KEY_RIGHT or key == ord('r'):
        g = rollin(g, 'r')
        stdscr.addstr(5, 0, 'Direction used: RIGHT')
    if key == curses.KEY_LEFT or key == ord('l'):
        g = rollin(g, 'l')
        stdscr.addstr(5, 0, 'Direction used: LEFT')
curses.endwin()
