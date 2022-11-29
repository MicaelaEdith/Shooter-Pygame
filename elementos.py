import pygame, random

class Avion1():
    def __init__(self):
        self.coordX=random.randrange(10,220)
        self.coordY=-50
        #self.cuadro=0
        self.imagen=pygame.image.load("img/Enemigo1.png")
        self.direct=4
        self.imagenBala=pygame.image.load("img/bala.png")
        self.imagenBala.set_colorkey([255,255,255])
        self.banderaDireccion=True
        self.coordXinicial=0
        self.coordYinicial=0
        self.inicioBala=True


    def dibujarAvion(self, pantalla,velX,velY):
        if self.banderaDireccion:
            if self.coordY<850:
                self.coordX+=velX
                self.coordY+=velY

            else:
                self.coordY=-30
                self.banderaDireccion=False
                self.coordX=random.randrange(375,700)

            pantalla.blit(self.imagen, (self.coordX, self.coordY))
        
        else:
            if self.coordY<850:
                self.coordX-=velX
                self.coordY+=velY

            else:
                self.coordY=-30
                self.banderaDireccion=True
                self.coordX=random.randrange(0,300)


        if self.coordX>850:

            if self.banderaDireccion:
                self.banderaDireccion=False
            else:
                self.banderaDireccion=True

            
        pantalla.blit(self.imagen, (self.coordX, self.coordY))

    def dibujarBala(self, pantalla, coordX, coordY): 

        if self.inicioBala:
            self.inicioBala=False
            self.coordXinicial=coordX+50         
            self.coordYinicial=coordY+30
            
        if not self.inicioBala:
            self.coordYinicial+=15

        if self.coordYinicial>850:
            self.inicioBala=True
        
        pantalla.blit(self.imagenBala, (self.coordXinicial, self.coordYinicial))

        

class Avion2():
    def __init__(self):
        self.coordX=random.randrange(500,780)
        self.coordY=-250
        self.cuadro=0
        self.imagen=pygame.image.load("img/Enemigo2.png")
        self.direct=-2
        self.imagenBala=pygame.image.load("img/bala.png")
        self.imagenBala.set_colorkey([255,255,255])
        self.coordXinicial=0
        self.coordYinicial=0
        self.inicioBala=True
        self.banderaDireccion=False

    def dibujarAvion(self, pantalla,velX,velY):
        if self.banderaDireccion:
            if self.coordY<850:
                self.coordX+=velX
                self.coordY+=velY

            else:
                self.coordY=-250
                self.banderaDireccion=False
                self.coordX=random.randrange(375,700)

            pantalla.blit(self.imagen, (self.coordX, self.coordY))
        
        else:
            if self.coordY<850:
                self.coordX-=velX
                self.coordY+=velY

            else:
                self.coordY=-250
                self.banderaDireccion=True
                self.coordX=random.randrange(0,300)


        if self.coordX>850:

            if self.banderaDireccion:
                self.banderaDireccion=False
            else:
                self.banderaDireccion=True

            
        pantalla.blit(self.imagen, (self.coordX, self.coordY))

    def dibujarBala(self, pantalla, coordX, coordY):

        if self.inicioBala:
            self.inicioBala=False
            self.coordYinicial=coordY+30
            self.coordXinicial=coordX+50  

        if not self.inicioBala:
            self.coordYinicial+=18

        if self.coordYinicial>850:
            self.inicioBala=True
            
        pantalla.blit(self.imagenBala, (self.coordXinicial, self.coordYinicial))

        
class Misil1():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-220
        self.cuadro=0
        self.misil1=[]
        self.misil1.append(pygame.image.load("img/misilA1.png"))
        self.misil1.append(pygame.image.load("img/misilA2.png"))
        self.direct=6
        self.puntaX=self.coordX+23
        self.puntaY=self.coordY+185
        self.contador=0

    def dibujarMisil(self, pantalla):
        if self.coordY<850 and self.contador<5:

            if self.coordX >750:
                self.direct=-6
            if self.coordX < 50:
                self.direct=6

            if self.coordY%2==0:
                self.coordY+=6.5
                self.cuadro=0
                self.coordX+=self.direct
            else:
                self.coordY+=6.5
                self.cuadro=1
                self.coordX+=self.direct

        else:
            self.coordY=-220
            self.coordX=random.randrange(750)
            self.contador+=1
        pantalla.blit(self.misil1[self.cuadro], (self.coordX, self.coordY))

    def __del__(self):
        pass

class Misil2():
    def __init__(self):
        self.coordX=random.randrange(750)
        self.coordY=-220
        self.cuadro=0
        self.misil2=[]
        self.misil2.append(pygame.image.load('img/misilB1.png'))
        self.misil2.append(pygame.image.load('img/misilB2.png'))
        self.direct=6
        self.contador=0


    def dibujarMisil(self, pantalla):

        if self.coordY<850 and self.contador<5:

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
            self.contador+=1              

        pantalla.blit(self.misil2[self.cuadro], (self.coordX, self.coordY))

    def __del__(self):
        pass

class Ovni():
    def __init__(self):
        self.coordX=10
        self.coordY=100
        self.cuadro=0
        self.imagen=pygame.image.load("img/Ovni.png")
        self.direct=4
        self.imagenBala=pygame.image.load("img/DisparoOvni.png")
        self.imagenBala.set_colorkey([255,255,255])
        self.banderaDireccionX=True
        self.banderaDireccionY=True
        self.coordYBala1=self.coordY+40
        self.coordYBala2=self.coordY
        self.coordYBala3=self.coordY
        self.coordXBala1=random.randrange(120,450)
        self.coordXBala2=random.randrange(460,700)
        self.coordXBala3=random.randrange(460,700)
        self.inicioBala1=False
        self.inicioBala2=False
        self.inicioBala3=False
        self.coordYinicial1=self.coordY+70
        self.coordXinicial1=self.coordX+110  
        self.coordYinicial2=self.coordY+70
        self.coordXinicial2=self.coordX+110  
        self.coordYinicial3=self.coordY+70
        self.coordXinicial3=self.coordX+110  
        self.contadorBalas=0

    def dibujarOvni(self, pantalla):
        if self.contadorBalas<=31:
            if self.banderaDireccionX:
                self.coordX+=6
                if self.coordX>600:
                    self.banderaDireccionX=False
            else:
                self.coordX-=6
                if self.coordX<-40:
                    self.banderaDireccionX=True

            if self.banderaDireccionY:
                self.coordY+=3.5
                if self.coordY>130:
                    self.banderaDireccionY=False
            else:
                self.coordY-=3.5
                if self.coordY<-25:
                    self.banderaDireccionY=True

            if self.inicioBala1:
                self.inicioBala1=False
                self.coordYinicial1=self.coordY+70
                self.coordXinicial1=self.coordX+110
                self.coordYBala1=self.coordYinicial1
        else:
            self.coordY-=2.5
            self.coordX+=3

    
        if not self.inicioBala1:
            self.coordYBala1+=12
            pantalla.blit(self.imagenBala, (self.coordXinicial1, self.coordYBala1))

        if self.coordYBala1>845 and self.contadorBalas<30:
            self.coordYBala1=self.coordY
            self.inicioBala1=True
            self.contadorBalas+=1

        if self.inicioBala2:
            self.inicioBala2=False
            self.coordYinicial2=self.coordY+70
            self.coordXinicial2=self.coordX+110
            self.coordYBala2=self.coordYinicial2
    
        if not self.inicioBala2:
            self.coordYBala2+=12
            pantalla.blit(self.imagenBala, (self.coordXinicial2, self.coordYBala2))

        if self.coordYBala2>990 and self.contadorBalas<32:
            self.coordYBala2=self.coordY
            self.inicioBala2=True
            self.contadorBalas+=1


        if self.inicioBala3:
            self.inicioBala3=False
            self.coordYinicial3=self.coordY+70
            self.coordXinicial3=self.coordX+110
            self.coordYBala3=self.coordYinicial3
    
        if not self.inicioBala3:
            self.coordYBala3+=10
            pantalla.blit(self.imagenBala, (self.coordXinicial3, self.coordYBala3))

        if self.coordYBala3>1200 and self.contadorBalas<31:
            self.coordYBala3=self.coordY
            self.inicioBala3=True
            self.contadorBalas+=1



        pantalla.blit(self.imagen, (self.coordX, self.coordY))



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
        self.estrella.set_colorkey([255,255,255])
        self.rect=self.estrella.get_rect()
        self.coordY=-50
        self.coordX=random.randrange(350)
    
    def caer(self, pantalla):
        self.coordY+=4
        self.coordX+=1
        if self.coordX>700 and self.coordY<10:
            self.coordX=80
        pantalla.blit(self.estrella, (self.coordX, self.coordY))


class ColisionAviones():
    def __init__(self):
        self.Y=570
        self.cuadro=0
        self.listaImg=[]
        self.Img0=pygame.image.load('img/ExplosionOvniGr.png')
        self.Img0.set_colorkey([255,255,255])
        self.Img1=pygame.image.load('img/ExplosionOvniCh2.png')
        self.Img1.set_colorkey([255,255,255])
        self.Img2=pygame.image.load('img/ExplosionOvniCh3.png')
        self.Img2.set_colorkey([255,255,255])
        self.listaImg.append(self.Img0)
        self.listaImg.append(self.Img1)
        self.listaImg.append(self.Img2)
        self.contador=0
        self.banderaJugador=True

    def explotar(self, pantalla, coordX):    
        if self.contador<10 and self.banderaJugador:
            self.contador+=1
            if self.contador==9:
                self.cuadro=1
        elif self.contador>=10 and self.contador<20:
            self.banderaJugador=False
            self.contador+=1
            if self.contador==19:
                self.cuadro=2
        elif self.contador>=20:
            self.contador+=1
            if self.contador==30:
                self.cuadro=0
                self.contador=0
                self.banderaJugador=True
        pantalla.blit(self.listaImg[self.cuadro], (coordX, self.Y))

    def explotarE(self, pantalla, coordX,coordY):    
        if self.contador<10 and self.banderaJugador:
            self.contador+=1
            if self.contador==9:
                self.cuadro=1
        elif self.contador>=10 and self.contador<20:
            self.banderaJugador=False
            self.contador+=1
            if self.contador==19:
                self.cuadro=2
        elif self.contador>=20:
            self.contador+=1
            if self.contador==30:
                self.cuadro=0
                self.contador=0
                self.banderaJugador=True
        pantalla.blit(self.listaImg[self.cuadro], (coordX, coordY))


class Nivel():
    def __init__(self):
        self.imagen=pygame.image.load('img/nivel.png')
        self.coordX=180
        self.coordY=820
    
    def dibujar(self, pantalla):
        if self.coordY>-100:
            self.coordY-=15
        pantalla.blit(self.imagen, (self.coordX, self.coordY))

class Copa():
    def __init__(self, texto):
        self.imagen=pygame.image.load('img/ganador.png')
        self.imagen.set_colorkey([255,255,255])
        self.coordX=180
        self.coordY=820
        self.texto1=f'¡Felicidades {texto}!'
        self.texto2='¡Ganaste el Juego!'
        self.texto3='Presiona ENTER para volver a Jugar'
        self.fuente=pygame.font.SysFont("Courier", 35, bold=True)
        self.fuente2=pygame.font.SysFont("Courier", 20, bold=True)
        self.render1= self.fuente.render(self.texto1, True, (10,10,10), (140,203,221) )
        self.render2= self.fuente.render(self.texto2, True, (10,10,10), (140,203,221) )
        self.render3= self.fuente2.render(self.texto3, True, (10,10,10), (140,203,221) )
    
    def dibujar(self, pantalla):
        if self.coordY>290:
            self.coordY-=15
        pantalla.blit(self.imagen, (self.coordX+50, self.coordY-60))
        pantalla.blit(self.render1,(self.coordX-15, self.coordY-150))
        pantalla.blit(self.render2,(self.coordX, self.coordY+270))
        pantalla.blit(self.render3,(self.coordX+15, self.coordY-170))
 
