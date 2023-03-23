from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QListWidget

from instr import*
#from second_win import*

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def initUI(self):
        self.lab1=QLabel(txt_lab1)
        self.edit1 = QLineEdit(txt_edit1)
        self.lab2 = QLabel(txt_lab2)
        self.edit2= QLineEdit(txt_edit2)
        self.lab3 = QLabel(txt_lab3)
        self.butt1 = QPushButton(txt_butt1)
        self.edit3  =QLineEdit(txt_edit3)
        self.lab4 = QLabel(txt_lab4)
        self.butt2 = QPushButton(txt_butt2)
        self.lab5 = QLabel(txt_lab5)
        self.butt3 = QPushButton(txt_butt3)
        self.edit4 = QLineEdit(txt_edit4)
        self.edit5 = QLineEdit(txt_edit5)
        self.butt4 = QPushButton(txt_butt4)
        self.lab6 = QLabel(txt_lab6)
        
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.l_line.addWidget(self.lab1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit1, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab4,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.lab5,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit4,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.edit5,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.butt4,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.lab6,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    
    def next_click(self):
        self.tw=FinalWin()
        self.hide()
    
    def connects(self):
        self.butt4.clicked.connect(self.next_click)

app=QApplication([])
mw=TestWin()
app.exec_()
