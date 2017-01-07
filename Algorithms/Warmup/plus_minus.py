# -*- coding: utf-8 -*-

n = 6
arr = [-4, 3, -9, 0, 4, 1]

arr_length = len(arr)

positive_num = 0
negative_num = 0
zero_num = 0

for i, num in enumerate(arr):
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1
    elif num == 0:
        zero_num += 1

print ('{:.6f}'.format(float(positive_num)/float(arr_length)))
print ('{:.6f}'.format(float(negative_num)/float(arr_length)))
print ('{:.6f}'.format(float(zero_num)/float(arr_length)))
