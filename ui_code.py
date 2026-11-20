from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QScrollArea, QHBoxLayout, QTabWidget, QGroupBox, QCheckBox, QLineEdit, QTextEdit, QFrame)        
        
from PySide6.QtCore import Qt
import sys


class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Smart Retopology")
        self.setMinimumSize(400, 550)
        
        self.init_ui()
        
        
       
        
    def init_ui(self):
        
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
       
        #create tab widget 
        self.tab_group = QTabWidget()
        self.tab_group.setTabPosition(QTabWidget.TabPosition.North)
        
        #Create Pages 
        self.analyzer_page = QWidget()
        self.retopology_page = QWidget()
        self.optimizer_page = QWidget()

        #add tabs 
        self.tab_group.addTab(self.analyzer_page, 'Analyzer')
        self.tab_group.addTab(self.retopology_page, 'Retopology')
        self.tab_group.addTab(self.optimizer_page, 'Optimizer')
        
        self.main_layout.addWidget(self.tab_group)
        
        self.setCentralWidget(self.main_widget)
            
    
    def analyzer_page():
        pass 
    
    def retopology_page():
        pass
    
    def optimizer_page():
        pass
    
        
    def get_selected_issues(self):
        issues = {
            # 'ngons': self.ui.check_ngons.isChecked()
        }
    
        
    
app = QApplication([])
window = NewWindow()

window.show()
app.exec()