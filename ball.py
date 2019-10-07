import constants
import pygame
import random

#initializing all the constants
screen = constants.initialize()

#Ball class:

class Ball:
    def __init__(self):
        #ball attributes needed for drawing the ball such al the color, the speed and the co-ordinates, etc.
        self.x = constants.cx        
        self.y = constants.cy
        self.color = constants.colors["PURPLE"]
        self.dx = 0
        self.dy = 0
        self.speed = 5
        self.radius = 10


    #method to change into desired color:
    def change_color(self, color):
        self.color = color


    #ball collison with borders method
    def border_collision(self):
        #right side:
        if self.x >= constants.screenWidth - self.radius:
            self.dx = -abs(self.speed)
        #left side:
        elif self.x <= self.radius:
            self.dx = abs(self.speed)
        #top side:
        if self.y <= self.radius:
            self.dy = abs(self.speed)
        #bottom side:
        elif self.y >= constants.screenHeight - self.radius:
            self.dy = -abs(self.speed)
    

    #paddle movement method
    def move(self):    
        self.x = self.x + self.dx
        self.y = self.y + self.dy
    

    #draw paddle onto screen method
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)

