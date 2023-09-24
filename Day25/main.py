import pandas as p
import turtle as t

screen = t.Screen()
screen.title('U.S. States Game')
screen.setup(725, 550)
screen.bgcolor("#000000")
image = './blank_states_img.gif'
screen.addshape(image)  # 725-491

screen_writer = t.Turtle()
screen_writer.hideturtle()
screen_writer.penup()
screen_writer.speed(0)
screen_writer.color("#00FF00")

OFFSET = -20
bg = t.Turtle(image)
bg.penup()
bg.setpos(0, OFFSET)

states_data = p.read_csv('./50_states.csv')
states_to_guess = states_data.state.to_list()


def write_state(state_name, color):
    state_info = states_data[states_data.state == state_name]
    x = state_info.x.item()
    y = state_info.y.item() + OFFSET
    screen_writer.setpos(x, y)
    screen_writer.color(color)
    screen_writer.write(state_name, False, 'center', ('Consolas', 10, 'bold'))


while states_to_guess:
    try:
        answer_state = screen.textinput(f'{50 - len(states_to_guess)}/50',
                                        "What's another state's name? (Cancel to finish)").title()
        if answer_state in states_to_guess:
            write_state(answer_state, "#00FF00")
            states_to_guess.remove(answer_state)
    except AttributeError:
        break

screen_writer.setpos(-352.5, 235)
screen_writer.color("#FFFFFF")
screen_writer.write(f'Final Score: {50 - len(states_to_guess)}/50', False, 'left', ('Consolas', 25, 'bold'))
screen_writer.setpos(345, 235)
screen_writer.color("#FF0000")
screen_writer.write('Exit ↑', False, 'right', ('Consolas', 25, 'bold'))

for state in states_to_guess:
    write_state(state, "#FF0000")

states_to_learn = p.DataFrame(states_data[states_data['state'].isin(states_to_guess)])
states_to_learn.to_csv('./states_to_learn.csv')

screen.mainloop()
