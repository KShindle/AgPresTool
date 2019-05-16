# AgPresTool
A tool I am developing for calculating the Agricultural Preservation score for properties being considered for inclusion into the PA Ag Pres program

Initially contains 4 files
- gui_main.ui file from QtPy5 Designer
- python script created from converting the .ui file that initializes a GUI
- main.py: main script that deoes the following:
      - defines a soil report function that takes inputs from GUI
      - defines a function for selecting input Shapefile in GUI
      - defines a function for selecting inputed soil unit ratings file
      - defines a function for setting user defined workspace where tool exports will be saved
      - connects signals from GUI
- Soil Rating Script.py that takes inputs from user-defined variables and does the following:
     - Clips inputed soil unit shapefile to AOI Shapefile
     - Adds fields for calculating total acreage, soil unit acreage, and soil evanluation rating
     - Calculates acreages and updates attribute columns with values
     - Calculates each soil unit rating based on acreages and soil unit score
     - Adds and calculates the property Soil Rating to the initial AOI Shapefile for recording purposes
     - This script is supposed to export a report from ArcGIS Pro to the specified workspace input, but I have not gotten this to work consistently.
     
      
