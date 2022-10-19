import pygame
from accesoDatos import AccesoDatos

class Inicio():

    def dibujar1(self, pantalla):
        self.fondo=pygame.image.load("img/Bienvenido.png")
        self.enter=pygame.image.load("img/EnterCh.png")
        pantalla.blit(self.fondo, [0, 0])
        pantalla.blit(self.enter, [4, 680])

    def dibujar2(self, pantalla):
        self.fondo=pygame.image.load("img/inicio.png")
        self.enter=pygame.image.load("img/EnterCh.png")
        pantalla.blit(self.fondo, [0, 0])
        pantalla.blit(self.enter, [4, 680])


    def guardar(self, accion, nombreJugador, seleccionado, id):
        self.agregar="insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('"+str(nombreJugador)+"',"+str(seleccionado)+",0,0);"
        self.modificar="UPDATE historial SET nombre = '"+str(nombreJugador)+"' WHERE id="+str(id)+";"
        self.eliminar="delete from historial where id="+str(id)+";"
        self.string=None
        if accion==1:
            string=self.agregar
        if accion==2:
            string=self.modificar
        if accion==3:
            string=self.eliminar
        acceso=AccesoDatos()
        acceso.ejecutarAccion(self.string)
        

    ##################--Definir: seleccion de acciones para ingresar, modificar, listar y eliminar jugadores.
    ### Definir selección de avion

#prueba


#medidaPantalla = (800,750)
#pantalla = pygame.display.set_mode(medidaPantalla)
#inicio=True

#inicio=Inicio()
#inicio.dibujar(pantalla)

#pygame.display.flip()
