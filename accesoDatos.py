import mysql.connector
from mysql.connector import Error

class AccesoDatos:
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(host='localhost' port=3306 user='root' password='' database='shooter_db')
        except Error as ex:
            print(f'Fallo: {ex}')
    
    def agregarJugador(self, string):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute(string)
                self.conexion.commit()
                print('guardadoOk')
            except Error as ex:
                print(f'Fallo: {ex}')

    def ejecutarAccion(self,string):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute(string)
                self.conexion.commit()
                print('guardadoOk')
            except Error as ex:
                print(f'Fallo: {ex}')

    def listarRanking(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute('select * from historial order by mejorPuntaje desc;')
                self.conexion.commit()
                print('guardadoOk')
            except Error as ex:
                print(f'Fallo: {ex}')
