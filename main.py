import pygame
from inicio import Inicio
from mapa import Mapa
from jugador import Jugador
from elementos import Avion1, Avion2, Misil1, Misil2, Nubes, Estrella, ColisionAviones, Ovni, Nivel
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()
inicio=Inicio()

inicio1=0
vidaJugador = True
dia= True
colisiones=0
colision=False
mapa= Mapa()
mapa.setearMapa(dia)
jugador=Jugador("Mica ")
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

while vidaJugador:
    if inicio1==0:
        inicio.dibujar1(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        inicio1+=1
    elif inicio1==1:
        inicio.dibujar2(pantalla)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inicio1+=1

    else: 
        mapa.dibujarMapa(pantalla)
        nubes.dibujarNubes(pantalla)
        mapa.marcador(pantalla, 1, jugador.puntos)
        mapa.estadoJugador(pantalla, jugador.nombre, jugador.vida)
            
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

        jugador.moverJugador(event, pantalla)
        jugador.dibujarJugador(pantalla)
        rectJ=jugador.image.get_rect(x=jugador.posX, y=jugador.posY)
        rectJB=jugador.bala.get_rect(x=jugador.posX+48, y=jugador.coordYBala)

        if jugador.puntos<80:                       #################################################---NIVEL1---
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            avion1.dibujarAvion(pantalla,4.5,5)
            if rectJ.colliderect(rectA1): 
                colision.explotar(pantalla, jugador.posX-20)
                jugador.vida-=5
            
            if rectJB.colliderect(rectA1) and jugador.BanderaImpacto:
                colision.explotarE(pantalla, avion1.coordX, avion1.coordY)
                jugador.puntos+=10
                jugador.BanderaImpacto=False

    ##################---DefinirImagenLevelUp

        plusVida=True
        if jugador.puntos>=80 and jugador.puntos<150 and misil1.contador<15:    ############################################---NIVEL2---
            rectM1=misil1.misil1[0].get_rect(x=misil1.coordX, y=misil1.coordY)
            rectM2=misil2.misil2[0].get_rect(x=misil2.coordX, y=misil2.coordY)
            misil1.dibujarMisil(pantalla)
            misil2.dibujarMisil(pantalla)
            if rectJ.colliderect(rectM1) or rectJ.colliderect(rectM2):
                colision.explotar(pantalla, jugador.posX-20)



        if (jugador.puntos>=150 and jugador.puntos<250) or misil1.contador==15:   ############################################---NIVEL3---
            rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
            rectA2=avion2.imagen.get_rect(x=avion2.coordX, y=avion2.coordY)
            avion1.dibujarAvion(pantalla,4,8)
            avion2.dibujarAvion(pantalla, 4,8)
            if rectJ.colliderect(rectA1) or rectJ.colliderect(rectA2):
                colision.explotar(pantalla, jugador.posX-20)
            if rectJB.colliderect(rectA1) or rectJB.colliderect(rectA2):
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
    reloj.tick(120)

