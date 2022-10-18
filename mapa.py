import pygame

from jugador import Jugador
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

    def marcador(self, pantalla,nivel, puntos):
        self.color= (0 ,0 ,0)
        self.colorFondo=(255,255,255)
        self.string="Puntaje : " + str(puntos)
        self.nivel="Nivel: "+str(nivel)
        self.fuente=pygame.font.SysFont("Courier", 20, bold= True)
        self.superficie=self.fuente.render(str(self.string),True,self.color, self.colorFondo)
        self.superficieN=self.fuente.render(str(self.nivel),True,self.color, self.colorFondo)
        pantalla.blit(self.superficie, [20, 20])
        pantalla.blit(self.superficieN, [20, 40])

    def nivelJugador(self, pantalla, jugador):
        self.color= (0 ,0 ,0)
        self.colorFondo=(255,255,255)
        self.fuente=pygame.font.SysFont("Courier", 20, bold= True)
        self.superficie=self.fuente.render(str(jugador),True,self.color, self.colorFondo)
        self.vida=pygame.image.load('vida.png')
        self.vida.set_colorkey([255,255,255])
        pantalla.blit(self.vida, [690, 20])
        pantalla.blit(self.superficie, [620, 20])
        
