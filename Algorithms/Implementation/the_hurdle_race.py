# -*- coding: utf-8 -*-

n = 5
k = 4
height = [1, 6, 3, 5, 2]
# 2

result = 0

highest_hurdle = max(height)

if highest_hurdle > k:
    result = highest_hurdle - k

print result




