#import modules:

import constants
import pygame

# Score Class:

class Score:
    def __init__(self, screen):
        self.font = "arial"
        self.x = 500
        self.y = 500
        self.size = 50
        self.color = constants.colors["BLUE"]
        self.score = 0
        self.text = "Score: " 


        #Attributes needed for "Score.write()" method:
        self.fonttitle = pygame.font.SysFont(self.font,self.size)
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        self.screen = screen

    #write to screen function:

    def write(self):
        int(self.score)
        self.text = "Score: " + str(self.score)
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        return self.screen.blit(self.rendertitle,(self.x,self.y))
    