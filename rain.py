import pygame
import random
import string
from time import sleep
from game_objects import Tear, Rain


pygame.init()
pygame.key.set_repeat()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 600
Y = 600

display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font('freesansbold.ttf', 20)


r = Rain(font, X, green, blue)

while True:

    r.add_new_Tear(font, X, green, blue)
    r.update_tears(font)
    display_surface.fill(white)
    r.render_tears(display_surface)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            ch = pygame.key.name(event.key)
            r.lock_tear(ch)
            r.update_locked_tear(ch)
            r.remove_locked_tear()

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

    pygame.display.update()

    sleep(0.03)
