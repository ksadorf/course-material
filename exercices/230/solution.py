from prime import *


s=[2,3]
for i in range(3, 100000000):
        if all( i % a for a in s ):
                s.append(i)
                print(i)
print(s)
