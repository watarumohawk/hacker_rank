# -*- coding: utf-8 -*-

# n = 4
# k = 1
# c = [3, 10, 2, 9]
# b = 12
# 5

n = 4
k = 1
c = [3, 10, 2, 9]
b = 7
# Bon Appetit

total_cost = c[:]
total_cost.remove(total_cost[k])
shared_cost = sum(total_cost)
b_actual = shared_cost / 2

refund = b - b_actual

if refund== 0:
    print 'Bon Appetit'
else:
    print refund
