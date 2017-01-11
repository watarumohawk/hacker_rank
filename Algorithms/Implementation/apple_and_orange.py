# -*- coding: utf-8 -*-

s = 7
t = 11
a = 5
b = 15
m = 3
n = 2

apple = [-2, 2, 1]
orange = [5, -6]

apple_amount = m
orange_amount = n

house_start = s
house_end = t

apple_tree_position = a
orange_tree_position = b

def search_fruit(fruit, fruite_position_list):

    matched_fruit = []
    for i, elm in enumerate(fruit):

        position = elm + fruite_position_list

        if house_start <= position <= house_end:
            matched_fruit.append(position)

    return len(matched_fruit)

print search_fruit(apple, apple_tree_position)
print search_fruit(orange, orange_tree_position)
