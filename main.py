#import packages
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
import gui_main
import soil_function

#initialize app & qgis, create main window
app = QApplication(sys.argv)

window = QWidget()
ui = gui_main.Ui_Dialog()
ui.setupUi(window) 

def runSoilReport():
    """performs the main soil report generation"""
    try:

        property = ui.shapefileLE.text()
        soils = ui.soilLE.text()
        workspace = ui.workspaceLE.text()
        prjName = ui.reportLE.text()
        soil_function.soilReport(property, soils, workspace, prjName)
        QMessageBox.information(window, "Result", "Your property soil evaluation have been successfully saved at " + workspace)        
    except Exception as e:
        QMessageBox.information(window, 'Operation failed', 'Soil Report Generation failed with ' + str(e.__class__) + ': ' + str(e), QMessageBox.Ok)

    
def selectShapefileInput ():
    """opens file dialog box to import shapefile and update GUI"""
    fileName, _ = QFileDialog.getOpenFileName(window, "Select shapefile", "", "Shapefile (*.shp)")
    if fileName:
        ui.shapefileLE.setText(fileName)

def selectSoilInput ():
    """opens file dialog box to import soil shapefile and update GUI"""
    fileName, _ = QFileDialog.getOpenFileName(window, "Select shapefile", "", "Shapefile (*.shp)")
    if fileName:
        ui.soilLE.setText(fileName)    
def workspaceInput ():
    """opens file dialog box to select location of for tool outputs and update GUI"""     
    path = QFileDialog.getExistingDirectory(window, "Select Directory")
    if path:
        ui.workspaceLE.setText(path)

"""Connect Signals"""
ui.reportBT.clicked.connect(runSoilReport)
ui.shapefileTB.clicked.connect(selectShapefileInput)
ui.soilTB.clicked.connect(selectSoilInput)
ui.workspaceTB.clicked.connect(workspaceInput)


window.show()

exitcode = app.exec_()
sys.exit(exitcode)