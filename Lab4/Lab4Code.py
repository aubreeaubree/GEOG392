import arcpy

# making the geodatabase
# step 1
folder_data = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab4"
name_data = folder_data + "\\Lab4Data.gdb"
arcpy.CreateFileGDB_management(folder_data,name_data)

# get data from csv and upload to database 
# step 2 
folder_csv = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab4\\garages.csv"
Parking_Garages = arcpy.MakeXYEventLayer_management(folder_csv, "X", "Y", "Parking_Garages")
# step 3
arcpy.FeatureClassToGeodatabase_conversion(Parking_Garages, name_data)

Parking_Points = name_data + "\\Parking_Garages"
Campus_Data = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab4\\Campus.gdb"
Buildings = Campus_Data + "\\Structures"
Building_Dest = name_data + "\\Buildings"

# step 4
arcpy.Copy_management(Buildings, Building_Dest)

# step 5
spatial = arcpy.Describe(Building_Dest).spatialReference
# step 6
arcpy.Project_management(Parking_Points, name_data + "\New_Garage_points", spatial)

# step 7
Added_Buffer = arcpy.Buffer_analysis(name_data + "\New_Garage_points", name_data+ "\Garage_points_buff", 150)

# step 8
arcpy.Intersect_analysis([Added_Buffer, Building_Dest], name_data + "\Garage_Intersect", 'ALL')

# step 9
arcpy.TableToTable_conversion(name_data + "\Garage_Intersect", folder_data, 'Buildings_Nearby')

