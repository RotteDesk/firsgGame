import pygame

from modul_tank import tank

pygame.init()
###########################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

size_of_window = (400,400)
window = pygame.display.set_mode(size_of_window)
####################################################################
pygame.display.set_caption('Tank')  # название окна

screen = pygame.Surface((size_of_window))  # главное окно

clock_1 = pygame.time.Clock()
FPS = 60



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()


    screen.fill(GREY)


    ########################
    clock_1.tick(FPS)
    #########################
    window.blit(screen, (0, 0))  # прилепляем наш экран на окно
    pygame.display.flip()
