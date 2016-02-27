n = input()
while n != -1:
    for x in range(0, n):
        spaces = n - x - 1
        line = ''
        for y in range(0, spaces):
            line += ' '
        line += '^'
        for y in range(0, 2*x):
            line += '^'
        print(line)
    n = input()
