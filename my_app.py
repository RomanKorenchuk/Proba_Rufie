from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

from instr import *
from second_win import *

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appaer()
        self.connects()
        self.show()
    def initUI(self):
        self.hello = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next, self)
        self.leyout_line = QVBoxLayout()
        self.leyout_line.addWidget(self.hello, alignment = Qt.AlignCenter)
        self.leyout_line.addWidget(self.instruction, alignment = Qt.AlignCenter)
        self.leyout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.leyout_line)
    def set_appaer(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide()
        self.mw = TestWin()

app = QApplication([])
mw = MainWin()
app.exec_()