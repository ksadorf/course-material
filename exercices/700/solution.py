import numpy as np
import random

def randGridPlace():
    return random.randint(0, 3), random.randint(0, 3)

def init_grid():
    m = np.zeros((4,4), dtype=int)
    u, v = randGridPlace()
    uu, vv= u, v
    m[u, v] = 2
    while uu == u and vv == v :
        uu, vv = randGridPlace()
    m[uu,vv]=2
    return m


def add_new(grid):
    available = np.where(grid == 0)
    places = zip(available[0],available[1])
    if len(available[0]) == 0:
        return grid
    pick = random.randint(0,len(available[0])-1)
    u, v = available[0][pick], available[1][pick]
    if random.random() <= 0.8 :
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
            r=rollin_row(r[::-1])
    elif direction == 'u':
        for r in grid.T:
            r=rollin_row(r)
    elif direction == 'd':
        for r in grid.T:
            r=rollin_row(r[::-1])
    return grid


