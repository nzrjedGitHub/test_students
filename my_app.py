from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # перевірка типів значень, що вводяться
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
 
     
class MainWin(QWidget):
    def __init__(self):
        ''' вікно, в якому розташовується привітання '''
        super().__init__()
 
        #Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.set_appear()
 
        # створюємо та налаштовуємо графічні елементи:
        self.initUI()
 
        #Встановлює зв'язки між елементами
        self.connects()
 
        # старт:
        self.show()
 
    def initUI(self):
        ''' створює графічні елементи '''
        pass
 
 
    def next_click(self):
        pass
 
    def connects(self):
        pass
 
    ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
    def set_appear(self):
        pass
 
def main():
    pass
 
main()
