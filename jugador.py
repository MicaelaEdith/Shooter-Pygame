import pygame
from accesoDatos import AccesoDatos


class Jugador():
    def __init__(self):
        self.accesoDatos=AccesoDatos()
        self.posX=340
        self.posY=625
        self.banderaVida=True
        self.puntos=0
        self.nivel=1
        self.bala=pygame.image.load("img/bala.png")
        self.bala.set_colorkey([255,255,255])
        self.coordYBala=635
        self.BanderaBala=True
        self.BanderaImpacto=True
        self.inicial=True
        self.coordXBalaInicial=self.posX
        self.disparo=False

    def setearJugador(self,nombre,seleccion):
        self.nombre=nombre 
        self.seleccion=seleccion
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

        if self.BanderaBala==False:
            self.coordYBala=635
            self.coordXBalaInicial=self.posX+48
            self.BanderaBala=True
            self.BanderaImpacto=True
        
        if self.coordYBala<-1:
            self.BanderaBala=False
    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.posX > 10:
                self.posX+=-self.velocidadMovimiento
            if event.key == pygame.K_RIGHT and self.posX < 662:
                self.posX+=self.velocidadMovimiento


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.disparo=True
                self.coordXBalaInicial=self.posX+48

            
           # if event.key == pygame.K_LEFT:
            #    self.posX+=0
            #if event.key == pygame.K_RIGHT:
             #   self.posX+=0


        if self.disparo:
            if self.coordYBala>-1 and self.BanderaBala==True:
                self.coordYBala-=self.velocidadDisparo
                pantalla.blit(self.bala, (self.coordXBalaInicial, self.coordYBala)) 
            else:
                self.BanderaBala=False

            if self.coordYBala<0:
                self.disparo=False

class Bala():
    def __init__(self):
        self.bala=pygame.image.load("img/bala.png")
        self.bala.set_colorkey([255,255,255])
        self.coordYBala=635
        self.BanderaBala=True
        self.BanderaImpacto=True
        self.inicial=True
        

    def dibujarBala(self, pantalla, coordX, coordY):
        if self.inicial:
            self.coordXBalaInicial=self.coordX+45
            self.inicial=False

        if self.coordYBala>-1 and self.BanderaBala==True:
            self.coordYBala-=self.velocidadDisparo
            
        else:
            self.BanderaBala=False

        if event.key == pygame.K_LEFT:
            self.posX+=0
        if event.key == pygame.K_RIGHT:
            self.posX+=0

        if self.BanderaBala==False:
            self.coordYBala=635
            self.BanderaBala=True
            self.BanderaImpacto=True
            self.inicial=True
        
        pantalla.blit(self.bala, (self.coordXBalaInicial, self.coordYBala)) 
    