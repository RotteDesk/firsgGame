import pygame


class Tank_1(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha() # ускорит прорисовку в Pygame, конвертируя изображение в тот формат, который будет быстрее появляться на экране
        self.rect = self.image.get_rect() # размер и местоположение  изображения
        self.x = x
        self.y = y
        self.speed = speed
    def render(self,work_place):
        work_place.blit(self.image, (self.x, self.y)) # хочу сделать прилепление на экран моего объекта но чет не идет..

