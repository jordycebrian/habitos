
import pyodbc

class ControlHabitos():
    def __init__(self):
        """Conxion base sqlserver"""
        conn = pyodbc.connect('Driver={ODBC Driver 17 for Sql Server};'
        'Server=DESKTOP-H2RJN7F;'
        'Database=BaseHabitos;'
        'UID=sa;'
        'PWD=cero41')

        self.cursor = conn.cursor()
        """fin conexion base"""

    """Construccion funciones para control de habitos"""
    def mostrar(self):
        try:
            self.cursor.execute('SELECT * FROM habitos')
            return "".join( str(f"Clave: {elementos[0]}\nNombre: {elementos[1]}\nHora Inicio: {elementos[2]}\nFin de la hora: {elementos[3]}\nFecha de Inicio: {elementos[4]}\nFecha Ultimo Día: {elementos[-1]}") + '\n'  for elementos in self.cursor)
        except Exception as e:
            return f"Error Fallo de consulta", e

    def insertar(self, clave, nombre, horaIncio, finHora, fechaInicio, fechaFinal):

        try:
            query = ('INSERT INTO habitos(idhabito,nombre,desde,hasta,iniciohabito,finhabito) VALUES(?,?,?,?,?,?)')
            self.cursor.execute(query,[clave,nombre,horaIncio,finHora,fechaInicio,fechaFinal])
            self.cursor.commit()
        except Exception as e:
            return f"Fallo de consulta",e

    
    def actualizar(self, clave, nombre, horaInicio, finHora, fechaInicio, fechaFinal):
        try:
            query = ('UPDATE habitos SET nombre = ?,desde = ?,hasta = ?,iniciohabito = ?,finhabito = ? WHERE idhabito = ?')
            self.cursor.execute(query,[nombre,horaInicio,finHora,fechaInicio,fechaFinal,clave])
            self.cursor.commit()
        except Exception as e:
            return f"Fallo de consulta",e
    
    def borrar(self, clave):
        try:
            query = ('DELETE FROM habitos WHERE idhabito = ?')
            self.cursor.execute(query,[clave])
            self.cursor.commit()
        except Exception as e:
            return "Error de consulta" , e
    """Fin Construccion funciones para control de habitos"""
