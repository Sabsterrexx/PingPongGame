The main code file of this program is "saabitPongGame.py", everything is run from there so if you would like to see all the code in this file in action, simply run that one file.

Please keep all python files relating to this project in the same directory. 

Do not move or delete any files in this directory unless you clearly know what you are doing, or else the game will not work.                

------------------------------------------------------------------------------------------------------------------------


The joystick branch of this project allows the 2 paddles to be controlled by a PS3 controller as well as the keyboard's keys. It also adresses a few glitches that were present in the master branch of this project. Nonetheless, the basic code structure remains the same, like so:


The basic code structure is that everything in the game is by classes, similar to how Java programs work. Infact, even the start screen, game screen and the end screen are all classes. All components seen in the games are also merely objects based off of classes, including the score boards, paddles, titles, and ball. 

Most of the code files however, all depend on the "screenState.py" file. This file essentially consists of a class called "ScreenState" which basically makes all the objects created in the game equal to an attribute of itself.

As a result, most functions inside the screen files contain this parameter: "(screenState: ScreenState)" .

This parameter basically states that whatever variable is passed in the parameter, it will create an object based off of the "ScreenState" class, which is then referred to in the function.

Tha main file only uses the start screen, game and end screen class files to generate the game. 

These files in turn are built off of the "initGame.py" file and it's "init()" function, which in turn is built off of the "screenState.py" file and it's "ScreenState" class. The "screenState.py" file is then built off of the "ball", "paddle", "score" and "text" classes and files. These files are in turn built off of the "constants.py" file.