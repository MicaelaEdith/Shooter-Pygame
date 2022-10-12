import pygame
from mapa import Mapa
from jugador import Jugador
from elementos import Avion1, Avion2, Misil1, Misil2, Nubes, Estrella #,ColisionRoja
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()

vidaJugador = True
dia= True
colisiones=0
colision=False
mapa= Mapa()
mapa.setearMapa(dia)
jugador=Jugador()
nubes=Nubes()
misil1=Misil1()
misil2=Misil2()
#colisionR=ColisionRoja()
estrella=Estrella()
avion1= Avion1()
avion2=Avion2()



while vidaJugador:

    rectJ=jugador.image.get_rect(x=jugador.posX, y=jugador.posY) 
    rectM1=misil1.misil1[0].get_rect(x=misil1.coordX, y=misil1.coordY)
    rectM2=misil2.misil2[0].get_rect(x=misil2.coordX, y=misil2.coordY)
    rectA1=avion1.imagen.get_rect(x=avion1.coordX, y=avion1.coordY)
    rectA2=avion2.imagen.get_rect(x=avion2.coordX, y=avion2.coordY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vidaJugador = False

        if jugador.BanderaBala==False:
                jugador.coordYBala=635
                jugador.BanderaBala=True

        if jugador.puntos<80:                   #nivel1
            if rectJ.colliderect(rectM1):
                colision=True

        if jugador.puntos>=80 and jugador.puntos< 200:     #nivel2
            pass

        if jugador.puntos>=200 and jugador.puntos<300:      #nivel3
            dia=False

        if jugador.puntos>=300 and jugador.puntos<420:         #ultimoNivel
            pass

        if jugador.puntos>=420:     #ImprimirFinal-ganador
            pass
            

    mapa.dibujarMapa(pantalla)
    nubes.dibujarNubes(pantalla)
    jugador.moverJugador(event, pantalla)
    #misil1.dibujarMisil(pantalla)
    #misil2.dibujarMisil(pantalla)
    avion1.dibujarAvion(pantalla,4.5,5)
    #avion2.dibujarAvion(pantalla, 4.5,6)
    jugador.dibujarJugador(pantalla)
    #estrella.caer(pantalla)
    if colision==True:
        colision=False
        colisiones+=1
    if colisiones ==3:
        vidaJugador=False


    pygame.display.flip()
    reloj.tick(60)

