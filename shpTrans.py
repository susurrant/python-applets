#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Transform the coordinates of points, polylines or polygons in shapefiles
Implemented by Xin Yao : https://github.com/susurrant/
"""

import arcpy
import os
from csTrans import gcj02_to_wgs84
import sys

codetype = sys.getfilesystemencoding()
print(codetype)
arcpy.env.workspace = './data'


def updateShapefile(fname):
    with arcpy.da.UpdateCursor(fname, ['SHAPE@X', 'SHAPE@Y']) as cursor:
        for row in cursor:
            x, y = row[0], row[1]
            c = gcj02_to_wgs84(x, y)
            row[0], row[1] = c[0], c[1]
            cursor.updateRow(row)


if __name__ == '__main__':
    files = os.listdir('./data')
    for sf in files:
        if sf.endswith('.shp'):
            print sf.decode(codetype).encode("utf-8")
            updateShapefile(sf.decode(codetype).encode("utf-8"))