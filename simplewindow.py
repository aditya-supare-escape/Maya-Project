from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QComboBox, QLineEdit, QSlider, QSpinBox, QDoubleSpinBox

from PySide6.QtCore import QSize, Qt


class  MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #ui setup
        self.btn = QPushButton("Click Me")
        self.btn2 = QPushButton("Click Me 2")
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMaximumHeight(700)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        
        
        self.spin_b = QSpinBox()
        
        
        
        self.combo_b = QComboBox()
        self.combo_b.addItems(['Unreal', 'Maya', 'Blender', 'Cinema4D'])
        
        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        
        self.main_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.btn2)
        self.main_layout.addWidget(self.slider)
        self.main_layout.addWidget(self.spin_b)
        self.main_layout.addWidget(self.combo_b)
        
        
        
        
        self.setCentralWidget(self.main_widget)
        
        #signals
        self.btn.clicked.connect(self.print_hello)
        self.slider.valueChanged.connect(self.slide_print)

    def slide_print(self,slider_value):
        print('Nick is this years old:',(slider_value))

    def print_hello(self):
        print("Hello, World!")

app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()