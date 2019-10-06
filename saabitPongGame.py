#Saabit Ping Pong Game (Main File)
#2019-10-04
#Extras Include:
#Start Screen
#End Screen
#Difficulty levels (ball changes speed, ball and paddles get smaller)
#Ball changing color upon collision with paddle(s)


#Import all the required screen modules into the main file:
from screenState import ScreenState
import initGame
import startScreen 
import gameScreen
import endGame

#Main drawing loop
while True:
    #Inititalize everything
    screenState = initGame.init()
    #Draw Start screen
    startScreen.show(screenState)
    #Draw game screen
    gameScreen.show(screenState)
    #End screen
    endGame.show(screenState)