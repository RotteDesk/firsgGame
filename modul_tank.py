import pygame


class Tank_1(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()  # ускорит прорисовку в Pygame, конвертируя изображение в тот формат, который будет быстрее появляться на экране
        self.rect = self.image.get_rect()  # размер и местоположение  изображения
        self.x = x
        self.y = y
        self.up = pygame.transform.rotate(self.image, 0)
        self.down = pygame.transform.rotate(self.image, 180)
        self.right = pygame.transform.rotate(self.image, -90)
        self.left = pygame.transform.rotate(self.image, 90)

    def render(self, speed, work_place):
        work_place.blit(self.image, (self.x, self.y))
        self.speed = speed
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.image = self.up
            self.y -= speed

        elif key[pygame.K_DOWN]:
            self.image = self.down
            self.y += speed

        elif key[pygame.K_LEFT]:
            self.image = self.left
            self.x -= speed

        elif key[pygame.K_RIGHT]:
            self.image = self.right
            self.x += speed


