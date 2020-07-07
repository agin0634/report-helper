# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 781, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 751, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 11, 731, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.excellineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.excellineEdit.setObjectName("excellineEdit")
        self.horizontalLayout.addWidget(self.excellineEdit)
        self.excelbrowseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.excelbrowseButton.setObjectName("excelbrowseButton")
        self.horizontalLayout.addWidget(self.excelbrowseButton)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 731, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.imagelineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.imagelineEdit.setObjectName("imagelineEdit")
        self.horizontalLayout_2.addWidget(self.imagelineEdit)
        self.imagepushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.imagepushButton.setObjectName("imagepushButton")
        self.horizontalLayout_2.addWidget(self.imagepushButton)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.excelbrowseButton.clicked.connect(MainWindow.eventExcelBrowseData)
        self.imagepushButton.clicked.connect(MainWindow.eventImageBrowseData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Report Helper"))
        self.label.setText(_translate("MainWindow", "Excel Path"))
        self.excelbrowseButton.setText(_translate("MainWindow", "Browse"))
        self.label_2.setText(_translate("MainWindow", "Image Path"))
        self.imagepushButton.setText(_translate("MainWindow", "Browse"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
