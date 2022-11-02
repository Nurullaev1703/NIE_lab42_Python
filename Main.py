#!/usr/bin/env python3
#coding=utf-8

import re
import sys
import textwrap

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        try:
            text = self.textEdit_text.toPlainText()  # получаем наш текст;
            text1 = text.split()
            answer = re.findall(r'[a-zA-Za-яА-ЯёЁ\']{2,}', str(text1))
            longest = max(answer,key=len)
            shortest = min(answer,key=len)
            self.textEdit_words.setText("Самое длинное слово: " + longest +"\n" + "Самое короткое слово: " + shortest)
            print(answer)
        except:
            self.textEdit_words.setText("Ошибка ввода")


    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
