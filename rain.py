import pygame
import random
import string
from time import sleep
import nltk


from nltk.corpus import words


LIST_WORDS = list(map(lambda s: s.lower(), words.words()))


class Tear():

    def __init__(self, font, screen_width, color1, color2):
        chosen_word = random.choice(LIST_WORDS)

        self.x = random.randint(0, screen_width - font.size(chosen_word)[0])
        self.y = 0
        self.color1 = color1
        self.color2 = color2
        self.word = chosen_word
        self.text = font.render(self.word, True, self.color1, self.color2)
        self.textRect = self.text.get_rect()

    def update_y(self):
        self.y += 1

    def update_tear(self, font):
        """
            text = font.render(r_str, True, green, blue)

            textRect = text.get_rect()

            textRect.x = given_x
            textRect.y = last_y

        """

        self.text = font.render(self.word, True, self.color1, self.color2)
        self.textRect = self.text.get_rect()

        self.textRect.x = self.x
        self.textRect.y = self.y

    def check_char(self, char):
        """
            if r_str.startswith(pygame.key.name(event.key)):
                r_str = r_str[1:]

        """

        if self.word.startswith(char):
            self.word = self.word[1:]


class Rain():

    def __init__(self, font, max_width, color1, color2):
        self.tears = []
        self.chosen = -1
        self.tears.append(Tear(font, max_width, color1, color2))

    def is_locked_tear(self):
        if self.chosen == -1:
            return False
        return True

    def add_new_Tear(self, font, screen_width, color1, color2):
        if len(self.tears) == 0 or random.random() >= 0.5 and self.tears[-1].y > 100:
            new_tear = Tear(font, screen_width, color1, color2)
            self.tears.append(new_tear)


    def remove_locked_tear(self):
        if self.is_locked_tear():
            if self.tears[self.chosen].word == '':
                self.tears.pop(self.chosen)
                self.chosen = -1

    def update_locked_tear(self, char):
        if self.is_locked_tear():
            self.tears[self.chosen].check_char(char)

    def lock_tear(self, char):
        if not self.is_locked_tear():
            for i in range(len(self.tears)):
                if self.tears[i].word.startswith(char):
                    self.chosen = i
                    break

    def update_tears(self, font):
        for t in self.tears:
            t.update_tear(font)
            t.update_y()

    def render_tears(self, display_surface):
        """
        display_surface.blit(t.text, t.textRect)
        """
        for t in self.tears:
            display_surface.blit(t.text, t.textRect)


pygame.init()
pygame.key.set_repeat()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 600
Y = 600

display_surface = pygame.display.set_mode((X, Y))

font = pygame.font.Font('freesansbold.ttf', 20)


"""
N = random.randint(1, 30)

r_str = ''.join(random.choice(string.ascii_uppercase + string.digits)
                for _ in range(N)).lower()
"""

"""
r_str = random.choice(words.words())
text = font.render(r_str, True, green, blue)

textRect = text.get_rect()

if X - font.size(r_str)[0] > 600:
    print("EXCEPTION")
    raise Exception

given_x = random.randint(0, X - font.size(r_str)[0])
textRect.x = given_x
textRect.y = 0
last_y = 0
"""


#t = Tear(font, X, green, blue)
r = Rain(font, X, green, blue)

while True:

    """
    text = font.render(r_str, True, green, blue)

    textRect = text.get_rect()

    if X - font.size(r_str)[0] > 600:
        print("EXCEPTION")
        raise Exception
    textRect.x = random.randint(0, X - font.size(r_str)[0])
    textRect.y = Y // 2
    """

    """
    text = font.render(r_str, True, green, blue)

    textRect = text.get_rect()

    textRect.x = given_x
    textRect.y = last_y

    last_y += 1
    """

    """
    t.update_tear(font)
    t.update_y()

    display_surface.fill(white)

    display_surface.blit(t.text, t.textRect)
    """

    r.add_new_Tear(font, X, green, blue)
    r.update_tears(font)
    display_surface.fill(white)
    r.render_tears(display_surface)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            # print(pygame.key.name(event.key))
            # t.check_char(pygame.key.name(event.key))
            ch = pygame.key.name(event.key)
            r.lock_tear(ch)
            r.update_locked_tear(ch)
            r.remove_locked_tear()
            """
            if r_str.startswith(pygame.key.name(event.key)):
                r_str = r_str[1:]
            """

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

    pygame.display.update()

    sleep(0.03)
