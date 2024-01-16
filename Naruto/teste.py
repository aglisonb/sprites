import pygame as pg
from pygame.locals import *

pg.init()
win = pg.display.set_mode((800, 600))
sprite_sheet = pg.image.load("teste.png")

leave = False
naruto_x = 100
naruto_y = 400
jumping = False
jump_count = 10

while not leave:
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            leave = True

    key = pg.key.get_pressed()


    if key[K_SPACE] and not jumping:
        jumping = True
        jump_start_y = naruto_y

    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            naruto_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1

            frame_y = 280
        else:
            jumping = False
            jump_count = 10
            frame_y = 280
            naruto_y = jump_start_y

    else:
        key = pg.key.get_pressed()
        if key[K_RIGHT]:
            naruto_x += 15
        elif key[K_LEFT]:
            naruto_x -= 15

            # Use o índice ou posição correto para a animação normal
            win.blit(sprite_sheet, (naruto_x, naruto_y), (0, 0, 80, 80))

    pg.display.flip()
    pg.time.Clock().tick(10)
    win.fill(0)

pg.quit()
