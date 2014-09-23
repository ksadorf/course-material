

dist = {1: 0}  # distance de key


def compDist(n):
    if n in dist:
        return dist[n]
    if n % 2 == 0:
        dist[n] = compDist(int(n / 2)) + 1
    else:
        dist[n] = compDist(int(3 * n + 1)) + 1
    return dist[n]

m = 0
indice = 0
for i in range(1, 1000001):
    dist[i] = compDist(i)
    if dist[i] > m:
        m = dist[i]
        indice = i

print(indice)
