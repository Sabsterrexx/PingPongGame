#Import required Modules:
import constants
import pygame

screen = constants.initialize()


#Paddle Class:

class Paddle:
    def __init__(self):   
        self.x = 0
        self.y = constants.cy
        self.color = constants.colors["RED"]
        self.speed = 10
        self.dy = 0
        self.score = 0
        self.width = 10
        self.height = 100

    #border collision method:
    def border_collision(self):
        if self.y <= self.width:
            self.y = self.width
        elif self.y >= constants.screenHeight - (self.height + 10):
            self.y = constants.screenHeight - (self.height + 10)

    #movement method:
    def move(self):
        self.y = self.y + self.dy
    
    #draw to screen method:
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height),0)

