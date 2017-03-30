# -*- coding: utf-8 -*-

scores = [37, 38]

for i, grade in enumerate(scores):

    # print grade

    base_num = 5
    quotient = grade / base_num
    nearest_multiple = (quotient * base_num) + base_num
    diff = nearest_multiple - grade

    if nearest_multiple > 40:

        if diff < 3:
            print nearest_multiple
        else:
            print grade

    elif nearest_multiple < 40:
        print grade

    else: # nearest_multiple == 40
        if diff < 3:
            print nearest_multiple
        else:
            print grade


