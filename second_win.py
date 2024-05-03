from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        ''' вікно, в якому проводиться опитування '''
        super().__init__()
 
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
 
        #Встановлює зв'язки між елементами
        self.connects()
 
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
     
        # старт:
        self.show()
 
    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
      pass
    ''' створює графічні елементи '''
    def initUI(self):
       pass
 
    def next_click(self):
      pass
 
    def timer_test(self):
      pass
 
    def timer_sits(self):
      pass
 
    def timer_final(self):
      pass
 
    def timer1Event(self):
      pass
 
    def timer2Event(self):
      pass
 
    def timer3Event(self):
      pass
 
    def connects(self):
       self.btn_next.clicked.connect(self.next_click)

