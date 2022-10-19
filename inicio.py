import pygame
pygame.init()

class Inicio():
    def dibujar(self, pantalla):
        self.bandera=True
        self.fondo=pygame.image.load("img/Bienvenido.png").convert()
        self.enterCh=pygame.image.load("img/EnterCh.png").convert()
        self.enterGR=pygame.image.load("img/EnterGr.png").convert()
        self.cuadro=0
        self.enter=[]
        self.enter.append(pygame.image.load("img/EnterCh.png"))
        self.enter.append(pygame.image.load("img/EnterGr.png"))
        self.contador=0

        while self.bandera:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        self.bandera = False

            if self.cuadro==0:
                self.contador+=1
                if self.contador>20:
                    self.cuadro=1
            if self.cuadro==1:
                self.contador-=1
                if self.contador<1:
                    self.cuadro=0
        
            pantalla.blit(self.fondo, [0, 0])
            pantalla.blit(self.enter[self.cuadro], [4, 680])


        ##################--Definir: seleccion de acciones para ingresar, modificar, listar y eliminar jugadores.
        ### Definir selección de avion

#prueba


medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)

inicio=Inicio()
inicio.dibujar(pantalla)

pygame.display.flip()
