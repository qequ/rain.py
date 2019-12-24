import pygame
import random
import string
from time import sleep
import nltk


from nltk.corpus import words


LIST_WORDS = words.words()


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


# HELPERS --

def set_position_rectangle(font, rect, max_x, given_str):
    rect.x = random.randint(0, max_x - font.size(given_str)[0])

    """
    print(X - font.size(r_str)[0])
    if X - font.size(r_str)[0] > 600:
        print("EXCEPTION")
        raise Exception
    textRect.x = random.randint(0, X - font.size(r_str)[0])
    textRect.y = Y // 2
    """


"""
    chunk of code liberating string

        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if r_str.startswith(pygame.key.name(event.key)):
                r_str = r_str[1:]


"""

# ENDHELPERS


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

t = Tear(font, X, green, blue)

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
    t.update_tear(font)
    t.update_y()

    display_surface.fill(white)

    display_surface.blit(t.text, t.textRect)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            t.check_char(pygame.key.name(event.key))
            """
            if r_str.startswith(pygame.key.name(event.key)):
                r_str = r_str[1:]
            """

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

    pygame.display.update()

    sleep(0.03)
