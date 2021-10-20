import pygame


class Tank_1(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()# ускорит прорисовку в Pygame, конвертируя изображение в тот формат, который будет быстрее появляться на экране
        self.rect = self.image.get_rect()  # размер и местоположение  изображения
        self.x = x
        self.y = y
        self.up = pygame.transform.rotate(self.image, 0)
        self.down = pygame.transform.rotate(self.image, 180)
        self.right = pygame.transform.rotate(self.image, -90)
        self.left = pygame.transform.rotate(self.image, 90)
        self.size = self.image.get_size()

    def render(self, speed, work_place):
        work_place.blit(self.image, (self.x, self.y))
        self.speed = speed
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.image = self.up
            self.y -= speed
            if self.y < 0:
                self.y = 0 # тут сообразил, но если сделаю окно, что ожно изменить в размере, то все пойдет не так

        elif key[pygame.K_DOWN]:
            self.image = self.down
            self.y += speed
            if self.y > 600:
                self.y = 600 - # нужна помощьб не соображу,как сжедать столкновение с экраном и остановку


        elif key[pygame.K_LEFT]:
            self.image = self.left
            self.x -= speed
            if self.x < 0:
                self.x = 0

        elif key[pygame.K_RIGHT]:
            self.image = self.right
            self.x += speed


