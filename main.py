import pandas as pd
from turtle import Turtle, Screen
import turtle

t= Turtle()
t.penup()
t.hideturtle()
screen = Screen()
screen.setup(height=500, width=750)
screen.bgpic('blank_states_img.gif')
data=pd.read_csv('50_states.csv')

us_states=data.state.to_list()

state_known=[]

while len(state_known)<=50:
    state_input = screen.textinput(f"{len(state_known)}/50 states", "indentify next us state").title()
    if state_input=="Exit":
        break
    elif state_input in us_states:
        state_known.append(state_input)
        us_states.remove(state_input)
        x_axis = data[data['state'] == state_input]['x'].values[0]
        y_axis = data[data['state'] == state_input]['y'].values[0]
        t.goto(x_axis,y_axis)
        t.write(state_input, False,'center')
dictionary= {
    'state':us_states
}
learn = pd.DataFrame(dictionary)
learn.to_csv('state_to_learn.csv')
screen.bye()
