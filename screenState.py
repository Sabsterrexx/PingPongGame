#Screen State class


#This class is basically designed to handle the creation of all the objects, and a few other variables, more effectively: 
class ScreenState:
    def __init__(self, screen, title_text, endScreen_text, paddle1, paddle2, ball, paddle1Score, paddle2Score, clock, FPS):
        self.screen = screen
        self.title_text = title_text
        self.endScreen_text = endScreen_text
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.ball = ball
        self.paddle1Score = paddle1Score
        self.paddle2Score = paddle2Score
        self.clock = clock
        self.FPS = FPS
        self.winner = " "



    #ball collision with paddle 1:
    def detectPaddle1Collision(self):  
        ball = self.ball
        paddle1 = self.paddle1
        if ball.x - ball.radius < paddle1.x + paddle1.width and ball.y > paddle1.y and ball.y < paddle1.y + paddle1.height:
            ball.dx = -ball.dx
            #change ball's color to paddle 1's color:
            ball.change_color(paddle1.color)


    #ball collision with paddle 2:
    def detectPaddle2Collision(self):  
        ball = self.ball
        paddle2 = self.paddle2
        if ball.x + ball.radius >= paddle2.x and ball.y >= paddle2.y and ball.y < paddle2.y + paddle2.height:
            ball.dx = -ball.dx
            #change ball's color to paddle 2's color:
            ball.change_color(paddle2.color)