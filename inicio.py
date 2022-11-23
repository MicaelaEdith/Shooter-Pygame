import pygame
from accesoDatos import AccesoDatos

class Inicio():
    def __init__(self):
        self.acceso=AccesoDatos()
        self.texto=''
        self.validar1Ok=True
        self.validar2Ok=True

    def dibujar0(self, pantalla, event):      #InicioGeneral
        self.fondo=pygame.image.load("img/Bienvenido.png")
        self.color=(255,255,255)
        self.seleccionAncho=190
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

    def dibujar1(self, pantalla, texto, posX, posY, validacion):           #InicioJugadorNuevo
        self.texto=texto
        self.validacion="- Ingrese un nombre para continuar -"
        self.color=(255,255,255)
        self.seleccionAncho=120
        self.seleccionAlto=5
        self.seleccionX=150
        self.seleccionY=380
        self.fondo=pygame.image.load("img/inicio.png")
        self.fuente=pygame.font.SysFont("Courier", 45, bold=True)
        self.fuenteChica=pygame.font.SysFont("Courier", 25, bold=True)
        self.renderNombre= self.fuente.render(self.texto, True, (200,200,200), (16,25,57) )
        self.renderValidacion= self.fuenteChica.render(self.validacion, True, (200,200,200), (16,25,57) )


        if posX ==1:
            self.seleccionX=115
        if posX ==2:
            self.seleccionX=347
        if posX ==3:
            self.seleccionX=575
        if posY ==1:
            self.seleccionY=380
        if posY ==2:
            self.seleccionY=90
            self.seleccionX=65


        pantalla.blit(self.fondo, [0, 0])
        pantalla.blit(self.renderNombre,(250,200))

        
        self.textoVali='Nombre de usuario no disponible, ingrese otro'
        self.fuenteVali=pygame.font.SysFont("Courier", 20, bold=True)
        self.textoValiR= self.fuente.render(self.texto, True, (200,200,200), (16,25,57) )
        self.aux=self.acceso.buscarJugador(texto)
        self.aux1=self.aux[0]
        self.nombreValidar=self.aux1[0]
    
        if texto==self.nombreValidar:
            pantalla.blit(self.textoValiR,(130,360))

        if not validacion:
            pantalla.blit(self.renderValidacion,[150,100])

        self.seleccion= pygame.draw.rect(pantalla, self.color, (self.seleccionX, self.seleccionY, self.seleccionAncho, self.seleccionAlto))
        


    def dibujar2(self, pantalla, texto, posX, validacion, busqueda, posBusquedaY):           #InicioSeleccionJugador
        self.texto=texto
        self.textoVolver='volver'
        self.textoContinuar='continuar'
        self.avion=pygame.image.load("img/Puma.png")
        self.nube=pygame.image.load("img/nube1.png")
        self.fondo=pygame.image.load("img/noche.png")
        self.fuente=pygame.font.SysFont("Courier", 30, bold=True)
        self.fuente2=pygame.font.SysFont("Courier", 20, bold=True)
        self.validacion="- Ingrese el nombre de su piloto -"
        self.aviso1='Usuario inexistente'
        self.aviso2='regrese y seleccione juego nuevo'
        self.fuenteChica=pygame.font.SysFont("Courier", 25, bold=True)
        self.renderValidacion= self.fuenteChica.render(self.validacion, True, (200,200,200), (16,25,57) )
        self.textoVolverR=self.fuente2.render(self.textoVolver, True, (200,200,200), (16,25,57) )
        self.textoContinuarR=self.fuente2.render(self.textoContinuar, True, (200,200,200), (16,25,57) )
        self.renderAviso1= self.fuente2.render(self.aviso1, True, (200,200,200), (16,25,57) )
        self.renderAviso2= self.fuente2.render(self.aviso2, True, (200,200,200), (16,25,57) )
        self.color=(255,255,255)
        self.seleccionAncho=100
        self.seleccionAlto=5
        self.seleccionX=60
        self.seleccionY=680
        self.renderNombre= self.fuente.render(self.texto, True, (200,200,200), (16,25,57) )
        self.texto=' '
        self.puesto1=''
        self.puesto2=''
        self.puesto3=''
        self.aux=0
        self.aux1=''
        self.aux2=''
        self.aux3=''
        self.contAux=0
        self.contador=1
        self.seleccionBusquedaY=405
        self.seleccionBusquedaX=220
        self.avionOk=0
        self.nombreBusqueda=''
        self.nombreCarga=''
        self.imprimirAviso=False
        self.busquedaOK=False

        try:
            self.busqueda=str(self.acceso.buscarJugador(texto))
            self.aux=self.acceso.buscarJugador(texto)
            self.aux1=self.aux[posBusquedaY-1]
            self.nombreCarga=self.aux1[0]
            self.avionOk=self.aux1[1]

            if self.aux=='[]':
                self.busquedaOK=False
            else:
                self.busquedaOK=True
            

            for i in self.busqueda:
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
                    
                    if i==' ' and self.contAux==0:
                        self.aux1=self.puesto1
                        self.contAux=1

                    self.puesto1+=i

                if not i=='\n' and self.contador==2:

                    if i==' ' and self.contAux==1:
                        self.aux2=self.puesto2
                        self.contAux=2

                    self.puesto2+=i

                if not i=='\n' and self.contador==3:

                    if i==' ' and self.contAux==2:
                        self.aux3=self.puesto3
                        self.contAux=3

                    self.puesto3+=i


                if i=='\n':
                    self.contador+=1
                

            if posBusquedaY==1:
                self.nombreBusqueda=self.aux1

            if posBusquedaY==2:
                self.nombreBusqueda=self.aux2

            if posBusquedaY==3:
                self.nombreBusqueda=self.aux3

        except:
            self.imprimirAviso=True
            

        if posX==1:
            self.seleccionX=50
        if posX==2:
            self.seleccionX=650

        if posBusquedaY==1:
            self.seleccionBusquedaY=405
        if posBusquedaY==2 and not self.puesto2=='':
            self.seleccionBusquedaY=485
        if posBusquedaY==3 and not self.puesto3=='':
            self.seleccionBusquedaY=565

        pantalla.blit(self.fondo, [0, 0])
        pantalla.blit(self.renderNombre,(250,200))
        pantalla.blit(self.avion,(335,635))
        pantalla.blit(self.nube,(25,40))

        self.puesto1R= self.fuente.render(self.puesto1, True, (200,200,200), (16,25,57) )
        self.puesto2R= self.fuente.render(self.puesto2, True, (200,200,200), (16,25,57) )
        self.puesto3R= self.fuente.render(self.puesto3, True, (200,200,200), (16,25,57) )

        pantalla.blit(self.puesto1R,(240,400))
        pantalla.blit(self.puesto2R,(240,480))
        pantalla.blit(self.puesto3R,(240,560))
        pantalla.blit(self.textoContinuarR,(46,660))
        pantalla.blit(self.textoVolverR,(663,660))


        if not validacion:
            pantalla.blit(self.renderValidacion,[150,50])

        if self.imprimirAviso:
            pantalla.blit(self.renderAviso1,(265,350))
            pantalla.blit(self.renderAviso2,(200,380))
        
        self.seleccion= pygame.draw.rect(pantalla, self.color, (self.seleccionX, self.seleccionY, self.seleccionAncho, self.seleccionAlto))
        if busqueda:
            self.seleccionBusqueda= pygame.draw.rect(pantalla, self.color, (self.seleccionBusquedaX, self.seleccionBusquedaY, self.seleccionAncho-70, self.seleccionAlto+15))



    def dibujar3(self, pantalla):       #cargarJuego-ListarRanking

        self.avion=pygame.image.load("img/Tango.png")
        self.nube=pygame.image.load("img/nube2.png")
        self.fondo=pygame.image.load("img/noche.png")
        self.respuesta=str(self.acceso.listarRanking())
        self.fuente=pygame.font.SysFont("Courier", 30, bold=True)
        self.fuente1=pygame.font.SysFont("Courier", 30, bold=True, italic=True)
        self.fuente2=pygame.font.SysFont("Courier", 20, bold=True)
        self.enter='Presione Enter para continuar'
        self.ranking='Top 5 - Mejores Jugadores'
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
        self.rankingR= self.fuente1.render(self.ranking, True, (200,200,200), (16,25,57) )
        self.enterR= self.fuente2.render(self.enter, True, (200,200,200), (16,25,57) )

        pantalla.blit(self.fondo,(0,0))
        pantalla.blit(self.puesto1R,(240,270))
        pantalla.blit(self.puesto2R,(240,300))
        pantalla.blit(self.puesto3R,(240,330))
        pantalla.blit(self.puesto4R,(240,360))
        pantalla.blit(self.puesto5R,(240,390))
        pantalla.blit(self.rankingR,(180,200))
        pantalla.blit(self.enterR,(220,550))
        pantalla.blit(self.avion,(600,635))
        pantalla.blit(self.nube,(30,50))
               
    def guardar(self, accion, nombreJugador, seleccionado, id):
        self.agregar="insert into historial (nombre,id_avion,historialPuntos,mejorPuntaje) value ('"+str(nombreJugador)+"',"+str(seleccionado)+",0,0);"
        self.modificar="UPDATE historial SET nombre = '"+str(nombreJugador)+"' WHERE id="+str(id)+";"
        self.eliminar="delete from historial where id="+str(id)+";"
        self.string=None
        if accion=='1':
            self.string=self.agregar
        if accion=='2':
            self.string=self.modificar
        if accion=='3':
            self.string=self.eliminar

        self.acceso.ejecutarAccion(self.string)

    def validarUsuario(self, string, pantalla):
        self.acceso=AccesoDatos()
        self.contador=0
        self.texto='Nombre de usuario no disponible, ingrese otro'
        self.fuente=pygame.font.SysFont("Courier", 20, bold=True)
        self.textoR= self.fuente.render(self.texto, True, (200,200,200), (16,25,57) )
        self.validar=self.acceso.buscarJugador(string)
        self.validarString=str(self.acceso.buscarJugador(string))
        self.validar1=None
        self.validar2=None
        self.validacionOK=False
        self.validacion10=True
        self.char=0

        if self.validarString=='[]':
            self.validar1=None
            self.validar2=None
        else:
            self.validar1=self.validar[0]
            self.validar2=self.validar1[0]

        if not self.validacionOK:
            if string==self.validar2:
                self.validar2=None
                
            else:
                self.validacionOK=True
                return True
    
    def dibujarValidacion(self,pantalla):
        pass

    def __del__(self):
        self.acceso.conexion.close()
