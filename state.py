from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def write_state(self,state, x, y):
        self.goto(x,y)
        self.write(state.capitalize())
        
    
    