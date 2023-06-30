from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QTimer, QTime
from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_widht, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.info_1 = QLabel(txt_info_1)
        self.l_line.addWidget(self.info_1, aligment = Qt.AlignLeft)
        self.line_name = QLineEdit()
        self.l_line.addWidget(self.line_name, aligment = Qt.AlignLeft)
        self.info_2 = QLabel(txt_info_2)
        self.l_line.addWidget(self.info_2, aligment = Qt.AlignLeft)
        self.line_age = QLineEdit()
        self.l_line.addWidget(self.line_age, aligment = Qt.AlignLeft)
        self.info_3 = QLabel(txt_info_3)
        self.l_line.addWidget(self.info_3, aligment = Qt.AlignLeft)
        self.button_1 = QPushButton('Начать первый тест')
        self.l_line.addWidget(self.button_1, aligment = Qt.AlignLeft)
        self.line_num = QLineEdit()
        self.l_line.addWidget(self.line_num, aligment = Qt.AlignLeft)
        self.info_4 = QLabel(txt_info_4)
        self.l_line.addWidget(self.info_4, aligment = Qt.AlignLeft)
        self.button_2 = QPushButton('Начать делать приседания')
        self.l_line.addWidget(self.button_2, aligment = Qt.AlignLeft)
        self.info_5 = QLabel(txt_info_5)
        self.l_line.addWidget(self.info_5, aligment = Qt.AlignLeft)
        self.button_3 = QPushButton('Начать финальный тест')
        self.l_line.addWidget(self.button_3, aligment = Qt.AlignLeft)
        self.line_num_1 = QLineEdit()
        self.l_line.addWidget(self.line_num_1, aligment = Qt.AlignLeft)
        self.line_num_2 = QLineEdit()
        self.l_line.addWidget(self.line_num_2, aligment = Qt.AlignLeft)
        self.button_4 = QPushButton('Отправить результаты')
        self.l_line.addWidget(self.button_4, aligment = Qt.AlignCenter)
        self.text_timer = QLabel()
        self.r_line.addWidget(self.tetx_timer, aligmnent = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.button_4.clicked.connect(self.next_click)
        self.button_3.clicked.connect(self.timer_final)
    
    def next_click(self):
        self.hide()
        self.tw = MainWin()
    
    def timer_final(self):
        global time 
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time3Event)
        self.timer.start(1000)
    
    def timer3Event(self):
        global time
        time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times, 36, QFont.Bold'))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            timer.stop()

app = QApplication([])
win_2 = TestWin()
# Внес изменения