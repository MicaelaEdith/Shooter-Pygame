import pygame

class Jugador():
    def __init__(self):
        self.image=pygame.image.load("img/Jugador.png").convert()
        self.image.set_colorkey([16,25,57])
        self.posX=340
        self.posY=625
        self.vida=5
        self.puntos=0
        self.nivel=1
        self.bala=pygame.image.load("img/bala.png")
        self.bala.set_colorkey([255,255,255])
        self.coordYBala=635
        self.BanderaBala=True
      
    def dibujarJugador(self, pantalla):
        pantalla.blit(self.image, [self.posX, self.posY])

    def moverJugador(self, event, pantalla):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.posX > 10:
                self.posX+=-5
            if event.key == pygame.K_RIGHT and self.posX < 662:
                self.posX+=5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if self.coordYBala>-1 and self.BanderaBala==True:
                    self.coordYBala-=20
                    pantalla.blit(self.bala, (self.posX+48, self.coordYBala)) 
                else:
                    self.BanderaBala=False
            if event.key == pygame.K_LEFT:
                self.posX+=0
            if event.key == pygame.K_RIGHT:
                self.posX+=0
    
    def definirNivel(self, nivel):
        self.nivel=nivel
    

