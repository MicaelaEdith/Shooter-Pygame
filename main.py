import pygame
import string
from inicio import Inicio
from mapa import Mapa
from jugador import Jugador
from elementos import Avion1, Avion2, Misil1, Misil2, Nubes, Estrella, ColisionAviones, Ovni, Nivel
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()
inicioContador=0
inicioBandera=False
vidaJugador = True
texto=''
posX=1
validacionNombre=False
dia= True
colisiones=0
colision=False
mapa= Mapa()
mapa.setearMapa(dia)
jugador=Jugador()
nubes=Nubes()
misil1=Misil1()
misil2=Misil2()
colision=ColisionAviones()
estrella=Estrella()
avion1= Avion1()
avion2=Avion2()
ovni=Ovni()
nivel=Nivel()
plusVida=True
seteo=True
inicio=Inicio()


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
        inicio.dibujar0(pantalla,event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if inicio.seleccionX==440:
                        inicioContador+=2
                    elif inicio.seleccionX==200:
                        inicioContador+=1

    elif inicioContador==1:

        inicio.dibujar1(pantalla, texto, posX, validacionNombre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if validacionNombre:
                        inicioContador+=2
                        inicio.guardar('1', texto, posX, '0')
                
                if event.key == pygame.K_LEFT:
                    if posX==2 or posX==3:
                        posX-=1
                if event.key == pygame.K_RIGHT:
                    if posX ==1 or posX==2:
                        posX+=1

                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                elif not event.key==pygame.K_RETURN:
                    texto += event.unicode      
            if not texto=='':                                   #####seguir desde acá, máximo de caracteres=10 -- hacer validacion
                validacionNombre=True
            if texto=='':
                validacionNombre=False

            
    elif inicioContador==2:
        inicio.dibujar2(pantalla, texto)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicioContador+=1

                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    texto += event.unicode
    
    elif inicioContador==3:
        inicio.dibujar3(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                vidaJugador = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicioContador+=1
                    inicioBandera = True
                
    else: 
        mapa.dibujarMapa(pantalla)
        nubes.dibujarNubes(pantalla)
        mapa.marcador(pantalla, 1, jugador.puntos)

        if inicioBandera:
            jugador.setearJugador(texto,posX)
            del inicio
            inicioBandera=False

        mapa.estadoJugador(pantalla, jugador.nombre, jugador.vida)

        jugador.moverJugador(event, pantalla)
        jugador.dibujarJugador(pantalla)
        rectJ=jugador.image.get_rect(x=jugador.posX, y=jugador.posY)
        rectJB=jugador.bala.get_rect(x=jugador.posX+48, y=jugador.coordYBala)


        if jugador.puntos<20:                       #################################################---NIVEL1---
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            avion1.dibujarAvion(pantalla,3.8,7)
            if rectJ.colliderect(rectA1): 
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=5
            
            if rectJB.colliderect(rectA1) and jugador.BanderaImpacto:
                colision.explotarE(pantalla, avion1.coordX, avion1.coordY)
                jugador.puntos+=10
                jugador.BanderaImpacto=False

    ##################---DefinirImagenLevelUp

        plusVida=True
        if jugador.puntos>=20 and jugador.puntos<150 and misil1.contador<5:    ############################################---NIVEL2---
            rectM1=misil1.misil1[0].get_rect(x=misil1.coordX, y=misil1.coordY)
            rectM2=misil2.misil2[0].get_rect(x=misil2.coordX, y=misil2.coordY)
            misil1.dibujarMisil(pantalla)
            misil2.dibujarMisil(pantalla)
            if rectJ.colliderect(rectM1) or rectJ.colliderect(rectM2):
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=5
            
        if (jugador.puntos>=150 and jugador.puntos<250) or misil1.contador==5:   ############################################---NIVEL3---
            dia=False
            if seteo:
                mapa.setearMapa(dia)
                seteo=False
            
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            rectA2=avion2.imagen.get_rect(x=avion2.coordX, y=avion2.coordY)
            avion1.dibujarAvion(pantalla,3.5,8)
            avion2.dibujarAvion(pantalla, 3.5,8)
            if rectJ.colliderect(rectA1) or rectJ.colliderect(rectA2):
                colision.explotar(pantalla, jugador.posX-20)
            if (rectJB.colliderect(rectA1) or rectJB.colliderect(rectA2)) and rectJB.y<620:
                jugador.puntos+=10
                jugador.BanderaImpacto=False 

        if jugador.puntos>=250 and jugador.puntos<450:   ############################################---NIVEL4---
            ovni.dibujarOvni(pantalla)

        if jugador.vida<800 and plusVida:
            rectE=estrella.estrella.get_rect(x=estrella.coordX, y=estrella.coordY)
            estrella.caer(pantalla)
            plusVida=False
            if rectJ.colliderect(rectE):
                jugador.vida+=500
        #if colision==True:
        #    colision=False
        #    colisiones+=1
        #if colisiones ==3:
        #   vidaJugador=False

#definirPantallaFin

    pygame.display.flip()
    reloj.tick(60)

