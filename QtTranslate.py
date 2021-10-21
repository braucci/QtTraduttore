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
    

    def pB_traducoClick(self):

        try:
        
            
            to_Translate = (self.lE_input.text())
            traduzione = t.Translator(to_lang="it")
            result = traduzione.translate(to_Translate)
            self.lE_output.setText(result)

        except:
            print('Valore nel campo non accettato')



app = QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec())