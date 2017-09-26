#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

' 半正矢公式：给定两点经纬度，计算距离（km） '

__author__ = 'Xin Yao'

import math

def haverSine(theta):
    v = math.sin(theta / 2)
    return v * v

'''
给定的经度1，纬度1；经度2，纬度2. 计算两个点之间的距离。
INPUT:  lon1 经度1
        lat1 纬度1
        lon2 经度2
        lat2 纬度2
        EARTH_RADIUS 地球半径平均值，单位：km
RETURN: 距离（单位：km）
'''
def haverSineDistance(lon1, lat1, lon2, lat2, EARTH_RADIUS = 6371.0):
    #用haverSinee公式计算球面两点间的距离。
    #经纬度转换成弧度
    lat1 *= math.pi / 180
    lon1 *= math.pi / 180
    lat2 *= math.pi / 180
    lon2 *= math.pi / 180
    #差值
    vLon = abs(lon1 - lon2)
    vLat = abs(lat1 - lat2)
    #h is the great circle distance in radians, great circle就是一个球体上的切面，它的圆心即是球心的一个周长最大的圆
    h = haverSine(vLat) + math.cos(lat1) * math.cos(lat2) * haverSine(vLon)
    distance = 2 * EARTH_RADIUS * math.asin(math.sqrt(h))
    return distance

'''
if __name__ == '__main__':
    print haverSineDistance(121.473704, 31.230393, 120.585316, 31.298886)
'''