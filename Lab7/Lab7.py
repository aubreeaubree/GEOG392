import arcpy

src = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab7\\Lab07_Data\\"
res = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab7\\Lab07_Results\\"
band1 = arcpy.sa.Raster(src + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1")
band2 = arcpy.sa.Raster(src + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2")
band3 = arcpy.sa.Raster(src + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3")
band4 = arcpy.sa.Raster(src + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4")

composite = arcpy.CompositeBands_management([band1,band2,band3,band4], res, "combined.tif")

azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(src + r"\\n30_w097_1arc_v3.tif", res + r"\\hillshade.tif", azimuth,altitude, shadows, z_factor)
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(src + r"\\n30_w097_1arc_v3.tif", res + r"\\slopes.tif", output_measurement, z_factor)
