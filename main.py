import xlsxwriter
import xlrd
import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from openpyxl import load_workbook
from mainUI import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class App():
    def readFile(self,file):
        if file.endswith(".xlsx"):
            self.wbRef = load_workbook(file)
        else:
            print("This file format is not supported. (.xlsx)")

    def writeFile(self):
        #wb = xlsxwriter.Workbook('report.xlsx')
        wsRef = self.wbRef.get_sheet_by_name(self.wbRef.sheetnames[0])
        content = self.loadSheetContent(self,wsRef)
        print(content, end=" ")
        
        '''
        try:
            wb = xlsxwriter.Workbook('report.xlsx')
            self.xlsHelper(self,wb)
        except:
            print("File being used by another process, please close the process and try again.")
            pass
        '''
        
    def loadSheetContent(self,ws):
        rows = ws.rows
        columns = ws.columns
        content = []
        for row in rows:
            line = [col.value for col in row]
            content.append(line)
        return content
        
    # def foundImage(self):
    # def write2Sheet(self):
    '''
        ws = wb.add_worksheet()
        # Headline
        ws.write('A2', '列標籤')
        ws.set_column('A:A', 10)
        ws.write('B2', '加總 - Total Order Items')
        ws.set_column('B:B', 24)
        ws.write('C2', 'ARTWORK')
        ws.set_column('C:C', 12)
        # 
        #print(self.wsRef.cell('A2').value)

        wb.close()
        '''
    
class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def eventExcelBrowseData(self):
        data = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',os.getcwd(),"All Files(*xlsx)")
        if data:
            self.ui.excellineEdit.setText(data[0])
            App.readFile(App,self.ui.excellineEdit.text())
            App.writeFile(App)
    
    def eventImageBrowseData(self):
        data = QtWidgets.QFileDialog.getExistingDirectory(None, 'Open Dir',os.getcwd())
        if data:
            self.ui.imagelineEdit.setText(data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec_())