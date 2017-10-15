#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

__author__ = 'Xin Yao'

import time
 
def ts2dt(value):
    tformat = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1469857960
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(tformat, value)
    return dt
 
def dt2ts(dt):
     #dt为字符串
     #中间过程，一般都需要将字符串转化为时间数组
     time.strptime(dt, '%Y-%m-%d %H:%M:%S')
     ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
     #转化为时间戳
     s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
     return int(s)
 
if __name__ == '__main__':
    print(dt2ts('2016-07-30 13:52:40'))
    print(ts2dt(1469857960))
