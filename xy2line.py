# Import system modules
import arcpy

arcpy.env.workspace = '.'
# Set local variables
input_table = 'f_sh_0601_s0.csv'
out_lines = 'f_sh_0601_s0'
spRef = r"Coordinate Systems\Geographic Coordinate Systems\World\WGS 1984.prj"

#XY To Line
arcpy.XYToLine_management(input_table,out_lines, 'ox', 'oy', 'dx', 'dy', spatial_reference=spRef)