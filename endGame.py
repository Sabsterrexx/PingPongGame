#Import required Modules:
import sys
import pygame
import constants
from screenState import ScreenState


#This function is designed to generate the game's end screen
def show(screenState: ScreenState):

    end_game = True
        
    while end_game:
        #Event listeners loop:
        for event in pygame.event.get():
                #Closing the game event listener:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    end_game = False
                    return
 
        screenState.screen.fill(constants.colors["WHITE"])

        #Setting the text to the screen:
        screenState.endScreen_text.text = "Game Over. " + screenState.winner + " wins. Press 'p' to play again"
        screenState.endScreen_text.x = 200
        screenState.endScreen_text.y = 300
        screenState.endScreen_text.write()

        #Write score(s):
        screenState.paddle1Score.write()
        screenState.paddle2Score.write()

        pygame.display.update()
