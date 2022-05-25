from PySide2.QtWidgets import QMainWindow,QMessageBox
from PySide2.QtCore import Slot
from ui_habitos import Ui_MainWindow
from habitcontrol import ControlHabitos

"""menu"""

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.acciones = ControlHabitos()
        """Objetos ui"""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnmostrar.clicked.connect(self.click_mostrar)
        self.ui.btnagreagar.clicked.connect(self.agregar_habito)
        self.ui.btneliminar.clicked.connect(self.borrar_habito)
        self.ui.btneditar.clicked.connect(self.actualizar_habito)
        """Fin objetos ui"""
    
    """Inicio construccion funciones"""
    @Slot()
    def click_mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.acciones.mostrar()))

    @Slot()
    def agregar_habito(self):
        clave = self.ui.txtclave.text()
        nombre = self.ui.txtnombre.text()
        horaInicio = self.ui.txtdesde.text()
        horaHasta = self.ui.txthasta.text()
        fechaIncio = self.ui.txtinicio.text()
        fechaFinal = self.ui.txtfechahasta.text()

        try:
            self.acciones.insertar(clave,nombre,horaInicio,horaHasta,fechaIncio,fechaFinal)
            QMessageBox.information(self,"Exito","Habito Guardado")
        except Exception:
            QMessageBox.critical(self, 'Error', ' Fallo al guardar')


    @Slot()
    def actualizar_habito(self):

        clave = self.ui.txtclave.text()
        nombre = self.ui.txtnombre.text()
        horaInicio = self.ui.txtdesde.text()
        horaHasta = self.ui.txthasta.text()
        fechaInicio = self.ui.txtinicio.text()
        fechaFinal = self.ui.txtfechahasta.text()
        

        try:
            self.acciones.actualizar(clave,nombre,horaInicio,horaHasta,fechaInicio,fechaFinal)
            QMessageBox.information(self,"Exito","Habito Actualizado")
        except Exception:
            QMessageBox.critical(self, 'Error', ' Fallo al Actualizar')
        

    @Slot()
    def borrar_habito(self):
        clave = self.ui.txtclave.text()
        try:
            self.acciones.borrar(clave)
            QMessageBox.information(self,"Exito","Habito Borrado")
        except Exception:
            QMessageBox.critical(self, 'Error', ' Fallo al Borrar')
    """Fin de funciones"""

"""Fin del menu"""