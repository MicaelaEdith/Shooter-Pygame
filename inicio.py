import pygame
from accesoDatos import AccesoDatos

class Inicio():

    def dibujar1(self, pantalla, event):
        self.fondo=pygame.image.load("img/Bienvenido.png")
        self.color=(255,255,255)
        self.seleccionAncho=160
        self.seleccionAlto=5
        self.seleccionX=200
        self.seleccionY=730

        pantalla.blit(self.fondo, [0, 0])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and self.seleccionX==200:
                self.seleccionX=440
            if event.key == pygame.K_LEFT and self.seleccionX==440:
                self.seleccionX=200

        self.seleccion= pygame.draw.rect(pantalla, self.color, (self.seleccionX, self.seleccionY, self.seleccionAncho, self.seleccionAlto))

    def dibujar2(self, pantalla):
        self.fondo=pygame.image.load("img/inicio.png")
        pantalla.blit(self.fondo, [0, 0])

    def dibujarRanking(self, pantalla):  #cargarJuego-ListarRanking

        self.fondo=pygame.image.load("img/noche.png")
        self.acceso=AccesoDatos()
        self.respuesta=self.acceso.listarRanking()
        self.fuente=pygame.font.SysFont("Courier", 30, bold=True)

################################### -- probar  !
        self.imagenTexto1= self.fuente.render(str(self.respuesta[0]), True, (200,200,200), (16,25,57) )
        self.imagenTexto2= self.fuente.render(str(self.respuesta[1]), True, (200,200,200), (16,25,57) )
        self.imagenTexto3= self.fuente.render(str(self.respuesta[2]), True, (200,200,200), (16,25,57) )
        self.imagenTexto4= self.fuente.render(str(self.respuesta[3]), True, (200,200,200), (16,25,57) )
        self.imagenTexto5= self.fuente.render(str(self.respuesta[4]), True, (200,200,200), (16,25,57) )


        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.imagenTexto1,(240,100))
        pantalla.blit(self.imagenTexto2,(240,200))
        pantalla.blit(self.imagenTexto3,(240,300))
        pantalla.blit(self.imagenTexto4,(240,400))
        pantalla.blit(self.imagenTexto5,(240,500))


    def guardar(self, accion, nombreJugador, seleccionado, id):
        self.agregar="insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('"+str(nombreJugador)+"',"+str(seleccionado)+",0,0);"
        self.modificar="UPDATE historial SET nombre = '"+str(nombreJugador)+"' WHERE id="+str(id)+";"
        self.eliminar="delete from historial where id="+str(id)+";"
        self.string=None
        if accion==1:
            self.string=self.agregar
        if accion==2:
            self.string=self.modificar
        if accion==3:
            self.string=self.eliminar
        acceso=AccesoDatos()
        acceso.ejecutarAccion(self.string)
        
###########################----  Prueba

#medidaPantalla = (800,750)
#pantalla = pygame.display.set_mode(medidaPantalla)
#inicio=True

#inicio=Inicio()
#inicio.dibujar(pantalla)

#pygame.display.flip()
