import pygame
from accesoDatos import AccesoDatos

class Finalizado():
    def __init__(self,nombre, puntos):
        self.acceso=AccesoDatos()
        self.puntajeActual=puntos
        self.historial=self.acceso.finalJuego(nombre)
        self.imagen=pygame.image.load('img/ganador.png')
        self.imagen.set_colorkey([255,255,255])
        self.texto1='Para volver a Jugar presioná ENTER'
        self.fuente=pygame.font.SysFont("Courier", 35, bold=True, italic=False)
        self.render1= self.fuente.render(self.texto1, True, (10,10,10), (140,203,221) )
        self.id=self.historial[0]
        self.nombre=self.historial[1]
        self.historialPuntos=self.historial[3]
        self.mejorPuntaje=self.historial[4]
        self.bandera=True

        self.string1="UPDATE historial SET historialPuntos = "+str(self.puntajeActual)+", mejorPuntaje="+str(self.mejorPuntaje)+" WHERE id="+str(self.id)+";"
        self.string2="UPDATE historial SET historialPuntos = "+str(self.puntajeActual)+", mejorPuntaje="+str(self.puntajeActual)+" WHERE id="+str(self.id)+";"

        if self.puntajeActual<self.mejorPuntaje and self.bandera:
            self.acceso.ejecutarAccion(self.string1)
            self.bandera=False
            
        elif self.puntajeActual>self.mejorPuntaje and self.bandera:
            self.acceso.ejecutarAccion(self.string2)
            self.bandera=False

    def dibujarGO(self, pantalla, vida ):
        
        if vida<200:
            self.fondo=pygame.image.load("img/Gameover.png")
            pantalla.blit(self.fondo, [0, 0])
        if vida>=200:
            pantalla.blit(self.render1,[180 , 700])

        
