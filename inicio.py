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
        self.respuesta=str(self.acceso.listarRanking())
        self.fuente=pygame.font.SysFont("Courier", 30, bold=True)
        self.texto=' '
        self.bandera=True
        self.contador=1
        self.puesto1=''
        self.puesto2=''
        self.puesto3=''
        self.puesto4=''
        self.puesto5=''

        for i in self.respuesta:
            if not i =='[' and not i =='(' and not i ==',' and not i ==')' and not i ==']' and not i =="'":
                self.texto=self.texto + i
            elif i == ',' and self.bandera:
                self.texto=self.texto + ' - '
                self.bandera=False
            elif i == ')':
                self.texto = self.texto +'\n'
            elif i =='(':
                self.bandera=True
        
        for i in self.texto:
            if not i=='\n' and self.contador==1:
                self.puesto1+=i
            if not i=='\n' and self.contador==2:
                self.puesto2+=i
            if not i=='\n' and self.contador==3:
                self.puesto3+=i
            if not i=='\n' and self.contador==4:
                self.puesto4+=i
            if not i=='\n' and self.contador==5:
                self.puesto5+=i
            if i=='\n':
                self.contador+=1

        self.puesto1R= self.fuente.render(self.puesto1, True, (200,200,200), (16,25,57) )
        self.puesto2R= self.fuente.render(self.puesto2, True, (200,200,200), (16,25,57) )
        self.puesto3R= self.fuente.render(self.puesto3, True, (200,200,200), (16,25,57) )
        self.puesto4R= self.fuente.render(self.puesto4, True, (200,200,200), (16,25,57) )
        self.puesto5R= self.fuente.render(self.puesto5, True, (200,200,200), (16,25,57) )

        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.puesto1R,(240,100))
        pantalla.blit(self.puesto2R,(240,300))
        pantalla.blit(self.puesto3R,(240,200))
        pantalla.blit(self.puesto4R,(240,400))
        pantalla.blit(self.puesto5R,(240,500))
               



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
