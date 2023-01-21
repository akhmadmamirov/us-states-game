#Author: Akhmadillo Mamirov
#Purpose: Us States Game
#Last Modified: January. 20, 2023

import turtle 
import numpy as np
from state import State

screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
make_state = State()


# Load CSV data into a NumPy array
data = np.genfromtxt('50_states.csv', delimiter=',', dtype=str)

# Use array slicing to get the first column and the rest of the columns
keys = data[:, 0]
values = data[:, 1:]

# Create a dictionary with the first column as the keys and the rest of the columns as the values in an array
my_dict = {keys[i].lower(): values[i] for i in range(1,len(keys))}

found_states = 0
found_list = []
#checking
game_on = True
while game_on:
    
    answer_state = screen.textinput(f"Found States:{found_states}/50", "What's the another state's name?")
    state = answer_state.lower()
    if answer_state == "exit":
        break
        
    if  state in my_dict and state not in found_list:
        #getting x and y coordinates
        x,y  = my_dict[state]
        #writing states
        make_state.write_state(state, int(x), int(y))
        found_list.append(state)
        found_states += 1 
        
    if found_states == 50:
        turtle.write("You Won. Congratulations!", align="center", font=("Cooper Black", 35, "bold"))
        game_on = False
                

states_to_learn = []

for state in my_dict:
    if state  not in found_list:
        states_to_learn.append(state)

np.savetxt("states_to_learn.csv", states_to_learn, delimiter=",", fmt="%s")


