# -*- coding: utf-8 -*-

a = 5
b = 2
c = 4
d = 3
e = 1

input_list = [a, b, c, d, e]

# print input_list

sorted_list = sorted(input_list)

# print sorted_list

min_sum = 0
max_sum = 0

for i in range(4):
    min_sum += sorted_list[i]

reversed_list = list(reversed(sorted_list))

for i in range(4):
    max_sum += reversed_list[i]

print min_sum, max_sum

