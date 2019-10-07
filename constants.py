#Import required Modules:

import pygame

#Declaring all the constants in one file that will be used throughout the program

#Making a dictionary of all the possible colors, where each key represents a string which spells a color and its value it's RGB representation in a tuple 
colors = {"WHITE": (255,255,255), "GREEN": (0,255,0), "RED": (255,0,0), "BLUE": (0,0,255),"BLACK": (0,0,0), "PURPLE": (128,0,128)}
screenWidth = 0
screenHeight = 0
maxScore = 10
cx = 0
cy = 0

#variables used to identify the shape's buttons keycodes for the PS3 contorllers 
joyUp = 0
joyDown = 2


#This function initializes the variables that will be used by the end, start and playing screens

def initialize():
    #I had to use the 'global' keyword because python could not tell whether I was creating new variables wiht a local scope or changing the values of pre-declared global variables
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
