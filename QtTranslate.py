#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

import translate as t
import sys


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setFixedSize(380, 225)
        lingue_list = ["it", "fr", "es", "ja", "pt"]
        self.cB_lingua.addItems(lingue_list)
        lingua = self.cB_lingua.currentText()

        if lingua == "it":
            lingua_estesa = "Italiano"
        if lingua == "fr":
            lingua_estesa = "Francese"
        if lingua == "es":
            lingua_estesa = "Spagnolo"
        if lingua == "ja":
            lingua_estesa = "Giapponese"
        if lingua == "pt":
            lingua_estesa = "Portoghese"

        self.label_2.setText(lingua_estesa)

    def cambio_lingua(self):
        lingua = self.cB_lingua.currentText()
        if lingua == "it":
            lingua_estesa = "Italiano"
        if lingua == "fr":
            lingua_estesa = "Francese"
        if lingua == "es":
            lingua_estesa = "Spagnolo"
        if lingua == "ja":
            lingua_estesa = "Giapponese"
        if lingua == "pt":
            lingua_estesa = "Portoghese"

        self.label_2.setText(lingua_estesa)
        

    def pB_traducoClick(self):

        try:
            to_Translate = (self.lE_input.text())
            lingua = self.cB_lingua.currentText()
            traduzione = t.Translator(to_lang=lingua)
            result = traduzione.translate(to_Translate)
            self.lE_output.setText(result)

        except:
            print('Valore nel campo non accettato')

    def cancello(self):
        self.lE_output.setText("")


app = QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec())
