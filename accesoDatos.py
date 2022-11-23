import mysql.connector
import string
from mysql.connector import Error


class AccesoDatos:
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='shooter_db')
        except Error as ex:
            print(f'Fallo: {ex}')
    
    def ejecutarAccion(self, string):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute(string)
                self.conexion.commit()
            except Error as ex:
                print(f'Fallo: {ex}')

    def listarRanking(self):

        if self.conexion.is_connected():
            try:
                self.cursor=self.conexion.cursor()
                self.cursor.execute('select nombre, mejorPuntaje from historial order by mejorPuntaje desc limit 5;')
                self.respuesta=self.cursor.fetchall()
     
                return str(self.respuesta)
            except Error as ex:
                print(f'Fallo: {ex}')

    def buscarJugador(self, nombreJugador):
        if self.conexion.is_connected():
            try:
                self.nombre=nombreJugador
                self.cursor=self.conexion.cursor()
                self.cursor.execute(f"select nombre, id_avion from historial where nombre like '%{self.nombre}%' limit 3;")
                self.respuesta=self.cursor.fetchall()
                return self.respuesta


            except Error as ex:
                print(f'Fallo: {ex}')

    def buscarAvion(self, seleccion):
        self.seleccion=seleccion
        if self.conexion.is_connected():
            try:
                self.cursor=self.conexion.cursor()
                self.cursor.execute(f"select * from aviones where id={self.seleccion};")
                self.respuesta=self.cursor.fetchone()
                return self.respuesta

            except Error as ex:
                print(f'Fallo: {ex}')
    
    def buscarAvionJugador(self, nombre):
        if self.conexion.is_connected():
            try:
                self.cursor=self.conexion.cursor()
                self.cursor.execute(f"select id_avion from historial where nombre='{nombre}';")
                self.respuesta=self.cursor.fetchone()
                return self.respuesta

            except Error as ex:
                print(f'Fallo: {ex}')

