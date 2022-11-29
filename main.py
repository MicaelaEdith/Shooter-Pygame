import pygame, random
import string
from inicio import Inicio
from fin import Finalizado
from mapa import Mapa
from jugador import Jugador
from elementos import Avion1, Avion2, Misil1, Misil2, Nubes, Estrella, ColisionAviones, Ovni, Nivel, Copa
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()
inicioContador=0
inicioBandera=False
vidaJugador = True
texto=''
posX=1
posY=1
posBusquedaY=1
avionSeleccionado=0
validacionNombre=False
busqueda=False
dia= True
colisiones=0
avionesN3=0
mapa= Mapa()
mapa.setearMapa(dia)
nivelMarcador=1
jugador=Jugador()
inicio=Inicio()
misil1=Misil1()
misil2=Misil2()
jugadorIdHistorial=None
validarEliminar1=False
validarEliminar2=False
nubes=Nubes()
colision=ColisionAviones()
estrella=Estrella()
avion1= Avion1()
avion2=Avion2()
ovni=Ovni()
nivel=Nivel()
plusVida=True
seteo=True



while vidaJugador:
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    inicio1=False

        if jugador.BanderaBala==False:
            jugador.coordYBala=635
            jugador.BanderaBala=True
            jugador.BanderaImpacto=True


    if inicioContador==0:
        validarEliminar1=False
        validarEliminar2=False
        texto=''
        
        inicio.usuarioOriginalNombre=None
        inicio.dibujar0(pantalla,event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if inicio.seleccionX==440:
                        inicioContador+=2
                        posX=1
                        posY=1
                    elif inicio.seleccionX==200:
                        inicioContador+=1

    elif inicioContador==1:
        inicio.dibujar1(pantalla, texto, posX, posY, validacionNombre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if validacionNombre and inicio.validarUsuario(texto) and not posY==2:
                        inicioContador+=2
                        inicio.guardar('1', texto, posX)
                  
                    if posY==2:
                        inicioContador=0
                        texto=''
                
                if event.key == pygame.K_LEFT:
                    if posX==2 or posX==3:
                        posX-=1
                if event.key == pygame.K_RIGHT:
                    if posX ==1 or posX==2:
                        posX+=1
                if event.key == pygame.K_UP:
                    if posY==1:
                        posY=2
                if event.key == pygame.K_DOWN:
                    if posY==2:
                        posY=1

                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif not event.key==pygame.K_RETURN and len(texto)<12:
                    texto += event.unicode      
              
            if not texto=='':
                validacionNombre=True
            if texto=='':
                validacionNombre=False
        avionSeleccionado=posX
            
    elif inicioContador==2:
        inicio.dibujar2(pantalla, texto, posX, validacionNombre, busqueda, posBusquedaY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if posX==2:
                        texto=''
                        inicioContador-=2
                    else:
                        if not busqueda:
                            if inicio.validarUsuario(validacionNombre):
                                busqueda=True

                        elif busqueda and inicio.busqueda:
                            inicioContador+=0.5
                            texto=inicio.nombreCarga            
                            avionSeleccionado=inicio.avionOk
                            posX=avionSeleccionado
                            inicio.cargaNombreOriginal=False
                            busqueda=False
                            posBusquedaY=1
                        

                if event.key == pygame.K_LEFT:
                    if posX==2:
                        posX=1
                if event.key == pygame.K_RIGHT:
                    if posX ==1:
                        posX=2
                if event.key == pygame.K_UP:
                    if posBusquedaY==2 or posBusquedaY==3:
                        posBusquedaY-=1
                if event.key == pygame.K_DOWN:
                    if posBusquedaY==1 or posBusquedaY==2:
                        posBusquedaY+=1

                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif not event.key==pygame.K_RETURN and len(texto)<12 and len(texto)>=0:
                    texto += event.unicode   
                
            
            if not texto=='':
                validacionNombre=True
            if texto=='':
                validacionNombre=False
    
    elif inicioContador==2.5:
        inicio.dibujar2B(pantalla, texto, posX, posY, validacionNombre, validarEliminar1, validarEliminar2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if posY==1:
                        if (validacionNombre  and inicio.validarUsuario(texto)) or texto==inicio.usuarioOriginalNombre:
                            inicioContador+=0.5
                            inicio.guardar('2', texto, posX)
                    
                    if posY==2:                     
                        inicioContador=0
                        texto=''
                        inicio.cargaNombreOriginal=False
                        validarEliminar1=False
                        validarEliminar2=False

                    if posY==3:
                        if not validarEliminar1:
                            validarEliminar1=True
                            break

                        if not validarEliminar2 and validarEliminar1:
                            texto=''
                            validarEliminar1=False
                            validarEliminar2=True
                            inicio.guardar('3', texto, posX)
                            posY=2
                            inicioContador=0
                            validarEliminar2=False
                            break


                if event.key == pygame.K_LEFT:
                    if posY==1:
                        if posX==2 or posX==3:
                            posX-=1
                    if posY==3:
                        posY=2
                    
                if event.key == pygame.K_RIGHT:
                    if posY==1:
                        if posX ==1 or posX==2:
                            posX+=1

                    if posY==2:
                        posY=3
                if event.key == pygame.K_UP:
                    if posY==1:
                        posY=2
                if event.key == pygame.K_DOWN:
                    if posY==2 or posY==3:
                        posY=1

                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif not event.key==pygame.K_RETURN and len(texto)<12:
                    texto += event.unicode      
              
            if not texto=='':
                validacionNombre=True
            if texto=='':
                validacionNombre=False
        avionSeleccionado=posX
            
    elif inicioContador==3:
        inicio.dibujar3(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicioContador+=1
                    inicioBandera = True
                
    elif inicioContador==4: 
        mapa.dibujarMapa(pantalla)
        nubes.dibujarNubes(pantalla)
        mapa.marcador(pantalla, nivelMarcador, jugador.puntos)

        if inicioBandera:
            jugador.setearJugador(texto,avionSeleccionado)
            del inicio
            inicioBandera=False
            copa=Copa(texto)
            dia=True
            
        
        mapa.estadoJugador(pantalla, jugador.nombre, jugador.vida)
        jugador.moverJugador(event, pantalla)
        jugador.dibujarJugador(pantalla)
        rectJ=jugador.image.get_rect(x=jugador.posX, y=jugador.posY)
        rectJB=jugador.bala.get_rect(x=jugador.posX+48, y=jugador.coordYBala)
        plusVida=True
        

        if nivelMarcador==1:                       #################################################---NIVEL1---
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            rectBala=avion1.imagenBala.get_rect(x=avion1.coordXinicial, y=avion1.coordYinicial)
            nivelMarcador=1
            avion1.dibujarAvion(pantalla,3,8)
            avion1.dibujarBala(pantalla, avion1.coordX, avion1.coordY)


            if rectJ.colliderect(rectA1): 
                colision.explotar
                (pantalla, jugador.posX-20)
                jugador.vida-=5
            
            if rectJ.colliderect(rectBala): 
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=2.5
                avion1.coordYinicial=840

            
            if rectJB.colliderect(rectA1) and jugador.BanderaImpacto:
                colision.explotarE(pantalla, avion1.coordX, avion1.coordY)
                jugador.coordYBala=635
                jugador.puntos+=10
                jugador.BanderaImpacto=False


        if jugador.puntos==80:
            nivel.dibujar(pantalla)
            if nivel.coordY<5:
                nivelMarcador=2


        if nivelMarcador==2:                                                        ############################################---NIVEL2---
            rectM1=misil1.misil1[0].get_rect(x=misil1.coordX, y=misil1.coordY)
            rectM2=misil2.misil2[0].get_rect(x=misil2.coordX, y=misil2.coordY)

            if misil1.contador<6:
                misil1.dibujarMisil(pantalla)

            if misil2.contador<5:
                misil2.dibujarMisil(pantalla)
            else:
                jugador.puntos=150
                nivel.coordY=820
                dibujarOK=True

            if rectJ.colliderect(rectM1) or rectJ.colliderect(rectM2):
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=10
    
            if jugador.puntos==150:
                nivelMarcador=2.5


        if nivelMarcador==2.5:
            nivel.dibujar(pantalla)
            if nivel.coordY<5:
                nivelMarcador=3
                del misil1
                del misil2


        if nivelMarcador==3:   ############################################---NIVEL3---
            dia=False
            if seteo:
                mapa.setearMapa(dia)
                seteo=False
            
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            rectA2=avion2.imagen.get_rect(x=avion2.coordX, y=avion2.coordY)
            rectBala1=avion1.imagenBala.get_rect(x=avion1.coordXinicial, y=avion1.coordYinicial)
            rectBala2=avion1.imagenBala.get_rect(x=avion2.coordXinicial, y=avion2.coordYinicial)

            avion1.dibujarBala(pantalla, avion1.coordX, avion1.coordY)
            avion1.dibujarAvion(pantalla,3,8)
            avion2.dibujarBala(pantalla, avion2.coordX, avion2.coordY)
            avion2.dibujarAvion(pantalla, 3,8)

            if rectJ.colliderect(rectA1) or rectJ.colliderect(rectA2):
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=12

            if rectJ.colliderect(rectBala1) or rectJ.colliderect(rectBala2):
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=5
                avion1.coordYinicial=840

            if rectJB.colliderect(rectA1):
                colision.explotarE(pantalla, avion1.coordX, avion1.coordY)
                jugador.puntos+=1
                jugador.BanderaImpacto=False

            if rectJB.colliderect(rectA2):
                colision.explotarE(pantalla, avion2.coordX, avion2.coordY)
                jugador.puntos+=2
                jugador.BanderaImpacto=False
            

            if not jugador.BanderaImpacto:
                avionesN3+=1

            if avionesN3>=800:
                nivelMarcador=3.5


        if nivelMarcador==3.5:
            nivel.dibujar(pantalla)
            if nivel.coordY<5:
                nivelMarcador=4
                dia=True
                if not seteo:
                    mapa.setearMapa(dia)
                    seteo=True
                    
                    
            

        if nivelMarcador==4:                             ############################################---NIVEL4---
            rectO=ovni.imagen.get_rect(x=ovni.coordX, y=ovni.coordY)
            rectOB1=ovni.imagenBala.get_rect(x=ovni.coordXinicial1, y=ovni.coordYBala1)
            rectOB2=ovni.imagenBala.get_rect(x=ovni.coordXinicial2, y=ovni.coordYBala2)
            rectOB3=ovni.imagenBala.get_rect(x=ovni.coordXinicial3, y=ovni.coordYBala3)
            ovni.dibujarOvni(pantalla)
            mapa.marcador(pantalla, nivelMarcador, jugador.puntos)
            mapa.estadoJugador(pantalla, jugador.nombre, jugador.vida)
            if rectJB.colliderect(rectO):
                colision.explotarE(pantalla, ovni.coordX, ovni.coordY)
                jugador.puntos+=2
            if rectJ.colliderect(rectOB1) or rectJ.colliderect(rectOB2) or rectJ.colliderect(rectOB3):
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=10

        if ovni.contadorBalas>31 and ovni.coordY<-150:            
            copa.dibujar(pantalla)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        inicio=Inicio()
                        misil1=Misil1()
                        misil2=Misil2()
                        inicioBandera=False
                        vidaJugador = True
                        texto=''
                        posX=1
                        posY=1
                        posBusquedaY=1
                        avionSeleccionado=0
                        validacionNombre=False
                        busqueda=False
                        dia= True
                        colisiones=0
                        jugadorIdHistorial=None
                        validarEliminar1=False
                        validarEliminar2=False
                        plusVida=True
                        seteo=True
                        nivel=0
                        nivelMarcador=1
                        inicioContador=0
                        jugador.puntos=0
                        mapa.setearMapa(dia)
                        estrella.coordY=-50


        if jugador.vida<200:
            inicioContador+=1

                                            
        if jugador.vida<800 and plusVida:           ######################## -- ESTRELLA 
            rectE=estrella.estrella.get_rect(x=estrella.coordX, y=estrella.coordY)
            estrella.caer(pantalla)
            if rectJ.colliderect(rectE):
                jugador.vida+=500
                estrella.coordY=-50
                if nivelMarcador==1 or nivelMarcador==3:
                    plusVida=False
            if not rectJ.colliderect(rectE) and estrella.coordY>920:
                 estrella.coordY=-50
                 estrella.coordX-=random.randrange(-25, 35)


    elif inicioContador==5:
        finalizado=Finalizado(texto, jugador.puntos)
        finalizado.dibujarGO(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                        inicio=Inicio()
                        misil1=Misil1()
                        misil2=Misil2()
                        inicioBandera=False
                        vidaJugador = True
                        texto=''
                        posX=1
                        posY=1
                        posBusquedaY=1
                        avionSeleccionado=0
                        validacionNombre=False
                        busqueda=False
                        dia= True
                        colisiones=0
                        jugadorIdHistorial=None
                        validarEliminar1=False
                        validarEliminar2=False
                        plusVida=True
                        seteo=True
                        nivel=0
                        inicioContador=0
                        finalizado.bandera=True
                        nivelMarcador=1
                        jugador.puntos=0
                        mapa.setearMapa(dia)
                        estrella.coordY=-50

    pygame.display.flip()
    reloj.tick(80)

