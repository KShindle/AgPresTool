import arcpy
import os
#from arcpy import env
arcpy.env.overwriteOutput = True

try:
    def soilReport(property, soils, workspace, prjName):
        reportLoc = os.path.join(workspace, "SoilEval\SoilEval.aprx")
        reportOut = os.path.join(workspace, prjName)
        
        shapefile = prjName + ".shp"
        colSUM = 0
        
        outFile =  os.path.join(workspace, shapefile)
        
        #variable for land evaluation rating attribute in new shapefile    
        acre_TL = "PROP_AREA"
        soil_Acreage = "SOIL_AREA"
        eval = "PROP_EVAL"
        propEVAL = "LAND_EVAL"
        
        #clip soils to shapefile & export to new shapefile
        arcpy.Clip_analysis(soils, property, outFile, "")
        arcpy.AddField_management(outFile, acre_TL, 'DOUBLE')
        arcpy.AddField_management(outFile, soil_Acreage, 'DOUBLE')
        arcpy.AddField_management(outFile, eval, 'DOUBLE')
        arcpy.CalculateField_management(outFile, soil_Acreage, "!SHAPE.AREA@ACRES!", "PYTHON3")
        propAC = arcpy.da.TableToNumPyArray(outFile, soil_Acreage, skip_nulls=True)
        colSUM = propAC[soil_Acreage].sum()
        expression = float(colSUM)
        arcpy.CalculateField_management(outFile, acre_TL, expression, "PYTHON3")
        arcpy.CalculateField_management(outFile, eval, "!SOIL_AREA! * !REL_VALUE!", "PYTHON3")
        
        rvTL = arcpy.da.TableToNumPyArray(outFile, eval, skip_nulls=True)
        rvSUM = rvTL[eval].sum()
        evalRating = (float(rvSUM)/float(colSUM))*0.4
    
        arcpy.AddField_management(property, acre_TL, 'DOUBLE')
        arcpy.CalculateField_management(property, acre_TL, "!SHAPE.AREA@ACRES!","PYTHON3")
        arcpy.AddField_management(property, propEVAL, 'DOUBLE')
        arcpy.CalculateField_management(property, propEVAL, evalRating, "PYTHON3")
        print(workspace)
        print(reportLoc)
#Export report of soils results        
        report = arcpy.mp.ArcGISProject(reportLoc)

        reportList = report.listReports("Soil Ranking")[0]
        reportList.exportToPDF(reportOut)
        del report, reportList, property, propAC, colSUM, rvTL, rvSUM, evalRating
        
except Exception as e:   #error handling help from https://docs.python.org/3/tutorial/errors.html
    print(type(e))    # the exception instance
    print(e)