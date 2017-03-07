# -*- coding: utf-8 -*-

n = 9
c = [10, 20, 20, 10, 10, 30, 50, 10, 20]

socks = c[:]
uniq_socks = list(set(socks))

pairs = 0

for i, uniq_elm in enumerate(uniq_socks):
    num = socks.count(uniq_elm)
    if num > 1:
        pairs += num / 2

print pairs