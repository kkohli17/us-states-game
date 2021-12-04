import turtle 
import pandas as pd 
import csv 


screen = turtle.Screen() 
screen.title('US States Game')

image = 'us_states_game/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)




df = pd.read_csv('us_states_game/50_states.csv')


correct_guesses = []

while len(correct_guesses) < 50: 
    answer_state = screen.textinput(title = f"{len(correct_guesses)}/50 states correct", prompt = "What's a state's name?").title()

    if answer_state in df['state'].values: 
        tim = turtle.Turtle() 
        tim.hideturtle() 
        tim.penup()
        tim.goto(int(df.loc[df['state'] == answer_state,'x']),int(df.loc[df['state'] == answer_state,'y'].iloc[0]))
        #above line is saying go to line where state = answer_state and pull out x and y using iloc = 1 and 2
        tim.write(answer_state,font=('Arial',7)) #can also use the item() function from pandas instead of answer_state
        correct_guesses.append(answer_state)
        score = len(correct_guesses)
    
    if answer_state == 'Exit': 
        tim = turtle.Turtle() 
        tim.hideturtle() 
        tim.penup()
        tim.goto(-50,0)
        tim.write('Game Over', font = ('Arial', 14))
        tim.goto(-130,-50)
        tim.write('Find csv file with missed states in downloaded area', font = ('Arial',10))
        break #this allows you to get out of the loop 



#states_to_learn.csv 
    all_states = df['state'].to_list()
    ungessed_states = []
    for state in all_states: 
        if state not in correct_guesses:
            ungessed_states.append(state)
    new_df = pd.DataFrame(ungessed_states)
    new_df.to_csv('us_states_game/states_not_guessed.csv')
screen.exitonclick() 