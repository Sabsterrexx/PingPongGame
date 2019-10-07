#Import required Modules:
import pygame
from pygame import joystick
import constants
from paddle import Paddle
from ball import Ball
from score import Score
from text import Text
from screenState import ScreenState


#This function basically executes everything in the "screenState" module's class 
def init():
    #Initialize all the constants:
    screen = constants.initialize()


    #Making the FPS clock:
    clock = pygame.time.Clock()
    FPS = 60

    #Creating paddle 1 score:
    paddle1Score = Score(screen)
    paddle1Score.x = 100


    #Creating paddle 2 score:
    paddle2Score = Score(screen)
    paddle2Score.color = constants.colors["RED"]


    #Making 2 paddles:
    paddle1 = Paddle()
    paddle1.x = paddle1.width
    paddle1.color = constants.colors["BLUE"]

    paddle2 = Paddle()
    paddle2.x = constants.screenWidth - paddle2.width
    paddle2.color = constants.colors["RED"]


    # Making the ball:
    ball = Ball()
    ball.dx = ball.speed
    ball.dy = ball.speed    
    #The ball starts at the center:           
    ball.x = constants.cx
    ball.y = constants.cy
    #The ball's intital color is blue
    ball.color = constants.colors["PURPLE"]

    #Creating the title screen's text:
    title_text = Text(screen)
    title_text.x = 10
    title_text.text = "Welcome to Saabit Pong Game. Difficulty keys: Easy: 1, Medium: 2, Hard: 3"

    #Creating the end game screen's text
    endScreen_text = Text(screen)
    endScreen_text.text = "Game Over. Press 'P' to play again"
   
   #function if the joysticks are connected to pygame
    initJoysticks()

    #returns the new object instance of the ScreenState class
    return ScreenState(screen, title_text, endScreen_text, paddle1, paddle2, ball, paddle1Score, paddle2Score, clock, FPS)


#function to check if the joysticks are initialized
def initJoysticks():
    for x in range (joystick.get_count()):
        j = joystick.Joystick(x)
        j.init()
        #print the name of every joystick pygame is able to detect in the terminal
        txt = "Enabled joystick: " + j.get_name()
        print(txt)
    #if no joysticks are detected, print "no joysticks to initialize" in the terminal   
    if not joystick.get_count():
        print("No Joysticks to Initialize")
