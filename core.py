from PySide2.QtWidgets import QApplication
from main import MainWindow
import sys

"""core for run app"""
app = QApplication()

window = MainWindow()
window.show()

"""Salida de loop"""
sys.exit(app.exec_())