import pygame
pygame.init()

class Mapa:
    def __init__(self):
        self.modo= None
        self.fondo= None

    def setearMapa(self,modo):
        self.modo=modo
        if self.modo== True:
            self.fondo=pygame.image.load("img/dia.png")
        else:
            self.fondo=pygame.image.load("img/noche.png")

    def dibujarMapa(self, pantalla):
        pantalla.blit(self.fondo, [0, 0])
