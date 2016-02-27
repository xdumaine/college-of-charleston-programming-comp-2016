min = 50
max = 0

n = int(input())
while n != -1:
    if n < min:
        min = n
    if n > max:
        max = n
    n = int(input())
print 'MAX: ', max
print 'MIN: ', min
