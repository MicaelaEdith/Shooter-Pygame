import pygame, random
      
class Misil1():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-50
        self.cuadro=0
        self.misil1=[]
        self.misil1.append(pygame.image.load('img/misilA1.png'))
        self.misil1.append(pygame.image.load('img/misilA2.png'))
        self.direct=6

    def dibujarMisil(self, pantalla):
        if self.coordY<850:

            if self.coordX >750:
                self.direct=-6
            if self.coordX < 50:
                self.direct=6

            if self.coordY%2==0:
                self.coordY+=6.5
                self.cuadro=1
                self.coordX+=self.direct
            else:
                self.coordY+=6.5
                self.cuadro=0
                self.coordX+=self.direct

        else:
            self.coordY=-50
            self.coordX=random.randrange(750)
    

        pantalla.blit(self.misil1[self.cuadro], (self.coordX, self.coordY))

class Misil2():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-220
        self.cuadro=0
        self.misil2=[]
        self.misil2.append(pygame.image.load('img/misilB1.png'))
        self.misil2.append(pygame.image.load('img/misilB2.png'))
        self.direct=6


    def dibujarMisil(self, pantalla):

        if self.coordY<850:

            if self.coordX >750:
                self.direct=-6
            if self.coordX < 50:
                self.direct=6

            if self.coordY%2==0:
                self.coordY+=5.5
                self.cuadro=1
                self.coordX+=self.direct
             
            else:
                self.coordY+=5.5
                self.cuadro=0
                self.coordX+=self.direct
        else:
            self.coordY=-220
            self.coordX=random.randrange(750)
                

        pantalla.blit(self.misil2[self.cuadro], (self.coordX, self.coordY))

class Nubes():
    def __init__(self):
        self.listaNubes=[]
        self.listaNubes.append(pygame.image.load('img/nube1.png'))
        self.listaNubes.append(pygame.image.load('img/nube2.png'))
        self.listaNubes.append(pygame.image.load('img/nube3.png'))
        self.coordX1=random.randrange(700)
        self.coordY1=-70
        self.coordX2=random.randrange(700)
        self.coordY2=-320
        self.coordX3=random.randrange(700)
        self.coordY3=-500
    
    def dibujarNubes(self, pantalla):
                
        if self.coordY1<850:
            pantalla.blit(self.listaNubes[2], (self.coordX1, self.coordY1))
            self.coordY1+=1.3
        else:
            self.coordY1=-70
        if self.coordY2<850:
            pantalla.blit(self.listaNubes[1], (self.coordX2, self.coordY2))
            self.coordY2+=1.3
        else:
            self.coordY2=-320
        if self.coordY3 <850:
            pantalla.blit(self.listaNubes[0], (self.coordX3, self.coordY3))      
            self.coordY3+=1.3
        else:
            self.coordY3=-500

class Estrella():
    def __init__(self):
        self.estrella=pygame.image.load('img/estrella.png')

class Vida():
    def __init__(self):
        self.vida=pygame.image.load('img/vida.png')

class ColisionRoja():
    def __init__(self):
        self.cuadro=0
        self.colision=[]
        self.colision.append(pygame.image.load('img/Explosion1.png').set_colorkey([255,255,255]))
        self.colision.append(pygame.image.load('img/Explosion2.png').set_colorkey([255,255,255]))
        self.colision.append(pygame.image.load('img/Explosion3.png').set_colorkey([255,255,255]))

    def explotarRojo(self):
        pass


