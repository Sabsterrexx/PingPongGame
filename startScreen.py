#Import required Modules:
import sys
import pygame
import constants
from screenState import ScreenState


#This function is designed to handle the game's start screen
def show(screenState: ScreenState):

    #Beginning of main start screen while-loop:
    start_screen = True
    while start_screen:
        #Event listeners for-loop for the start screen loop:
        for event in pygame.event.get():
            #Event listener for closing the game:
            if event.type == pygame.QUIT:
                #closing the game:
                start_screen = False
                pygame.quit()
                sys.exit()
            #Key down event listeners, for adjusting game difficulty:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    #adjusting ball speed and radius:
                    screenState.ball.speed = 5
                    screenState.ball.radius = 20
                    #adjusting paddle height:
                    screenState.paddle1.height = 100
                    screenState.paddle2.height = 100                    
                    start_screen = False
                if event.key == pygame.K_2:
                    #adjusting ball speed and radius
                    screenState.ball.speed = 6
                    screenState.ball.radius = 15
                    #changing paddle height
                    screenState.paddle1.height = 95
                    screenState.paddle2.height = 95
                    start_screen = False
                if event.key == pygame.K_3:
                    #adjusting ball speed
                    screenState.ball.speed = 7
                    screenState.ball.radius = 10
                    #changing paddle height
                    screenState.paddle1.height = 90
                    screenState.paddle2.height = 90
                    start_screen = False
        

        #Erase screen:
        screenState.screen.fill(constants.colors["WHITE"])

        #Write title onto screen
        screenState.title_text.write()
        
        #Update the screen's display:
        pygame.display.update()
