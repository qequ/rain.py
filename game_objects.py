import random
import nltk
from nltk.corpus import words


LIST_WORDS = list(map(lambda s: s.lower(), words.words()))


class Tear():

    def __init__(self, font, screen_width, color1, color2, is_custom_word=False, custom_word=''):
        chosen_word = random.choice(LIST_WORDS)

        self.x = random.randint(0, screen_width - font.size(chosen_word)[0])
        self.y = 0
        self.color1 = color1
        self.color2 = color2
        if custom_word:
            self.word = custom_word
        else:
            self.word = chosen_word
        self.text = font.render(self.word, True, self.color1, self.color2)
        self.textRect = self.text.get_rect()

    def update_y(self):
        self.y += 1

    def update_tear(self, font):

        self.text = font.render(self.word, True, self.color1, self.color2)
        self.textRect = self.text.get_rect()

        self.textRect.x = self.x
        self.textRect.y = self.y

    def check_char(self, char):

        if self.word.startswith(char):
            self.word = self.word[1:]


class Rain():

    def __init__(self, font, max_width, color1, color2, custom_list=[], main_menu=False):
        self.tears = custom_list  # the list of words that is going through the screen
        self.chosen = -1  # this refers to the word's index position which player is typing
        self.__score = 0
        if not main_menu:
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
                self.__score += 1 
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

    def return_score(self):
    	return self.__score
    
    def update_tears(self, font):
        for t in self.tears:
            t.update_tear(font)
            t.update_y()

    def render_tears(self, display_surface):
        for t in self.tears:
            display_surface.blit(t.text, t.textRect)
