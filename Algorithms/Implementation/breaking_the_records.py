# -*- coding: utf-8 -*-


score = [10, 5, 20, 20, 4, 5, 2, 25, 1]
#  2 4

# score = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
# 4 0

highest_num = score[0]
lowest_num = score[0]

count_lowest = 0
count_highest = 0

for i, num in enumerate(score):

    if num > highest_num:
        highest_num = num
        count_highest += 1

    if num < lowest_num:
        lowest_num = num
        count_lowest += 1

print count_highest, count_lowest

