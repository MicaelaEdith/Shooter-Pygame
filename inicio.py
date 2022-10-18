import pygame

class Inicio():
    def dibujar(self, pantalla, text):
        self.fondo=pygame.image.load("img/noche.png")
        self.fuente=pygame.font.SysFont("Courier", 30, bold= True)
        self.superficie=self.fuente.render(text,True,(255,255,255))
        pantalla.blit(self.fondo, [0, 0])
        

        ##################--Definir: seleccion de acciones para ingresar, modificar, listar y eliminar jugadores.
        ### Definir selección de avion

