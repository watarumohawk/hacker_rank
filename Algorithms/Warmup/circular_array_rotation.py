# -*- coding: utf-8 -*-
"""
Sample Input

3 2 3
1 2 3
0
1
2

Sample Output

2
3
1
"""

def rotate_list(list):
    list.insert(0, list.pop())
    return list

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

n_times = k
rotated_list = []

for i in range(n_times):
    rotated_list = rotate_list(a)

for a0 in range(q):
    m = int(raw_input().strip())
    print rotated_list[m]
