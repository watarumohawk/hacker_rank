# -*- coding: utf-8 -*-

x1 = 0
v1 = 3

x2 = 4
v2 = 2

k1_position = x1
k2_position = x2

# x is less than 10000
for i in range(10000):
    k1_position += v1
    k2_position += v2

    if k1_position == k2_position:
        print 'YES'
        break

    if (k1_position != k2_position) and i == 9999:
        print 'NO'