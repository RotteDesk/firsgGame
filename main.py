import pygame
from work_place import initPyGame
from modul_tank import Tank_1

pygame.init()
###########################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
####################################################################
main_window, work_place = initPyGame()
###################################################################
clock_1 = pygame.time.Clock()
FPS = 60
Plaeyr_1 = Tank_1(200, 200, 'pictures/up.png')

game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            quit()


    work_place.fill(GREY)

    Plaeyr_1.render(1, work_place)

    ########################
    clock_1.tick(FPS)
    #########################
    main_window.blit(work_place, (0, 0))  # прилепляем наш экран на окно
    pygame.display.update()
