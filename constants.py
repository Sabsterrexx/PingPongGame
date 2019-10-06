#Import required Modules:

import pygame

#Declaring all the constants in one file

colors = {"WHITE": (255,255,255), "GREEN": (0,255,0), "RED": (255,0,0), "BLUE": (0,0,255),"BLACK": (0,0,0), "PURPLE": (128,0,128)}
screenWidth = 0
screenHeight = 0
maxScore = 10
cx = 0
cy = 0

def initialize():
    global cx
    global cy
    global screenWidth
    global screenHeight
    pygame.init()
    screenSize = (800,600)
    screen = pygame.display.set_mode((screenSize),0)
    pygame.display.set_caption("Saabit Ping Pong Game")

    screen.fill(colors["WHITE"])
    pygame.display.update()
    pygame.key.set_repeat(1,1)
    screenWidth = screen.get_width()
    screenHeight = screen.get_height()
    cx = screenWidth//2
    cy = screenHeight//2
    return screen
