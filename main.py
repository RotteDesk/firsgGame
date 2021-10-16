import pygame as pg

pg.init()
###########################################################
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
size_of_window = (400,400)
window = pg.display.set_mode(size_of_window)  # окно просто окно

pg.display.set_caption('First try')  # название окна

sc = pg.Surface((size_of_window))  # главное окно

clock_1 = pg.time.Clock()

FPS = 60
###########################################################
'''наш обьект'''
x, y = 200, 200  # дал две переменные для позиции

Tank_img_load = pg.image.load('pictures/up.png')
#wt1, ht1 = t1.get_size()

speed = 1  # дал скорость своей машинке

##################J.23.1941###############################


run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            quit()

            # управление
    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        Tank_img_load = pg.image.load('pictures/up.png')
        y -= speed

    elif key[pg.K_DOWN]:
        Tank_img_load = pg.image.load('pictures/down.png') # не тот метод для использования в игре
        y += speed

    elif key[pg.K_LEFT]:
         Tank_img_load = pg.image.load('pictures/left.png')
         x -= speed

    elif key[pg.K_RIGHT]:
        Tank_img_load = pg.image.load('pictures/right.png')
        x += speed


    sc.fill(GREY)
    sc.blit(Tank_img_load, (x, y))  # прилепил картинку к рабочему столу, так сказать, и дал координаты
    pg.display.update()  # обновляю дисплей,что б картинка работала
    ########################
    clock_1.tick(FPS)
    #########################
    window.blit(sc, (0, 0))  # прилепляем наш экран на окно
    pg.display.flip()
