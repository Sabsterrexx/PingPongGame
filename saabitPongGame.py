#Saabit Ping Pong Game (Main File)
#2019-10-06
#Extras Include:
#Start Screen
#End Screen (with restart option)
#Difficulty levels (ball changes speed, ball and paddles get smaller)
#Ball changing color upon collision with paddle(s)
#Paddle's movement also controlled via joysticks using the Raspberry Pi 3


#Import all the required screen modules into the main file:
from screenState import ScreenState
import initGame
import startScreen 
import gameScreen
import endGame

#Main game loop for all game screens
while True:
    #Inititalize everything
    screenState = initGame.init()
    #Draw Start screen
    startScreen.show(screenState)
    #Draw game screen
    gameScreen.show(screenState)
    #End screen
    endGame.show(screenState)