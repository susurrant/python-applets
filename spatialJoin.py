#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Joins attributes from one feature to another based on the spatial relationship.
Implemented by Xin Yao : https://github.com/susurrant/
"""



import arcpy
import os
import pandas as pd

arcpy.env.workspace = './data'
arcpy.env.overwriteOutput = True

# target_file:   data to be joined
# join_file:     join features
# output_fields: a list of field name to export

def spatialJoin(target_file, join_file, output_fields):
    try:
        # make XY event from a text file
        out_Layer = 'p'+target_file[1:-4]
        spRef = r"Coordinate Systems\Geographic Coordinate Systems\World\WGS 1984.prj"
        arcpy.MakeXYEventLayer_management(target_file, 'x', 'y', out_Layer, spRef)
        arcpy.CopyFeatures_management(out_Layer, 'tem.shp')

        # spatial join
        arcpy.SpatialJoin_analysis('tem.shp', join_file, 'sj_lyr')
        

        # export joined data
        arcpy.ExportXYv_stats('sj_lyr.shp', output_fields, 'COMMA', 'sj_'+target_file, 'ADD_FIELD_NAMES')
    except Exception as err:
        print(err.args[0])

    # remove unnecessary files
    os.remove('./data/sj_' + target_file[:-3] + 'txt.xml')
    arcpy.Delete_management('tem.shp')
    arcpy.Delete_management('sj_lyr.shp')

if __name__ == '__main__':
    target_file = 'p_051316.csv'
    join_file = 'fishnet_1km_4rr_origin.shp'
    fields = ['Join_Count', 'pid', 'fid_', 'time', 'tag', 'gid']
    spatialJoin(target_file, join_file, fields)

    
