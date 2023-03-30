from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton,QButtonGroup,QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

from second_win import *
from instr import *

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def results(self):
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        self.index1 = self.index

        if self.exp.age == 0:
            return txt_result0
        elif 8 >= self.exp.age >= 7:
            self.index1 -= 6
        elif 10 >= self.exp.age >= 9:
            self.index1 -= 4.5
        elif 12 >= self.exp.age >= 11:
            self.index1 -= 3
        elif 14 >= self.exp.age >= 13:
            self.index1 -= 1.5

        if self.index1 >= 15:
            return txt_result1
        elif 14.5 >= self.index1 >= 11:
            return txt_result2
        elif 10.9 >=  self.index1 >= 6:
            return txt_result3
        elif 5.9 >= self.index1 >= 0.5:
            return txt_result4
        elif 0.4 >= self.index1:
            return txt_result5

    def initUI(self):
        self.workheart = QLabel(txt_workheart + self.results())
        self.indexik = QLabel(txt_index + str(self.index))
        self.leyout_line = QVBoxLayout()
        self.leyout_line.addWidget(self.indexik, alignment = Qt.AlignCenter)
        self.leyout_line.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.leyout_line)

        
