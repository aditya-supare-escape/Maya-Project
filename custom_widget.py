from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QMessageBox)


class SmallMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.btn_1 = QPushButton('print hello')
        self.btn_2 = QPushButton('print world')
        
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        
        
        
        
        main_layout.addWidget(self.btn_1)
        main_layout.addWidget(self.btn_2)
        
        
        
        main_widget.setLayout(main_layout)
        
        self.setCentralWidget(main_widget)
        
        #signals 
        self.btn_1.clicked.connect(self.print_hello)
        self.btn_2.clicked.connect(self.make_question)
        
    def print_hello(self):
        print('hello!')
        
    def make_popup(self):
        popup = QMessageBox(self)
        popup.setWindowTitle('Message Box')
        popup.setText('this is the contents of the message')
        popup.setStandardButtons(QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ok)        
        result = popup.exec()
        if result == QMessageBox.StandardButton.Ok:
            print('ok was pressed')
        
    def make_question(self):
        # result = QMessageBox.question(self, 'Question', 'this is a question msg box', QMessageBox.StandardButton.Cancel  | QMessageBox.StandardButton.No)
        # result = QMessageBox.about(self, 'about', 'its about page')
        result = QMessageBox.warning(self, 'warning', 'this is the warning', QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.No )
        print(result)
        
        
        
app = QApplication([])
window = SmallMainWindow()

window.show()
app.exec()