import pygame
from accesoDatos import AccesoDatos

class Inicio():

    def dibujar1(self, pantalla, event):
        self.fondo=pygame.image.load("img/Bienvenido.png")
        self.color=(255,255,255)
        self.seleccionAncho=160
        self.seleccionAlto=5
        self.seleccionX=200
        self.seleccionY=730

        pantalla.blit(self.fondo, [0, 0])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and self.seleccionX==200:
                self.seleccionX=440
            if event.key == pygame.K_LEFT and self.seleccionX==440:
                self.seleccionX=200

        self.seleccion= pygame.draw.rect(pantalla, self.color, (self.seleccionX, self.seleccionY, self.seleccionAncho, self.seleccionAlto))

    def dibujar2(self, pantalla):
        self.fondo=pygame.image.load("img/inicio.png")
        pantalla.blit(self.fondo, [0, 0])

    def dibujar3(self, pantalla):  #cargarJuego-ListarRanking
        pass

    def guardar(self, accion, nombreJugador, seleccionado, id):
        self.agregar="insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('"+str(nombreJugador)+"',"+str(seleccionado)+",0,0);"
        self.modificar="UPDATE historial SET nombre = '"+str(nombreJugador)+"' WHERE id="+str(id)+";"
        self.eliminar="delete from historial where id="+str(id)+";"
        self.string=None
        if accion==1:
            self.string=self.agregar
        if accion==2:
            self.string=self.modificar
        if accion==3:
            self.string=self.eliminar
        acceso=AccesoDatos()
        acceso.ejecutarAccion(self.string)
        
s
###########################----  Prueba

#medidaPantalla = (800,750)
#pantalla = pygame.display.set_mode(medidaPantalla)
#inicio=True

#inicio=Inicio()
#inicio.dibujar(pantalla)

#pygame.display.flip()
