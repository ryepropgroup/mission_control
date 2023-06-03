# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer, QDate, Qt

#from linearGauge file to add linear gauge custom widgets
from updated_gauge import LinearGauge

from functools import partial

#allow different parts of the program to run concurrently 
import threading

#impot time module to allow python to work with time
import time

#allowing us to work with JSON data
import json



import socket
PORT = 6970





import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt, QRect, QBasicTimer, QPoint  # Import QPoint
from PyQt5.QtGui import QPainter, QPen, QFont, QColor, QPolygon

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 872)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.p_and_id = QtWidgets.QLabel(self.centralwidget)
        self.p_and_id.setGeometry(QtCore.QRect(0, 0, 1441, 831))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.p_and_id.setFont(font)
        self.p_and_id.setText("")
        self.p_and_id.setPixmap(QtGui.QPixmap("pid.png"))
        self.p_and_id.setScaledContents(True)
        self.p_and_id.setObjectName("p_and_id")

        self.mach_logo = QtWidgets.QLabel(self.centralwidget)
        self.mach_logo.setGeometry(QtCore.QRect(10, 10, 281, 201))
        self.mach_logo.setText("")
        self.mach_logo.setPixmap(QtGui.QPixmap("mach_logo.png"))
        self.mach_logo.setScaledContents(True)
        self.mach_logo.setObjectName("mach_logo")

        #time label
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(330, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        
        #date label
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(330, 70, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.date_label.setFont(font)
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")

        #update date and time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)


        #Valve 10 sb open, close, and state
        self.V10_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V10_SB_open.setGeometry(QtCore.QRect(350, 350, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V10_SB_open.setFont(font)
        self.V10_SB_open.setObjectName("V10_SB_open")
        self.V10_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V10_SB_open.clicked.connect(lambda: self.open_valve(b"V10_SB_open\n"))
        self.V10_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V10_SB_close.setGeometry(QtCore.QRect(350, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V10_SB_close.setFont(font)
        self.V10_SB_close.setObjectName("V10_SB_close")
        self.V10_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V10_SB_close.clicked.connect(lambda: self.close_valve(b"V10_SB_close\n"))
        self.V10_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V10_SB_state.setGeometry(QtCore.QRect(350, 320, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V10_SB_state.setFont(font)
        self.V10_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V10_SB_state.setObjectName("Current State")
        self.V10_SB_state.setStyleSheet("color: blue; font-size: 16px;")   


        #v11 s no open, close, and state
        self.V11_S_NO_open = QtWidgets.QPushButton(self.centralwidget)
        self.V11_S_NO_open.setGeometry(QtCore.QRect(220, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V11_S_NO_open.setFont(font)
        self.V11_S_NO_open.setObjectName("V11_S_NO_open")
        self.V11_S_NO_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V11_S_NO_open.clicked.connect(lambda: self.open_valve(b"V11_S_open\n"))
        self.V11_S_NO_close = QtWidgets.QPushButton(self.centralwidget)
        self.V11_S_NO_close.setGeometry(QtCore.QRect(220, 580, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V11_S_NO_close.setFont(font)
        self.V11_S_NO_close.setObjectName("V11_S_NO_close")
        self.V11_S_NO_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V11_S_NO_close.clicked.connect(lambda: self.close_valve(b"V11_S_close\n"))
        self.V11_S_NO_state = QtWidgets.QLabel(self.centralwidget)
        self.V11_S_NO_state.setGeometry(QtCore.QRect(220, 610, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V11_S_NO_state.setFont(font)
        self.V11_S_NO_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V11_S_NO_state.setObjectName("Current State")
        self.V11_S_NO_state.setStyleSheet("color: blue; font-size: 16px;")


        #v12_s_no open, close, and state
        self.V12_S_NO_open = QtWidgets.QPushButton(self.centralwidget)
        self.V12_S_NO_open.setGeometry(QtCore.QRect(350, 550, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V12_S_NO_open.setFont(font)
        self.V12_S_NO_open.setObjectName("V12_S_open")
        self.V12_S_NO_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V12_S_NO_open.clicked.connect(lambda: self.open_valve(b"V12_S_open\n"))
        self.V12_S_NO_close = QtWidgets.QPushButton(self.centralwidget)
        self.V12_S_NO_close.setGeometry(QtCore.QRect(350, 580, 71, 21))
        self.V12_S_NO_close.setObjectName("V12_S_close")
        self.V12_S_NO_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V12_S_NO_close.clicked.connect(lambda: self.close_valve(b"V12_S_close\n"))
        self.V12_S_state = QtWidgets.QLabel(self.centralwidget)
        self.V12_S_state.setGeometry(QtCore.QRect(350, 610, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V12_S_state.setFont(font)
        self.V12_S_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V12_S_state.setObjectName("Current State")
        self.V12_S_state.setStyleSheet("color: blue; font-size: 16px;") 

        
    
        self.V20_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V20_SB_open.setGeometry(QtCore.QRect(1150, 250, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V20_SB_open.setFont(font)
        self.V20_SB_open.setObjectName("V20_SB_open")
        self.V20_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V20_SB_open.clicked.connect(lambda: self.open_valve(b"V20_SB_open\n"))
        self.V20_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V20_SB_close.setGeometry(QtCore.QRect(1150, 280, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V20_SB_close.setFont(font)
        self.V20_SB_close.setObjectName("V20_SB_close")
        self.V20_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V20_SB_close.clicked.connect(lambda: self.close_valve(b"V20_SB_close\n"))
        self.V20_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V20_SB_state.setGeometry(QtCore.QRect(1150, 220, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V20_SB_state.setFont(font)
        self.V20_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V20_SB_state.setObjectName("Current State")
        self.V20_SB_state.setStyleSheet("color: blue; font-size: 16px;") 


        self.V21_MB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V21_MB_open.setGeometry(QtCore.QRect(510, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V21_MB_open.setFont(font)
        self.V21_MB_open.setObjectName("V21_MB_open")
        self.V21_MB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V21_MB_open.clicked.connect(lambda: self.open_valve(b"V21_SB_open\n"))
        self.V21_MB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V21_MB_close.setGeometry(QtCore.QRect(590, 370, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V21_MB_close.setFont(font)
        self.V21_MB_close.setObjectName("V21_MB_close")
        self.V21_MB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V21_MB_close.clicked.connect(lambda: self.close_valve(b"V21_SB_close\n"))
        self.V21_MB_state = QtWidgets.QLabel(self.centralwidget)
        self.V21_MB_state.setGeometry(QtCore.QRect(550, 400, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V21_MB_state.setFont(font)
        self.V21_MB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V21_MB_state.setObjectName("Current State")
        self.V21_MB_state.setStyleSheet("color: blue; font-size: 16px;") 

        self.V23_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V23_SB_open.setGeometry(QtCore.QRect(590, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V23_SB_open.setFont(font)
        self.V23_SB_open.setObjectName("V22_SB_open")
        self.V23_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V23_SB_open.clicked.connect(lambda: self.open_valve(b"V23_SB_open\n"))
        self.V23_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V23_SB_close.setGeometry(QtCore.QRect(590, 200, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V23_SB_close.setFont(font)
        self.V23_SB_close.setObjectName("V22_SB_close")
        self.V23_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V23_SB_close.clicked.connect(lambda: self.close_valve(b"V23_SB_close\n"))
        self.V23_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V23_SB_state.setGeometry(QtCore.QRect(670, 200, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V23_SB_state.setFont(font)
        self.V23_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V23_SB_state.setObjectName("Current State")
        self.V23_SB_state.setStyleSheet("color: blue; font-size: 16px;") 
       
        self.V30_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V30_SB_open.setGeometry(QtCore.QRect(1130, 570, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V30_SB_open.setFont(font)
        self.V30_SB_open.setObjectName("V30_SB_open")
        self.V30_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V30_SB_open.clicked.connect(lambda: self.open_valve(b"V30_SB_open\n"))
        self.V30_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V30_SB_close.setGeometry(QtCore.QRect(1130, 600, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V30_SB_close.setFont(font)
        self.V30_SB_close.setObjectName("V30_SB_close")
        self.V30_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }""QPushButton:pressed { background-color: #4d0505; }")
        self.V30_SB_close.clicked.connect(lambda: self.close_valve(b"V30_SB_close\n"))
        self.V30_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V30_SB_state.setGeometry(QtCore.QRect(1130, 540, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V30_SB_state.setFont(font)
        self.V30_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V30_SB_state.setObjectName("Current State")
        self.V30_SB_state.setStyleSheet("color: blue; font-size: 16px;") 


        self.V31_MB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V31_MB_open.setGeometry(QtCore.QRect(580, 580, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V31_MB_open.setFont(font)
        self.V31_MB_open.setObjectName("V31_SB_open")
        self.V31_MB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V31_MB_open.clicked.connect(lambda: self.open_valve(b"V31_SB_open\n"))
        self.V31_MB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V31_MB_close.setGeometry(QtCore.QRect(580, 610, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V31_MB_close.setFont(font)
        self.V31_MB_close.setObjectName("V30_SB_close")
        self.V31_MB_close.setStyleSheet("QPushButton { background-color: red; color: white; }""QPushButton:pressed { background-color: #4d0505; }")
        self.V31_MB_close.clicked.connect(lambda: self.close_valve(b"V31_SB_close\n"))
        self.V31_MB_state = QtWidgets.QLabel(self.centralwidget)
        self.V31_MB_state.setGeometry(QtCore.QRect(580, 550, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V31_MB_state.setFont(font)
        self.V31_MB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V31_MB_state.setObjectName("Current State")
        self.V31_MB_state.setStyleSheet("color: blue; font-size: 16px;") 


        

        
        self.V34_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V34_SB_open.setGeometry(QtCore.QRect(460, 730, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V34_SB_open.setFont(font)
        self.V34_SB_open.setObjectName("V34_SB_open")
        self.V34_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }""QPushButton:pressed { background-color: #074d05; }")
        self.V34_SB_open.clicked.connect(lambda: self.open_valve(b"V34_SB_open\n"))
        self.V34_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V34_SB_close.setGeometry(QtCore.QRect(460, 760, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V34_SB_close.setFont(font)
        self.V34_SB_close.setObjectName("V34_SB_close")
        self.V34_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V34_SB_close.clicked.connect(lambda: self.close_valve(b"V34_SB_close\n"))
        self.V34_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V34_SB_state.setGeometry(QtCore.QRect(370, 740, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V34_SB_state.setFont(font)
        self.V34_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V34_SB_state.setObjectName("Current State")
        self.V34_SB_state.setStyleSheet("color: blue; font-size: 16px;") 



        

       



       

        self.V35_S_open = QtWidgets.QPushButton(self.centralwidget)
        self.V35_S_open.setGeometry(QtCore.QRect(660, 790, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V35_S_open.setFont(font)
        self.V35_S_open.setObjectName("V35_S_open")
        self.V35_S_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V35_S_open.clicked.connect(lambda: self.open_valve(b"V35_S_open\n")) 
        self.V35_S_close = QtWidgets.QPushButton(self.centralwidget)
        self.V35_S_close.setGeometry(QtCore.QRect(740, 790, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V35_S_close.setFont(font)
        self.V35_S_close.setObjectName("V35_S_close")
        self.V35_S_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V35_S_close.clicked.connect(lambda: self.close_valve(b"V35_S_close\n"))
        self.V35_S_state = QtWidgets.QLabel(self.centralwidget)
        self.V35_S_state.setGeometry(QtCore.QRect(660, 760, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V35_S_state.setFont(font)
        self.V35_S_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V35_S_state.setObjectName("Current State")
        self.V35_S_state.setStyleSheet("color: blue; font-size: 16px;") 

        self.V36_SB_open = QtWidgets.QPushButton(self.centralwidget)
        self.V36_SB_open.setGeometry(QtCore.QRect(880, 700, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V36_SB_open.setFont(font)
        self.V36_SB_open.setObjectName("V36_SB_open")
        self.V36_SB_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V36_SB_open.clicked.connect(lambda: self.open_valve(b"V36_SB_open\n"))
        self.V36_SB_close = QtWidgets.QPushButton(self.centralwidget)
        self.V36_SB_close.setGeometry(QtCore.QRect(880, 730, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V36_SB_close.setFont(font)
        self.V36_SB_close.setObjectName("V36_SB_close")
        self.V36_SB_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V36_SB_close.clicked.connect(lambda: self.close_valve(b"V36_SB_close\n"))
        self.V36_SB_state = QtWidgets.QLabel(self.centralwidget)
        self.V36_SB_state.setGeometry(QtCore.QRect(800, 710, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V36_SB_state.setFont(font)
        self.V36_SB_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V36_SB_state.setObjectName("Current State")
        self.V36_SB_state.setStyleSheet("color: blue; font-size: 16px;") 


        self.V37_S_open = QtWidgets.QPushButton(self.centralwidget)
        self.V37_S_open.setGeometry(QtCore.QRect(870, 790, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V37_S_open.setFont(font)
        self.V37_S_open.setObjectName("V37_S_open")
        self.V37_S_open.setStyleSheet("QPushButton { background-color: #12b81b; color: white; }" "QPushButton:pressed { background-color: #074d05; }")
        self.V37_S_open.clicked.connect(lambda: self.open_valve(b"V37_S_open\n"))
        self.V37_S_close = QtWidgets.QPushButton(self.centralwidget)
        self.V37_S_close.setGeometry(QtCore.QRect(950, 790, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.V37_S_close.setFont(font)
        self.V37_S_close.setObjectName("V37_S_close")
        self.V37_S_close.setStyleSheet("QPushButton { background-color: red; color: white; }" "QPushButton:pressed { background-color: #4d0505; }")
        self.V37_S_close.clicked.connect(lambda: self.close_valve(b"V37_S_close\n"))
        self.V37_S_state = QtWidgets.QLabel(self.centralwidget)
        self.V37_S_state.setGeometry(QtCore.QRect(1020, 790, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.V37_S_state.setFont(font)
        self.V37_S_state.setAlignment(QtCore.Qt.AlignCenter)
        self.V37_S_state.setObjectName("Current State")
        self.V37_S_state.setStyleSheet("color: blue; font-size: 16px;") 


        

        self.P10 = LinearGauge(self.centralwidget)
        self.P10.setGeometry(QtCore.QRect(200, 330, 100, 60))
        self.P10.setObjectName("P10")
        
        
        self.P21 = LinearGauge(self.centralwidget)
        self.P21.setGeometry(QtCore.QRect(890, 390, 100, 60))
        self.P21.setObjectName("P21")

        self.P22 = LinearGauge(self.centralwidget)
        self.P22.setGeometry(QtCore.QRect(1070, 340, 100, 60))
        self.P22.setObjectName("P22")

        self.P32 = LinearGauge(self.centralwidget)
        self.P32.setGeometry(QtCore.QRect(1070, 430, 100, 60))
        self.P32.setObjectName("P32")

        self.P20 = LinearGauge(self.centralwidget)
        self.P20.setGeometry(QtCore.QRect(1300, 290, 100, 60))
        self.P20.setObjectName("P20")

        self.P30 = LinearGauge(self.centralwidget)
        self.P30.setGeometry(QtCore.QRect(1300, 560, 100, 60))
        self.P30.setObjectName("P30")

        self.P31 = LinearGauge(self.centralwidget)
        self.P31.setGeometry(QtCore.QRect(860, 540, 100, 60))
        self.P31.setObjectName("P31")


        self.T3_N2O_run = QtWidgets.QLabel(self.centralwidget)
        self.T3_N2O_run.setGeometry(QtCore.QRect(740, 600, 71, 21))
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.T3_N2O_run.setFont(font)
        self.T3_N2O_run.setAlignment(QtCore.Qt.AlignCenter)
        self.T3_N2O_run.setStyleSheet("color: red; font-size: 16px;") 
 


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_date_time(self): 

        #set the current date and time 
        current_time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
        current_date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)

        #update date and time 
        self.date_label.setText(current_time)
        self.time_label.setText(current_date)



    def receive_until_newline(self):
        data = b''  # Initialize an empty byte string to store the received data

        while True:
            chunk = s.recv(32)  # Receive data in chunks of 1024 bytes
            data += chunk  # Append the received data to the existing data

            if b'\n' in chunk:
                break  # Break the loop when a newline character is received
        #find index of new line
        data = data.decode('utf-8')  # Convert the byte string to a Unicode string
        index = data.index('\n')
        #trunicate
        #print(data[:index]) 
        return data[:index].strip()
        
        

    def update_valve_state(self): 
       
        while True:
            try:
                json_str = self.receive_until_newline()
                json_data = json.loads(json_str)
                p1_val = json_data['lj']['p1val']
                p2_val = json_data['lj']['p2val']
                p3_val = json_data['lj']['p3val']

                v11_s  = json_data['valves']['V11_S']
                v10_sb = json_data['valves']['V10_SB']
                v12_s  = json_data['valves']['V12_S']

                v20_sb = json_data['valves']['V20_SB']
                v21_sb = json_data['valves']['V21_SB']
                v23_sb = json_data['valves']['V23_SB']

                v30_sb = json_data['valves']['V30_SB']
                v31_sb = json_data['valves']['V30_SB']
                v34_sb = json_data['valves']['V34_SB']
                v35_s =  json_data['valves']['V35_S']
                v36_sb = json_data['valves']['V36_SB']
                v37_s  = json_data['valves']['V37_S']

                t3_thermo = json_data['lj']['t1val']

                print(json_data)

                #self.P21.setValue(int(p1_val))
                self.P31.setValue(int(p2_val))
                self.P21.setValue(int(p3_val))

                #set valve state
                self.V10_SB_state.setText(self.translateState(str(v10_sb)))
                self.V11_S_NO_state.setText(self.translateState(str(v11_s)))
                self.V12_S_state.setText(self.translateState(str(v12_s)))

                self.V20_SB_state.setText(self.translateState(str(v20_sb)))
                self.V21_SB_state.setText(self.translateState(str(v21_sb)))
                self.V23_SB_state.setText(self.translateState(str(v23_sb)))

                self.V30_SB_state.setText(self.translateState(str(v30_sb)))
                self.V31_SB_state.setText(self.translateState(str(v31_sb)))
                self.V34_SB_state.setText(self.translateState(str(v34_sb)))
                self.V35_S_state.setText(self.translateState(str(v35_s)))
                self.V36_SB_state.setText(self.translateState(str(v36_sb)))
                self.V37_S_state.setText(self.translateState(str(v37_s)))


                #set thermocouples 
                self.T3_N2O_run.setText(str(t3_thermo))

                valves = json_data['valves']
                print("P1 Value:", p1_val)
                print("P2 Value:", p2_val)
                print("P3 Value:", p3_val)
                print("Valves:", valves)

            except json.JSONDecodeError:
                pass
                
    def translateState(self, string):
        if string == "False": 
            field = "Closed"
            return(field)
        elif string == "True": 
            field = "Open"
            return(field)


    def connect(self): 
        global s 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp socket

        try: 
            s.connect(("127.0.0.1", PORT)) #connect to mini server
            print('connected')
        except Exception: 
            s.close()

    def open_valve(self,name): 
        s.send(name)
  
    def close_valve(self,name): 
        s.send(name)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.time_label.setText(_translate("MainWindow", "TextLabel"))
        self.date_label.setText(_translate("MainWindow", "TextLabel"))



        self.V10_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V10_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V10_SB_state.setText(_translate("MainWindow", "STATE"))
    
        self.V11_S_NO_open.setText(_translate("MainWindow", "OPEN"))
        self.V11_S_NO_close.setText(_translate("MainWindow", "CLOSE"))
        self.V11_S_NO_state.setText(_translate("MainWindow", "STATE"))

        self.V12_S_NO_open.setText(_translate("MainWindow", "OPEN"))
        self.V12_S_NO_close.setText(_translate("MainWindow", "CLOSE"))     
        self.V12_S_state.setText(_translate("MainWindow", "STATE"))

        self.V20_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V20_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V20_SB_state.setText(_translate("MainWindow", "STATE"))

        self.V21_MB_open.setText(_translate("MainWindow", "OPEN"))
        self.V21_MB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V21_MB_state.setText(_translate("MainWindow", "STATE"))

        self.V23_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V23_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V23_SB_state.setText(_translate("MainWindow", "STATE"))

        self.V30_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V30_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V30_SB_state.setText(_translate("MainWindow", "STATE"))

        self.V31_MB_open.setText(_translate("MainWindow", "OPEN"))
        self.V31_MB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V31_MB_state.setText(_translate("MainWindow", "STATE"))

        self.V34_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V34_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V34_SB_state.setText(_translate("MainWindow", "STATE"))

        self.V35_S_open.setText(_translate("MainWindow", "OPEN"))
        self.V35_S_close.setText(_translate("MainWindow", "CLOSE"))
        self.V35_S_state.setText(_translate("MainWindow", "STATE"))

        self.V36_SB_open.setText(_translate("MainWindow", "OPEN"))
        self.V36_SB_close.setText(_translate("MainWindow", "CLOSE"))
        self.V36_SB_state.setText(_translate("MainWindow", "STATE"))

        self.V37_S_open.setText(_translate("MainWindow", "OPEN"))
        self.V37_S_close.setText(_translate("MainWindow", "CLOSE"))
        self.V37_S_state.setText(_translate("MainWindow", "STATE"))

        self.T3_N2O_run.setText(_translate("MainWinsow", "Temp"))

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.connect()
    update_thread = threading.Thread(target=ui.update_valve_state, daemon=True)
    update_thread.start()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
