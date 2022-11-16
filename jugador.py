import pygame
from accesoDatos import AccesoDatos


class Jugador():
    def __init__(self):
        self.accesoDatos=AccesoDatos()
        self.posX=340
        self.posY=625
        self.banderaVida=True
        self.puntos=90
        self.nivel=1
        self.bala=pygame.image.load("img/bala.png")
        self.bala.set_colorkey([255,255,255])
        self.coordYBala=635
        self.BanderaBala=True
        self.BanderaImpacto=True

    def setearJugador(self,nombre,seleccion):
        self.nombre=nombre
        self.seleccion=int(seleccion)
        self.caracteristicas=self.accesoDatos.buscarAvion(seleccion)
        self.velocidadMovimiento=self.caracteristicas[2]
        self.velocidadDisparo=self.caracteristicas[3]
        self.potenciaDisparo=self.caracteristicas[4]
        self.vida=self.caracteristicas[5]
        if self.seleccion==1:
            self.image=pygame.image.load("img/Pampa.png").convert()
        if self.seleccion==2:
            self.image=pygame.image.load("img/Tango.png").convert()
        if self.seleccion==3:
            self.image=pygame.image.load("img/Puma.png").convert()

        self.image.set_colorkey([16,25,57])

    def dibujarJugador(self, pantalla):
        pantalla.blit(self.image, [self.posX, self.posY])

    def moverJugador(self, event, pantalla):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.posX > 10:
                self.posX+=-self.velocidadMovimiento
            if event.key == pygame.K_RIGHT and self.posX < 662:
                self.posX+=self.velocidadMovimiento
                                                                        ##############################################
                ######################################################################################################

        if event.type == pygame.KEYUP:         ###### -- K.UP porque con K.Down no dispara, o sí pero mantiene la coordenada en el mismo lugar
            if event.key == pygame.K_SPACE:             ################## -- Arreglo temporal con K.UP , volver después y solucionarlo!
                if self.coordYBala>-1 and self.BanderaBala==True:
                    self.coordYBala-=self.velocidadDisparo
                    pantalla.blit(self.bala, (self.posX+48, self.coordYBala)) 
                else:
                    self.BanderaBala=False
            if event.key == pygame.K_LEFT:
                self.posX+=0
            if event.key == pygame.K_RIGHT:
                self.posX+=0
    
    def definirNivel(self, nivel):
        self.nivel=nivel
    

