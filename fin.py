import pygame
from accesoDatos import AccesoDatos

class Finalizado():
    def __init__(self,nombre):
        self.acceso=AccesoDatos()
        self.historial=self.acceso.finalJuego('chinit')
    
    def dibujarGO(self, pantalla):
        self.fondo=pygame.image.load("img/Gameover.png")
    
        pantalla.blit(self.fondo, [0, 0])

