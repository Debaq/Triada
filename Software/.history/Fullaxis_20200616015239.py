#################################################################
#                                                               #
#                  NOMBRE PROYECTO : FULLAXIS                   #
#                       VER. 20.6 - GUI                         #
#               CREADOR : NICOLÁS QUEZADA QUEZADA               #
#                                                               #
#################################################################

## ==> LIBRERIAS BÁSICAS
import sys
import platform
import os

## ==> LIBRERIAS PYSIDE2
from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> LIBRERIAS PROPIAS
# BACKEND
from lib.ui_functions import *

# FRONTEND
from lib.uiForm.ui_main import Ui_FullAxis

## ==> LIBRERIAS PLUGINS
# AUN NO HAY NADA, TAREA : BUSCAR LA FORMA DE QUE SE CARGEN

#################################################################
#                      CLASE PRINCIPAL                          #
#################################################################

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_FullAxis()
        self.ui.setupUi(self)
        self.show()
        self.btn_basic()
        
    def btn_basic(self):
        self.ui.btn_ContractExplorer.clicked.connect(lambda: UIFunctions.toggleFrameOption_L5(self,20, True))
        self.ui.

        






#################################################################
#                      SE INICA EL PROGRAMA                     #
#################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 