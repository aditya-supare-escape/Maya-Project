from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QGridLayout)



class LockHideMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # make our main widget and its layout
        self.main_layout= QVBoxLayout()
        self.main_widget = QWidget() 
        self.main_widget.setLayout(self.main_layout)
        
        self.lock_btn = QPushButton('Lock')
        self.hide_btn = QPushButton('Hide')
        self.unlock_btn = QPushButton('Unlock')
        self.show_btn = QPushButton('Show')
        
        #radio button and labels
        self.translate_lbl = QLabel('Translate')
        self.trans_list = [QRadioButton('Tx'), QRadioButton('Ty'), QRadioButton('Tz'), QRadioButton('All')]
        
        
        self.rotate_lbl = QLabel('Rotate')
        self.rot_list = [QRadioButton('Rx'), QRadioButton('Ry'), QRadioButton('Rz'), QRadioButton('All')]
        
        
        self.scale_lbl = QLabel('Scale')
        self.scale_list = [QRadioButton('Sx'), QRadioButton('Sy'), QRadioButton('Sz'), QRadioButton('All')]
        
        
        
        self.radio_gridlayout = QGridLayout()
        

        for i in range(len(self.trans_list)):
            self.trans_list[i].setAutoExclusive(False)
            self.radio_gridlayout.addWidget(self.trans_list[i], 0, i+1 )
            
        
        for j in range(len(self.rot_list)):
            self.radio_gridlayout.addWidget(self.rot_list[j], 1, j+1)
            
        for k in range(len(self.scale_list)):
            self.radio_gridlayout.addWidget(self.scale_list[k], 2, k+1)
            
        
                    
        self.radio_gridlayout.addWidget(self.translate_lbl, 0, 0)
        self.radio_gridlayout.addWidget(self.rotate_lbl, 1, 0)
        self.radio_gridlayout.addWidget(self.scale_lbl, 2, 0)
        
        #make button layout
        self.button_gridlayout = QGridLayout()
        self.button_gridlayout.addWidget(self.lock_btn, 0, 0)
        self.button_gridlayout.addWidget(self.hide_btn, 1, 0)
        self.button_gridlayout.addWidget(self.unlock_btn, 0, 1)
        self.button_gridlayout.addWidget(self.show_btn, 1, 1)
        # self.button_gridlayout.addWidget(self.radio_btn, 2,0)
        
        

        
        
        
        
        self.main_layout.addLayout(self.radio_gridlayout)
        self.main_layout.addLayout(self.button_gridlayout)
        
        #set central widget of the main window
        self.setCentralWidget(self.main_widget)
        
        self.trans_list[0].toggled.connect(self.is_toggled)
        self.trans_list[-1].toggled.connect(self.set_buttons)


    def is_toggled(self):
        print('is toggled')
        
    def set_buttons(self):
        if self.trans_list[-1].isChecked():
            for i in range(len(self.trans_list)-1):
                self.trans_list[i].setChecked(True)
        
        else:
            for k in range(len(self.trans_list)):
                self.trans_list[k].setChecked(False)

app = QApplication([])
window = LockHideMainWindow()
window.show()

app.exec()