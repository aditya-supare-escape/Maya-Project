from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox, QScrollArea, QHBoxLayout, QTabWidget)        
        
from PySide6.QtCore import Qt



class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tab_group = QTabWidget()
        self.tab_group.TabPosition(QTabWidget)
        btn1 = QPushButton('clickme')
        
        #main layout 
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.init_scroll_area()
        
        #add widget
        self.main_layout.addWidget(btn1)
        self.main_layout.addWidget(self.scroll_area)
        
        self.setCentralWidget(self.main_widget)
        
        #signals
        btn1.clicked.connect(self.print_func)
    
    def print_func(self):
        print('hey')
        
    def init_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_layout = QVBoxLayout()
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)
        
        
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        
        


        
        
        
app = QApplication([])
window = NewWindow()

window.show()
app.exec()