from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QGroupBox, QListWidget
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont

from instr import*
from final_win import *

class Experiment():
    def __init__(self, age, test1,test2,test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()

    def initUI(self):
        self.hintname=QLabel(txt_hintname)
        self.name = QLineEdit(txt_name)
        self.hintage = QLabel(txt_hintage)
        self.age= QLineEdit(txt_age)
        self.test1 = QLabel(txt_test1)
        self.starttest1 = QPushButton(txt_starttest1)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.test2 = QLabel(txt_test2)
        self.starttest2 = QPushButton(txt_starttest2)
        self.test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.starttest3 = QPushButton(txt_starttest3)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)
        self.sendresults = QPushButton(txt_sendresults)
        
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()
        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignRight)
        self.l_line.addWidget(self.hintname,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.name, alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hintage,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.age,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest1,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.test3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.starttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest2,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.hinttest3,alignment=Qt.AlignLeft)
        self.l_line.addWidget(self.sendresults,alignment=Qt.AlignCenter)
        self.r_line.addWidget(self.text_timer,alignment=Qt.AlignRight)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    
    def next_click(self):
       self.hide()
       self.exp = Experiment(int(self.age.text()), self.hinttest1.text(), self.hinttest2.text(), self.hinttest3.text())
       self.fw = FinalWin(self.exp)

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):    
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()
        
    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()
        
    def timer_final(self):
        global time 
        time =QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        else:
            self.text_timer.setStyleSheet('color rgb(0,0,0)')
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))    
        if time.toString('hh:mm:ss') == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.sendresults.clicked.connect(self.next_click)
        self.starttest1.clicked.connect(self.timer_test)
        self.starttest2.clicked.connect(self.timer_sits)
        self.starttest3.clicked.connect(self.timer_final)

