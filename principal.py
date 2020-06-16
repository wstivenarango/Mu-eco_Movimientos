import sys
import pygame
import util
from pygame.locals import *
from personaje import *

def game():
    pygame.init()
    posX=200
    posY=200
    screen = pygame.display.set_mode((1000, 900))
    pygame.display.set_caption("Mario_Cambios")
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)
    heroe = Heroe()
    heroe.defPositions(posX,posY)
    ejecutando = True
    jugando = True 
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        screen.blit(background_image, (0,0))
        if jugando:
            
            heroe.update(sprite)
            heroe.draw(screen)
        pygame.display.update()  

if __name__ == '__main__':
    game()

