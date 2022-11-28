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

    def marcador(self, pantalla,nivel, puntos):
        self.color= (0 ,0 ,0)
        self.colorFondo=(255,255,255)
        self.string="Puntaje : " + str(puntos)
        self.seteoNivel=nivel

        if nivel==2.5:
            self.seteoNivel=2
        else:
            self.seteoNivel=nivel

        self.nivel="Nivel: "+str(self.seteoNivel)
        self.fuente=pygame.font.SysFont("Courier", 20, bold= True)
        self.superficie=self.fuente.render(str(self.string),True,self.color, self.colorFondo)
        self.superficieN=self.fuente.render(str(self.nivel),True,self.color, self.colorFondo)
        pantalla.blit(self.superficie, [20, 20])
        pantalla.blit(self.superficieN, [20, 40])

    def estadoJugador(self, pantalla, jugador, vida):
        self.color= (0 ,0 ,0)
        self.colorFondo=(255,255,255)
        self.fuente=pygame.font.SysFont("Courier", 20, bold= True)
        self.superficie=self.fuente.render(str(jugador),True,self.color, self.colorFondo)
        self.vida=pygame.image.load('img/vida.png')
        self.vida.set_colorkey([255,255,255])
        
        self.auxNombre=int(len(jugador))
        self.posNombre=740-(self.auxNombre*8)


        pantalla.blit(self.superficie, [self.posNombre, 20])
        
        if vida==1000:
            pantalla.blit(self.vida, [730, 50])
        if vida>800:
            pantalla.blit(self.vida, [690, 50])
        if vida>600:
            pantalla.blit(self.vida, [650, 50])
        if vida>400:
            pantalla.blit(self.vida, [610, 50])
        if vida>200:
            pantalla.blit(self.vida, [570, 50])
        
