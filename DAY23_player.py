from turtle import Turtle,Screen
STARTING_POSITION=(0,-280)#IT WILL SET OUR TURTLE TO BOTTOM-CENTER POSITION OF THE SCREEN
MOVE_DISTANCE=10
FINISH_LINE_Y=280

#HERE OUR PLAYER CLASS IN INHERITING FROM TURTLE CLASS
class Player(Turtle):
    #SET THE TURTLE
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.go_to_start()
        
    #MOVE_UP FUNCTION WILL MOVE TURTLE TO THE NORTH BY 10 UNITS   
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

        
