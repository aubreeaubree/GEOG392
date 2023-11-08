import arcpy

Campus_Data = r"D:\\Aubree's GIS Stuff\\GEOG392\\Lab4\\Campus.gdb"
structures = Campus_Data + "\\Structures"
where_clause = "BldgName = '%s'" % Selected_Garage_Name

cursor = arcpy.SearchCursor(structures, where_clause=where_clause)

shouldContinue = False
for row in cursor:
    if row.getValue("BldgName") == Selected_Garage_Name:
        shouldContinue = True
        break

if shouldContinue:

