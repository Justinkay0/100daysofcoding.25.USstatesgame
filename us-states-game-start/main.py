import turtle
import pandas as pd


def get_xy(state, df):
    data = df[df['state'] == state]
    data = data.iloc[0, 1:].values
    return data


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv('50_states.csv')
states = df['state'].to_list()
num_country = 0
country_done = []
max_country = len(states)
answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name")
while num_country < max_country:
    answer_state = answer_state.title()

    if answer_state == 'Exit':
        break

    if answer_state in states and answer_state not in country_done:
        cord = get_xy(answer_state, df)
        freedom = turtle.Turtle()
        freedom.hideturtle()
        freedom.penup()
        freedom.setposition(cord)
        freedom.write(arg=answer_state)
        country_done.append(answer_state)
        num_country += 1
    answer_state = screen.textinput(title=f'{num_country}/{max_country} States correct',\
                                    prompt="What's another state's name")


learn_states = []
for i in states:
    if i not in country_done:
        learn_states.append(i)
learn_states = pd.DataFrame(learn_states,columns=['states'])
learn_states.to_csv('states_to_learn.csv')
