# -*- coding: utf-8 -*-

h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word = 'abc'

width = len(word)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_height = {}
height_list = []
word_list = list(word)

# generate a dictionary having set of alphabet and its height
for i, elm in enumerate(alphabet):
    alphabet_height[elm] = h[i]

for i, elm in enumerate(word_list):
    height_list.append(alphabet_height[elm])

height = max(height_list)

print width * height
