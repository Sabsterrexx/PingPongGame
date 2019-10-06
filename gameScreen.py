#Import required Modules:
import sys
import pygame
import constants
import time
from screenState import ScreenState


#This function is designed to handle the games's playing screen:

def show(screenState: ScreenState):
        
    #Main Drawing Loop
    while True:  

        processKeyboardInput(screenState)

        #controlling the speed of the loop:
        screenState.clock.tick(screenState.FPS)

        detectCollisions(screenState)

        #Making everything move:
        screenState.paddle1.move()
        screenState.paddle2.move()
        screenState.ball.move()

        #Erase Screen:
        screenState.screen.fill(constants.colors["WHITE"])

        #Updating scores
        updateScore(screenState)

        #Draw Paddles and ball:
        screenState.paddle1.draw()
        screenState.paddle2.draw()
        screenState.ball.draw()

        #Check if game has ended
        if hasGameEnded(screenState):
        #If the game has ended step out of the loop
            return

        #Redraw everything:
        pygame.display.update()


#Function for the event listeners:
def processKeyboardInput(screenState: ScreenState):
    #Event listeners for-loop:
    for event in pygame.event.get():
        #Closing the game event listener:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Key down event listeners:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                screenState.paddle1.dy = -screenState.paddle1.speed
            elif event.key == pygame.K_s:
                screenState.paddle1.dy = screenState.paddle1.speed
            elif event.key == pygame.K_UP:
                screenState.paddle2.dy = -screenState.paddle2.speed
            elif event.key == pygame.K_DOWN:
                screenState.paddle2.dy = screenState.paddle2.speed
                
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.joy == 0:
                if event.button == constants.joyDown:
                    screenState.paddle1.dy = -screenState.paddle1.speed
                elif event.button == constants.joyUp:
                    screenState.paddle1.dy = screenState.paddle1.speed
            else:
                 if event.button == constants.joyDown:
                    screenState.paddle2.dy = -screenState.paddle2.speed
                 elif event.button == constants.joyUp:
                    screenState.paddle2.dy = screenState.paddle2.speed           
            
        elif event.type == pygame.JOYBUTTONUP:
            if event.joy == 0:
                screenState.paddle1.dy = 0
            else:
                screenState.paddle2.dy = 0
                
                
        #Key up event listeners:      
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                screenState.paddle2.dy = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                screenState.paddle1.dy = 0


#Function to detect all the collisions
def detectCollisions(screenState: ScreenState):
    #Detecting all collisions between the ball and the paddle:
    screenState.detectPaddle1Collision()
    screenState.detectPaddle2Collision()
    #Detecting all border collisions between the paddle and the ball:
    screenState.paddle1.border_collision()
    screenState.paddle2.border_collision()
    screenState.ball.border_collision()


#function to update scores
def updateScore(screenState: ScreenState):
    #Changing paddle 1 score:
    if screenState.ball.x >= (constants.screenWidth - screenState.ball.radius):
        int(screenState.paddle1Score.score)
        screenState.paddle1Score.score = screenState.paddle1Score.score + 1
        str(screenState.paddle1Score.score)
        #Moving ball to screen's center 
        screenState.ball.x = constants.cx 
        screenState.ball.y = constants.cy
        #Wait a second
        time.sleep(1)

    #Changing paddle 2 score:
    elif screenState.ball.x <= screenState.ball.radius:
        int(screenState.paddle2Score.score)
        screenState.paddle2Score.score = screenState.paddle2Score.score +  1
        str(screenState.paddle2Score.score)
        #Moving ball to screen's center
        screenState.ball.x = constants.cx
        screenState.ball.y = constants.cy
        #Wait a second
        time.sleep(1)

    #Write score(s):
    screenState.paddle1Score.write()
    screenState.paddle2Score.write()



#This function decides which player wins the game and if the game has ended, based on which player reaches the max-score first:
def hasGameEnded(screenState: ScreenState):
    #Deciding if Player 1 is the winner:
    if screenState.paddle1Score.score == constants.maxScore:
        screenState.winner = "Player 1"
        #Return true if player 1 wins because the game has ended
        return True
    #Deciding if Player 2 is the winner:
    if screenState.paddle2Score.score == constants.maxScore:
        screenState.endScreen_text.color = constants.colors["RED"]
        screenState.winner = "Player 2"
        #Return true if player 2 wins because the game has ended
        return True

    #When both of the above if-statements evaluate to false that means neither player has won, nor has the game ended, so return false:
    return False
