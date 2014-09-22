def sumLim(n):
    num = int(999 / n)
    return int(n * (num * (num + 1)) / 2)
print(sumLim(5) + sumLim(3) - sumLim(15))
