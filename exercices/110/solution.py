import sys

op = '+-*/%'
if len(sys.argv) != 4 or sys.argv[2] not in op:
    print('usage: ./calc.py a_number (an_operator +-*/%) a_number')
    exit(0)
n1 = int(sys.argv[1])
n2 = int(sys.argv[3])
o = sys.argv[2]
if o == '+':
        print(n1 + n2)
elif o == '-':
    print(n1 - n2)
elif o == '*':
    print(n1 * n2)

if n2 == 0:
    print('input error')
    exit(0)

if o == '%':
    print(n1 % n2)
elif o == '/':
    print(n1 / n2)
