import pygame


def Display():
    w = 600
    h = 600

    pygame.init()
    main_window = pygame.display.set_mode((w, h))  # окно просто окно
    pygame.display.set_caption('First try')  # название окна
    work_place = pygame.Surface((w, h))  # главное окно

    return main_window, work_place
