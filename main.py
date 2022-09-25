import pygame
from mapa import Mapa
from jugador import Jugador
from elementos import Misil1, Misil2, Nubes
pygame.init()

medidaPantalla = (800,750)
pantalla = pygame.display.set_mode(medidaPantalla)
reloj = pygame.time.Clock()

vidaJugador = True
dia= False
colisiones=0
mapa= Mapa()
mapa.setearMapa(dia)
jugador=Jugador()
nubes=Nubes()
misil1=Misil1()
misil2=Misil2()


while vidaJugador:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vidaJugador = False
        if jugador.BanderaBala==False:
                jugador.coordYBala=635
                jugador.BanderaBala=True
        if (misil1.coordY+90>565 and misil1.coordY<720) and (misil1.coordX>jugador.posX and misil1.coordX<jugador.posX+90):
            colisiones+=1
        if (misil2.coordY+90>565 and misil2.coordY<720) and (misil2.coordX>jugador.posX and misil2.coordX<jugador.posX+90):
            colisiones+=1
        if colisiones==2:
            print("gameOver")   #   <--       ######### probando colisiones, animación en 'colisionRojo'
        
        
    mapa.dibujarMapa(pantalla)
    nubes.dibujarNubes(pantalla)
    misil1.dibujarMisil(pantalla)
    misil2.dibujarMisil(pantalla)
    jugador.moverJugador(event, pantalla)
    jugador.dibujarJugador(pantalla)


    pygame.display.flip()
    reloj.tick(60)
