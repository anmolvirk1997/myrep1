"""for printing
####
####
####
####"""
for i in range(4):
    for j in range(4):
        # continues printing in same line with charcter specified
        print('# ', end='*')
    print()

for i in range(4):
    for j in range(i+1):  # prints triangle
        print('#', end='')
    print()

for i in range(4):
    for j in range(4-i):  # reverse triangle
        print('#', end='')
    print()

for i in range(5):  # for equilateral trailangle
    for j in range(5-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    for l in range(i):
        print('*', end='')
    print()

print('Triangle')
for i in range(10):  # Equilateral triangle using string repeating with * operand
    print(' '*(20-i), end='')  # repeates blank space 20-i times
    print('*'*(2*i+1))  # reapeates * 2i+1 times eg 1,3,5,7,9...

print('Triangle of numbers')
for i in range(5):
    print(' '*(20-i), end='')
    for j in range(2*i+1):
        print(j, end='')
    print()

print('Triangle of numbers with left right symmetry')
for i in range(10):
    print(' '*(20-i), end='')
    for j in range(i, -1, -1):
        print(j, end='')
    for k in range(i):
        print(k+1, end='')
    print()

print('Triangle of 0-9 with symmetry and rows>10')
x = int(input('How many rows?'))
for i in range(x):
    print(' '*((x+10)-i), end='')
    for j in range(i, -1, -1):
        print(j % 10, end='')
    for k in range(i):
        print((k+1) % 10, end='')
    print()
