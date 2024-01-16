import pygame as pg
from pygame.locals import *

pg.init()
win = pg.display.set_mode((800, 600))
sprite_sheet = pg.image.load("teste (2).png")

leave = False
x_sprite = 0
y_sprite = 0
naruto_x = 100
naruto_y = 400
jumping = False
jump_count = 10
jump_start_y = 0

while not leave:
    for e in pg.event.get():
        if e.type == pg.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            leave = True

    key = pg.key.get_pressed()
    if key[K_SPACE] and not jumping:
        jumping = True
        jump_start_y = naruto_y  # Guarda a posição inicial do pulo

    if jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            naruto_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1

            # Exibe as frames enquanto ele está pulando
            if jump_count > -8:
                frame_index = 0  # Frames de subida
            else:
                frame_index = 2  # Frames de queda

            frame_y = 280  # Posição y fixa para todas as frames de pulo
            win.blit(sprite_sheet, (naruto_x, naruto_y), (frame_index * 80, frame_y, 80, 80))
        else:
            jumping = False
            jump_count = 10
            frame_index = 5  # Frame de pouso
            frame_y = 280
            naruto_y = jump_start_y  # Restaura a posição inicial após o pulo

    key = pg.key.get_pressed()
    if key[K_RIGHT]:
        naruto_x += 15
        y_sprite = 90
        x_sprite += 1
    elif key[K_LEFT]:
        naruto_x -= 15
        y_sprite = 185
        x_sprite += 1
    else:
        if y_sprite == 185:
            y_sprite = 0
        elif y_sprite == 90:
            y_sprite = 0
        x_sprite += 1
    if x_sprite > 5:
        x_sprite = 0

    if not jumping:
        win.blit(sprite_sheet, (naruto_x, naruto_y), (x_sprite * 80, y_sprite, 80, 80))
    else:
        win.blit(sprite_sheet, (naruto_x, naruto_y), (frame_index * 80, frame_y, 80, 80))

    pg.display.flip()
    pg.time.Clock().tick(10)
    win.fill(0)
