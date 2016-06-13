# coding=utf-8

import datetime

#strftime日期格式化函数
print datetime.date.today().strftime('%Y-%m-%d')
print datetime.date(2016,06,13).strftime('%Y-%m-%d')


print datetime.date.today() + datetime.timedelta(days=1)  #timedelta 时间加减函数
print datetime.date.today().replace(year=2017)  #replace 时间替换,可替换年月日部分

import time #处理时间需要使用time模块
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
