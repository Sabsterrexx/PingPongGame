#Import required Modules:
import constants
import pygame

#Text/title class:

class Text:
    def __init__(self, screen):
        #making all the attributes for the text class
        self.font = "arial"
        self.x = 40
        self.y = 300
        self.size = 18
        self.text = " "
        self.color = constants.colors["BLUE"]
        self.dx = 2
        self.dy = 2

        #attributes needed for the draw function:
        self.fonttitle = pygame.font.SysFont(self.font,self.size)
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        self.screen = screen

        self.width = self.rendertitle.get_width()
        self.height = self.rendertitle.get_height()

    #method that writes the titles text to the screen
    def write(self):
        self.rendertitle = self.fonttitle.render(self.text,True,self.color)
        return self.screen.blit(self.rendertitle,(self.x,self.y))
