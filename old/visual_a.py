#!/usr/local/bin/python3

import tkinter
import random
import time

window = tkinter.Tk()
picture = tkinter.PhotoImage(file="wp.gif")
canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
Canvas_Image = canvas.create_image(0, 0, image=picture, anchor="nw")
canvas.pack()
board = {}
choices = {'a': 0, 'b':0}

def color_generator(model_board):
    color_effect = {'step': '#5AB440', 'health': '#620A0A', 'goto_p': '#D9E748', 'turn_mod' :'#7E5DD9', 'goto_t': '#2E9E9C', 'dice_mod': '#C0335F', 'none': '#252630'}
    board_colors = {}
    for key in model_board:
        if model_board[key][0] == 'step':
            board_colors[key] = color_effect['step']
        elif model_board[key][0] == 'health':
            board_colors[key] = color_effect['health']
        elif model_board[key][0] == 'goto_p':
            board_colors[key] = color_effect['goto_p']
        elif model_board[key][0] == 'turn_mod':
            board_colors[key] = color_effect['turn_mod']
        elif model_board[key][0] == 'goto_t':
            board_colors[key] = color_effect['goto_t']
        elif model_board[key][0] == 'dice_mod':
            board_colors[key] = color_effect['dice_mod']
        elif model_board[key][0] == 'none':
            board_colors[key] = color_effect['none']
    return board_colors


counter = 0

def print_board(model_board):
    length = len(model_board)
    board_colors = color_generator(model_board)
    global board
    global counter
    # window = tkinter.Tk()
    # # picture = ImageTk.PhotoImage(Image.open("wp.jpg").resize((1400, 830)))
    # canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
    # # Canvas_Image = canvas.create_image(0, 0, image=picture, anchor="nw")
    # canvas.pack()
    if counter != 0:
        board[0] = canvas.create_rectangle(570, 380, 630, 440, fill="#222222", tag='cell')
        c = canvas.coords(board[0])
        count = 1
        k = 0
        while True:
            for i in range((k * 4) + 2):
                board[count] = canvas.create_rectangle(
                    c[0] + (i + 1) * 60, c[1], c[2] + (i + 1) * 60, c[3], fill=board_colors[count], tag='cell')
                nc = canvas.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 2):
                board[count] = canvas.create_rectangle(
                    nc[0], nc[1] - (i + 1) * 60, nc[2], nc[3] - (1 + i) * 60, fill=board_colors[count],
                    tag='cell')
                c = canvas.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 4):
                board[count] = canvas.create_rectangle(
                    c[0] - (i + 1) * 60, c[1], c[2] - (i + 1) * 60, c[3], fill=board_colors[count], tag='cell')
                nc = canvas.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 4):
                board[count] = canvas.create_rectangle(
                    nc[0], nc[1] + (i + 1) * 60, nc[2], nc[3] + (1 + i) * 60, fill=board_colors[count],
                    tag='cell')
                c = canvas.coords(board[count])
                count += 1
                if count >= length:
                    return
            k += 1

players = {}


def make_players(player_no, current_tile):
    global counter
    global players
    if counter != 0:
        pawns = ['♨','☃','⚛','✎','☺','웃']
        for player in range(player_no):
            the_player = player + 1
            players[the_player] = [current_tile, canvas.create_text(580 + 5 * the_player, 380 + 5 * the_player, text=pawns[player], font=('Helvetica Neue UltraLight', 40),
                                            fill='white', anchor='nw', tag='effect_text')]
        print('k', players)
    counter = 1
    idle()
    return players

super_slide = ['', '']

def activated_effect(s):
    global super_slide
    super_slide[0] = canvas.create_rectangle(-490, 200, 10, 300, fill="#222222", tag='box')
    super_slide[1] = canvas.create_text(-240, 250, text=s, width='420',
                                    font=('Helvetica Neue UltraLight', 20), fill="white", anchor='center',
                                    tag='box_text')
    for element in slide:
        canvas.tag_raise(element)
    move_in_effect()
    time.sleep(0.8)
    move_out_effect()


def idle():
    canvas.tag_bind('roll', '<Button-1>', roll)
    canvas.tag_bind('save', '<Button-1>', save)
    canvas.tag_bind('load', '<Button-1>', load)
    canvas.tag_bind('quit', '<Button-1>', quit)
    window.mainloop()



# TODO ☠


# def move_player(player_no, diceval):
#     global player
#     current_tile = (player[player_no][0])
#     new_tile = current_tile + diceval
#     old_pos = canvas.coords(board[current_tile])
#     position = canvas.coords(board[new_tile])
#
#     canvas.move(player[player_no][1], (position[0] - old_pos[0]), (position[1] -old_pos[1]))
#     player[player_no][0] = new_tile
#     canvas.after(10)
#     canvas.update()

def move_player2(player_no, pos):
    global players
    print (players, player_no)
    current_tile = (players[player_no][0])
    new_tile = pos
    old_pos = canvas.coords(board[current_tile])
    position = canvas.coords(board[new_tile])

    canvas.move(players[player_no][1], (position[0] - old_pos[0]), (position[1] - old_pos[1]))
    players[player_no][0] = new_tile
    canvas.after(10)
    canvas.update()


def color_tile(tile):
    # FIXME there should be a third dictionary; number:position, number:effect and effect:color
    dictio_board = {1: '#D53B81', 2: '#7D156A', 3: '#DF6422', 4: '#845946', 5: '#1B498A', 6: '#5B528E',
                    7: '#059239', 8: '#B7D14D', 9: '#B7D14D', 10: '#B7D14D', 11: '#006AAC', 12: '#5CAC35',
                    13: '#CD0927', 14: '#009E8D', 15: '#F5BC1C'}
    if tile in dictio_board:
        return dictio_board[tile]


def move_in(event):
    x = 0
    for i in range(21):
        for element in range(4):
            canvas.move(slide[element], x, 0)
        x -= 1
        canvas.after(10)
        canvas.update()

def move_in_effect():
    x = 0
    for i in range(30):
        for element in range(2):
            canvas.move(super_slide[element], x, 0)
        x += 2
        canvas.after(10)
        canvas.update()

def move_out_effect():
    x = 0
    for i in range(40):
        for element in range(2):
            canvas.move(super_slide[element], x, 0)
        x += 2
        canvas.after(10)
        canvas.update()


def move_out_a(event):
    global choices
    x = 0
    for i in range(30):
        for element in range(4):
            canvas.move(slide[element], x, 0)
        x += 1
        canvas.after(10)
        canvas.update()
    choices['a'] = 1
    canvas.quit()
    return

def move_out_b(event):
    global choices
    x = 0
    for i in range(30):
        for element in range(4):
            canvas.move(slide[element], x, 0)
        x += 1
        canvas.after(10)
        canvas.update()
    choices['b'] = 1
    canvas.quit()
    return

def win_box_move():
    x = 0
    for i in range(30):
        for element in range(2):
            canvas.move(win_slide[element], x, 0)
        x += 2
        canvas.after(2)
        canvas.update()

slide = ['', '', '', '']


def slide_event(string, option0, option1):
    global slide
    slide[0] = canvas.create_rectangle(1410, 410, 1620, 710, fill="#222222", tag='box')
    slide[1] = canvas.create_text(1430, 430, text=string, justify=tkinter.LEFT, width='420',
                                    font=('Helvetica Neue UltraLight', 20), fill="white", anchor='nw',
                                    tag='box_text')
    slide[2] = canvas.create_text(1430, 550, text=option0, width='420', font=('Helvetica Neue UltraLight', 20),
                                    fill="white", anchor='nw', tag='choice_a')
    slide[3] = canvas.create_text(1430, 600, text=option1, font=('Helvetica Neue UltraLight', 20), fill="white",
                                    anchor='nw', tag='choice_b')
    for element in slide:
        canvas.tag_raise(element)
    move_in('event')

win_slide = ['', '']

def win_effect(current_p):
    global win_slide
    win_slide[0] = canvas.create_rectangle(-500, 200, 10, 300, fill="#002D40", tag='box')
    win_slide[1] = canvas.create_text(-250, 250, text='The winner is Player{0}'.format(str(current_p)), width='420',
                                    font=('Helvetica Neue UltraLight', 30), fill="#FFBF44", anchor='center',
                                    tag='box_text')
    for element in slide:
        canvas.tag_raise(element)
    win_box_move()

choices = {'a': 0, 'b':0}

def choice(option0, option1):
    global choices
    global slide
    print(choices, 'k')
    slide_event("choose either A or B", option0, option1)
    canvas.tag_bind('choice_a', '<Button-1>', move_out_b)
    canvas.tag_bind('choice_b', '<Button-1>', move_out_a)
    while choices['a'] == 0 and choices['b'] == 0:
        canvas.mainloop()
    print(choices, 'kk')
    canvas.delete('box', 'box_text', 'choice_a', 'choice_b')
    a, b = choices['a'], choices['b']
    choices['a'] = 0
    choices['b'] = 0
    return a, b


bar = []

def create_hide_roll():
    canvas.create_text(1370, 490, text="Roll", font=('Helvetica Neue UltraLight', 45), fill="white", anchor='se', tag='hide_roll')
    canvas.tag_raise('hide_roll')


def delete_hide_roll():
    canvas.delete("hide_roll")



def sidebar():
    global bar
    bar.append(canvas.create_rectangle(1200, 0, 1410, 830, fill="#222222", outline=''))
    bar.append(canvas.create_text(1370, 90, text="dice: ", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='dice'))
    bar.append(canvas.create_text(1370, 190, text="turn: ", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='turn'))
    bar.append(canvas.create_text(1370, 290, text="hp: ", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='health'))
    bar.append(canvas.create_text(1370, 490, text="Roll", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='roll'))
    bar.append(canvas.create_text(1370, 590, text="Save", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='save'))
    bar.append(canvas.create_text(1370, 690, text="Load", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='load'))
    bar.append(canvas.create_text(1370, 790, text="Quit", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='quit'))


def print_dice(result):
    global bar
    print(bar[1])
    canvas.delete("dice")
    bar.append(canvas.create_text(1370, 90, text="dice: " + str(result), font=('Helvetica Neue UltraLight', 45),
                                fill="white", anchor='se', tag='dice'))


def print_turn(player):
    global bar
    canvas.delete("turn")
    bar.append(canvas.create_text(1370, 190, text="turn: " + str(player), font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='turn'))

def print_health(player):
    global bar
    health = player[3]
    canvas.delete("health")
    bar.append(canvas.create_text(1370, 290, text="hp: " + str(health), font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='health'))

def print_move(players, player):
    this_player = players[player]
    position = this_player[0]
    move_player2(player, position)


# def set(players, player):
#     print('a')
#     print(player)
#     print('b')
#     this_player = players[player]
#     position = this_player[0]
#     health = this_player [-1]
#     # canvas.delete("dice")
#     # bar.append(canvas.create_text(1370, 90, text="dice: " + str(dice), font=('Helvetica Neue UltraLight', 45),
#     #                             fill="white", anchor='se', tag='dice'))
#
#     canvas.delete("health")
#     bar.append(canvas.create_text(1370, 290, text="hp: " + str(health), font=('Helvetica Neue UltraLight', 45),
#                                   fill="white", anchor='se', tag='health'))
#     move_player2(player, position)


#TODO ♡♡♡


def save(event):
    print('save')


def load(event):
    print('load')


def roll(event):
    import controlTest_paolo
    import model
    controlTest_paolo.turn_handler()


s = 'lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem'


# canvas.tag_bind('roll', '<Double-1>', roll)
# canvas.tag_bind('save', '<Double-1>', save)
# canvas.tag_bind('load', '<Double-1>', load)
# canvas.tag_bind('quit', '<Double-1>', quit)