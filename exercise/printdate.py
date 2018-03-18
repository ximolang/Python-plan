#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 将以数指定年月日的日期打印出来

def printDate():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # 一个包含1-31对应结尾的字符串
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

    year = input('Input the Year: ')
    month = int(input('Input the Month(1-12): '))
    day = int(input('Input the Day(1-31): '))

    month_name = months[month - 1]
    ordinal = str(day) + endings[day - 1]

    print('----------------')
    print('Today is\n' + month_name + ' ' + ordinal + ', ' + str(year))

printDate()
