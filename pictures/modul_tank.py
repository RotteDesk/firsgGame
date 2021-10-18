import pygame


class tank(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pictures/up.png').convert_alpha()
        self.rect = self.image.get_rect(left=(x, y)) # размер и местоположение  изображения
        self.speed = 1
