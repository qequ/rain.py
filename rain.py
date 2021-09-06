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

#            new_tear = Tear(font, screen_width, color1, color2)

main_menu = [Tear(font, X, green, blue, True, "rain.py"),
             Tear(font, X, green, blue, True, "start"),
             Tear(font, X, green, blue, True, "quit")
             ]
main_menu[0].x = X // 2
main_menu[1].x = (X // 2) - 60
main_menu[2].x = (X // 2) + 60

r_main_menu = Rain(font, X, green, blue, main_menu, True)

# start screen loop
while len(r_main_menu.tears) == 3:

    for t in r_main_menu.tears:
        t.update_tear(font)

    for t in main_menu:
        if t.word == "rain.py" and t.y < (Y // 4):
            t.update_y()

        if (t.word == "start" or t.word == "quit") and t.y < ((Y // 4) + 50):
            t.update_y()

    display_surface.fill(white)

    r_main_menu.render_tears(display_surface)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            ch = pygame.key.name(event.key)
            r_main_menu.lock_tear(ch)
            r_main_menu.update_locked_tear(ch)
            r_main_menu.remove_locked_tear()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    sleep(0.001)

exited = True

for t in r_main_menu.tears:
    if t.word == "quit":
        exited = False

if exited:
    pygame.quit()
    quit()

# Main game loop
r = Rain(font, X, green, blue)

while True:

    r.add_new_Tear(font, X, green, blue)
    r.update_tears(font)
    display_surface.fill(white)
    r.render_tears(display_surface)
    a = r.return_score()
    text = font.render("Score:"+str(a), True, green, blue)
    textrec = text.get_rect()
    textrec.center = (X-50 , 15)
    display_surface.blit(text, textrec)

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
