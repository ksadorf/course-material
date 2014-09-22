from prime import *


d = []
for i in range(10000, 10050):
        if is_prime(i):
                d.append(str(i))
print(', '.join(d))
