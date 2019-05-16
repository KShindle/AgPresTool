# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 401, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.soilLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.soilLE.setObjectName("soilLE")
        self.gridLayout.addWidget(self.soilLE, 1, 1, 1, 1)
        self.workspaceTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.workspaceTB.setObjectName("workspaceTB")
        self.gridLayout.addWidget(self.workspaceTB, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.workspaceLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.workspaceLE.setObjectName("workspaceLE")
        self.gridLayout.addWidget(self.workspaceLE, 2, 1, 1, 1)
        self.soilTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.soilTB.setObjectName("soilTB")
        self.gridLayout.addWidget(self.soilTB, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.shapefileTB = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.shapefileTB.setObjectName("shapefileTB")
        self.gridLayout.addWidget(self.shapefileTB, 0, 2, 1, 1)
        self.reportLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.reportLE.setObjectName("reportLE")
        self.gridLayout.addWidget(self.reportLE, 3, 1, 1, 1)
        self.shapefileLE = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shapefileLE.setObjectName("shapefileLE")
        self.gridLayout.addWidget(self.shapefileLE, 0, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 240, 401, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.reportBT = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.reportBT.setObjectName("reportBT")
        self.horizontalLayout_2.addWidget(self.reportBT)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.soilLE.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the soil shapefile to be clipped</p></body></html>"))
        self.workspaceTB.setText(_translate("Dialog", "..."))
        self.label_3.setText(_translate("Dialog", "Workspace:"))
        self.workspaceLE.setToolTip(_translate("Dialog", "<html><head/><body><p>Select location where all outputs of the tool will be saved</p></body></html>"))
        self.soilTB.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "Soil Shapefile:"))
        self.label_4.setText(_translate("Dialog", "Name / File #:"))
        self.label_2.setText(_translate("Dialog", "Property Shapefile:"))
        self.shapefileTB.setText(_translate("Dialog", "..."))
        self.reportLE.setToolTip(_translate("Dialog", "<html><head/><body><p>This will be used to create the new shapefile and soil report</p></body></html>"))
        self.shapefileLE.setToolTip(_translate("Dialog", "<html><head/><body><p>Select the input property shapefile</p></body></html>"))
        self.reportBT.setText(_translate("Dialog", "Create Soil Report"))

