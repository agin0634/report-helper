# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(3000, 3000))
        MainWindow.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(67, 67, 67);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 481, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 11, 461, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.excellineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.excellineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.excellineEdit.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.excellineEdit.setObjectName("excellineEdit")
        self.horizontalLayout.addWidget(self.excellineEdit)
        self.excelBrowseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.excelBrowseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.excelBrowseButton.setObjectName("excelBrowseButton")
        self.horizontalLayout.addWidget(self.excelBrowseButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 461, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.imagelineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.imagelineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.imagelineEdit.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);")
        self.imagelineEdit.setObjectName("imagelineEdit")
        self.horizontalLayout_2.addWidget(self.imagelineEdit)
        self.imageBrowseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.imageBrowseButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.imageBrowseButton.setObjectName("imageBrowseButton")
        self.horizontalLayout_2.addWidget(self.imageBrowseButton)
        self.line = QtWidgets.QFrame(self.widget_2)
        self.line.setGeometry(QtCore.QRect(10, 50, 479, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.widget_2)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 0))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"    border: 1px solid gray; \n"
"    margin-top:7px;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    subcontrol-origin: margin;\n"
"    color: rgb(255, 255, 255);\n"
"     subcontrol-position: top center; /* position at the top left*/ \n"
"     padding:0 3px;\n"
" } ")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 441, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.searchButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.searchButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.searchButton.setObjectName("searchButton")
        self.verticalLayout_4.addWidget(self.searchButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"    border: 1px solid gray; \n"
"    margin-top:7px;\n"
"}\n"
"\n"
"QGroupBox::title { \n"
"    subcontrol-origin: margin;\n"
"    color: rgb(255, 255, 255);\n"
"     subcontrol-position: top center; /* position at the top left*/ \n"
"     padding:0 3px;\n"
" } ")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 441, 71))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.exportSoldButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.exportSoldButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.exportSoldButton.setObjectName("exportSoldButton")
        self.verticalLayout_3.addWidget(self.exportSoldButton)
        self.exportUnsoldButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.exportUnsoldButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(98, 98, 98);")
        self.exportUnsoldButton.setObjectName("exportUnsoldButton")
        self.verticalLayout_3.addWidget(self.exportUnsoldButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exportSoldButton.clicked.connect(MainWindow.eventExportSoldReport)
        self.exportUnsoldButton.clicked.connect(MainWindow.eventExportUnsoldReport)
        self.searchButton.clicked.connect(MainWindow.eventSearch)
        self.excelBrowseButton.clicked.connect(MainWindow.eventExcelBrowseData)
        self.imageBrowseButton.clicked.connect(MainWindow.eventImageBrowseData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Helper"))
        self.label.setText(_translate("MainWindow", "Source Path"))
        self.excelBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Image Path"))
        self.imageBrowseButton.setText(_translate("MainWindow", "Browse"))
        self.groupBox.setTitle(_translate("MainWindow", "Properties"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Export"))
        self.exportSoldButton.setText(_translate("MainWindow", "Export Sold Report"))
        self.exportUnsoldButton.setText(_translate("MainWindow", "Export unsold Report"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
