# -*- coding: utf-8 -*-

# import sys

n = 6
k = 3
a = [1, 3, 2, 6, 1, 2]

result = 0

for i, elm_i in enumerate(a):
    for j, elm_j in enumerate(a):
        if (elm_i + elm_j) % k == 0 and i < j:
            result += 1

print result
