# -*- coding: utf-8 -*-

n = 6
space = ' '
stair = '#'

for i in range(n):
    stairs = stair * (i + 1)
    print ('{: >%d}' % n).format(stairs)