import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QListWidgetItem
from PySide6.QtGui import QPalette 
from PySide6.QtCore import QSize, Qt

from ui_layout import Ui_MainWindow

from modules import *

class MainWindow(QMainWindow):
    
    def selectFiles(self):
        files, filters = QFileDialog.getOpenFileNames(self, 'Selecione as Invoices...', "", "Arquivos PDF (*.pdf)")
        
        self.ui.FileList.addItems(files)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setMinimumSize(QSize(740, 450))  # cada linha na DataTable tem altura: deltaH = 40
        
        self.ui.GenerateButton.setMinimumSize(QSize(163, 31))
        self.ui.GenerateButton.setMaximumSize(QSize(163, 31))
        
        verticalLayout = self.ui.gridLayout_2.findChild(QVBoxLayout, 'verticalLayout')
        
        if verticalLayout != None:
            verticalLayout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
            verticalLayout.setContentsMargins(0, 20, 0, 0)
        
        self.ui.FileButton.clicked.connect(self.selectFiles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
