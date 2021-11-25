from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random
import os

class Ui_Play_AE(object):

        ##สร้างฟังก์ชันเพื่อเก็บค่า score ตอนเริ่มโปรแกรม
        def __init__(self) -> None:
                super().__init__()
                self.score = 0
                self.find_correct = 0

        def back_menu(self):
                from menu_ae import Ui_Main_AE
                self.menu = QtWidgets.QMainWindow()
                self.ui = Ui_Main_AE()
                self.ui.setupUi(self.menu)
                self.menu.show()
        
        def setupUi(self, Play_AE):
                Play_AE.setObjectName("Play_AE")
                Play_AE.resize(1920, 1080)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image/Picture/cards.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                Play_AE.setWindowIcon(icon)
                Play_AE.setStyleSheet("background-image: url(:/image/Picture/play_menu.jpg);")
                self.centralwidget = QtWidgets.QWidget(Play_AE)
                self.centralwidget.setObjectName("centralwidget")
                self.btn_play = QtWidgets.QPushButton(self.centralwidget)
                self.btn_play.setGeometry(QtCore.QRect(690, 400, 88, 88))
                self.btn_play.setStyleSheet("background-image: url(:/image/Picture/play.png);")
                self.btn_play.setText("")
                self.btn_play.setIconSize(QtCore.QSize(20, 20))
                self.btn_play.setAutoDefault(False)
                self.btn_play.setDefault(False)
                self.btn_play.setFlat(True)
                self.btn_play.setObjectName("btn_play")
                self.btn_correct = QtWidgets.QPushButton(self.centralwidget)
                self.btn_correct.setGeometry(QtCore.QRect(232, 790, 421, 91))
                self.btn_correct.setStyleSheet("QPushButton{\n"
        "    font: 25pt \"Mitr SemiBold\";\n"
        "    color: rgb(255, 255, 255);\n"
        "    background: #009933;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #009960;\n"
        "}")
                self.btn_correct.setObjectName("btn_correct")
                self.btn_back = QtWidgets.QPushButton(self.centralwidget)
                self.btn_back.setGeometry(QtCore.QRect(110, 90, 93, 93))
                self.btn_back.setStyleSheet("background-image: url(:/image/Picture/back.png);")
                self.btn_back.setText("")
                self.btn_back.setFlat(True)
                self.btn_back.setObjectName("btn_back")
                self.btn_show = QtWidgets.QPushButton(self.centralwidget)
                self.btn_show.setGeometry(QtCore.QRect(575, 500, 321, 71))
                self.btn_show.setStyleSheet("QPushButton{\n"
        "    font: 25pt \"Mitr SemiBold\";\n"
        "    color: dark;\n"
        "    background: transparent;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #a3ffdd;\n"
        "}")
                self.btn_show.setAutoDefault(False)
                self.btn_show.setDefault(False)
                self.btn_show.setFlat(True)
                self.btn_show.setObjectName("btn_show")
                self.btn_incorrect = QtWidgets.QPushButton(self.centralwidget)
                self.btn_incorrect.setGeometry(QtCore.QRect(809, 790, 421, 91))
                self.btn_incorrect.setStyleSheet("QPushButton{\n"
        "    font: 25pt \"Mitr SemiBold\";\n"
        "    color: rgb(255, 255, 255);\n"
        "    background: #CC0033;\n"
        "}\n"
        "QPushButton:pressed {\n"
        "    background-color: #CC0050;\n"
        "}")
                self.btn_incorrect.setObjectName("btn_incorrect")
                self.label_question = QtWidgets.QLabel(self.centralwidget)
                self.label_question.setGeometry(QtCore.QRect(470, 310, 531, 51))
                self.label_question.setStyleSheet("font: 20pt \"Mitr SemiBold\";\n"
        "background: transparent;")
                self.label_question.setAlignment(QtCore.Qt.AlignCenter)
                self.label_question.setObjectName("label_question")
                self.label_answer = QtWidgets.QLabel(self.centralwidget)
                self.label_answer.setGeometry(QtCore.QRect(470, 620, 531, 51))
                self.label_answer.setStyleSheet("font: 20pt \"Mitr SemiBold\";\n"
        "background: transparent;")
                self.label_answer.setAlignment(QtCore.Qt.AlignCenter)
                self.label_answer.setObjectName("label_answer")
                self.label_score = QtWidgets.QLabel(self.centralwidget)
                self.label_score.setGeometry(QtCore.QRect(1457, 385, 321, 51))
                self.label_score.setStyleSheet("font: 40pt \"Mitr SemiBold\";\n"
        "background: transparent;")
                self.label_score.setAlignment(QtCore.Qt.AlignCenter)
                self.label_score.setObjectName("label_score")
                Play_AE.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(Play_AE)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
                self.menubar.setObjectName("menubar")
                Play_AE.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(Play_AE)
                self.statusbar.setObjectName("statusbar")
                Play_AE.setStatusBar(self.statusbar)

                self.btn_back.clicked.connect(self.back_menu)
                self.btn_back.clicked.connect(Play_AE.hide)
                self.label_answer.setVisible(True)
                self.btn_play.clicked.connect(self.play)
                self.btn_show.clicked.connect(self.show)
                self.btn_correct.clicked.connect(self.correct)
                self.btn_incorrect.clicked.connect(self.incorrect)

                self.retranslateUi(Play_AE)
                QtCore.QMetaObject.connectSlotsByName(Play_AE)

        def retranslateUi(self, Play_AE):
                _translate = QtCore.QCoreApplication.translate
                Play_AE.setWindowTitle(_translate("Play_AE", "Play A-E"))
                self.btn_play.setToolTip(_translate("Play_AE", "<html><head/><body><p>กดปุ่มเพื่อเล่นสุ่มคำศัพท์</p></body></html>"))
                self.btn_correct.setText(_translate("Play_AE", "CORRECT"))
                self.btn_back.setToolTip(_translate("Play_AE", "<html><head/><body><p>กดปุ่มเพื่อกลับหน้าแรก</p></body></html>"))
                self.btn_show.setText(_translate("Play_AE", "SHOW ANSWER"))
                self.btn_incorrect.setText(_translate("Play_AE", "INCORRECT"))
                self.label_question.setText(_translate("Play_AE", "Question"))
                self.label_answer.setText(_translate("Play_AE", "Answer"))
                self.label_score.setText(_translate("Play_AE", "0"))
                self.btn_play.setShortcut("A")
                self.btn_show.setShortcut("S")
                self.btn_correct.setShortcut("D")
                self.btn_incorrect.setShortcut("F")
        
        def play(self):
                file = "a_e.txt"
                a_e = {}
                msg = QMessageBox()
                msg.setWindowTitle("ไม่พบคำศัพท์")
                msg.setIcon(QMessageBox.Information)
                with open(file, "a", encoding="UTF-8") as f:
                        filesize = os.path.getsize("a_e.txt")
                        if filesize == 0:
                                msg.setText("ไม่พบคำศัพท์ในระบบ")
                                x = msg.exec_()
                        else:
                                with open(file,encoding="UTF-8") as f:
                                        for line in f:
                                                line = line.replace('\n','')
                                                line = line.replace('_',' ')
                                                (Question,Answer) = line.split('=')
                                                a_e.setdefault(Question,[])
                                                a_e[Question].append(Answer) #ให้จำนวนของ values ขึ้นอยู่กับข้อมูลของ values ที่มี
                                        random_ae = random.choice(list(a_e.items()))
                                ans = ", "
                                self.label_question.setText(random_ae[0])
                                self.label_answer.setText("{}".format(ans.join(random_ae[1])))
                                self.label_question.setVisible(True)
                                self.label_answer.setVisible(False)
        
        def show(self):
                self.find_correct = 1
                self.label_answer.setVisible(True)
                self.label_question.setVisible(True)
                
        def correct(self):
                if self.find_correct == 0:
                        pass
                else:
                        self.score += 1
                        self.label_score.setText(f"{self.score}")
                        self.label_question.setVisible(False)
                        self.label_answer.setVisible(False)
                self.find_correct = 0

        def incorrect(self):
                self.label_question.setVisible(False)
                self.label_answer.setVisible(False)
                self.find_correct = 0

import vocab_pic1_rc

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Play_AE = QtWidgets.QMainWindow()
        ui = Ui_Play_AE()
        ui.setupUi(Play_AE)
        Play_AE.show()
        sys.exit(app.exec_())
