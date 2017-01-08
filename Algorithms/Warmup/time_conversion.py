# -*- coding: utf-8 -*-

# time = '07:05:45PM'
# time = '07:05:45AM'
time = '12:40:22AM'
# time = '12:00:00PM'

hour = time[0:2]
minute = time[3:5]
second = time[6:8]
notation = time[8:10]

if notation == 'AM':

    if hour == '12':
        print '00' + ':' + minute + ':' + second
    else:
        print hour + ':' + minute + ':' + second

elif notation == 'PM':

    if hour == '12':
        print hour + ':' + minute + ':' + second
    else:
        hour = int(hour) + 12
        print str(hour) + ':' + minute + ':' + second
