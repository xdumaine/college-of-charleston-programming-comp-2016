import math
triangle = raw_input()
while triangle != -1:
    triangle = triangle.split(' ')
    a2 = 0
    b2 = 0
    c2 = 0
    if triangle[0] == 'AB':
        a2 = int(triangle[1]) ** 2
    elif triangle[0] == 'BC':
        b2 = int(triangle[1]) ** 2
    else:
        c2 = int(triangle[1]) ** 2

    if triangle[2] == 'AB':
        a2 = int(triangle[3]) ** 2
    elif triangle[2] == 'BC':
        b2 = int(triangle[3]) ** 2
    else:
        c2 = int(triangle[3]) ** 2


    if c2 == 0:
        area = (int(math.sqrt(a2)) * int(math.sqrt(b2))) / 2
        print 'AC: ', int(math.sqrt(a2+b2)), 'AREA: ', int(area)
    if b2 == 0:
        b2 = c2-a2
        area = (int(math.sqrt(a2)) * int(math.sqrt(b2))) / 2
        print 'BC: ', int(math.sqrt(b2)), 'AREA: ', int(area)
    if a2 == 0:
        a2 = c2-b2
        area = (int(math.sqrt(a2)) * int(math.sqrt(b2))) / 2
        print 'AB: ', int(math.sqrt(a2)), 'AREA: ', int(area)
    triangle = raw_input()
