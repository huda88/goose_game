#!/usr/local/bin/python3

import tkinter
from PIL import Image, ImageTk
import random

# window = tkinter.Tk()
# picture = ImageTk.PhotoImage(Image.open("wp.jpg").resize((1400, 830)))
# canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
# Canvas_Image = canvas.create_image(0, 0, image=picture, anchor="nw")
# canvas.pack()
board = {}


def color_generator():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    r = hex((red + 128) // 2)
    g = hex((green + 128) // 2)
    b = hex((blue + 128) // 2)
    rgb = '#' + r[2:] + g[2:] + b[2:]
    return rgb

class num_Player:
    """ this function allows the user to choose the number of players for the game,
    using a slider to give a choice between 1 - 4 players."""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.numPlayer = tkinter.Label(frame, text='Select number of players', fg='blue')
        self.numPlayer.pack(fill='both')

        self.play_slide = tkinter.Scale(frame, from_=1, to=4, orient='horizontal', fg='blue')
        self.play_slide.pack()

class SetBoard:
    def __init__(self):
        window = tkinter.Tk()
        # picture = ImageTk.PhotoImage(Image.open("wp.jpg").resize((1400, 830)))
        SetBoard.canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
        # Canvas_Image = canvas.create_image(0, 0, image=picture, anchor="nw")
        SetBoard.canvas.pack()
        window.mainloop()

    def print_board(self, length):
        global board
        global canvas
        board[0] = self.canvas.create_rectangle(570, 380, 630, 440, fill="#222222", outline='', tag='cell')
        c = canvas.coords(board[0])
        count = 1
        k = 0
        while True:
            for i in range((k * 4) + 2):
                board[count] = self.create_rectangle(
                    c[0] + (i + 1) * 60, c[1], c[2] + (i + 1) * 60, c[3], fill=color_generator(), outline='', tag='cell')
                nc = master.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 2):
                board[count] = master.create_rectangle(
                    nc[0], nc[1] - (i + 1) * 60, nc[2], nc[3] - (1 + i) * 60, fill=color_generator(), outline='',
                    tag='cell')
                c = master.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 4):
                board[count] = master.create_rectangle(
                    c[0] - (i + 1) * 60, c[1], c[2] - (i + 1) * 60, c[3], fill=color_generator(), outline='', tag='cell')
                nc = master.coords(board[count])
                count += 1
                if count >= length:
                    return
            for i in range((k * 4) + 4):
                board[count] = master.create_rectangle(
                    nc[0], nc[1] + (i + 1) * 60, nc[2], nc[3] + (1 + i) * 60, fill=color_generator(), outline='',
                    tag='cell')
                c = master.coords(board[count])
                count += 1
                if count >= length:
                    return
            k += 1
    def sidebar(self, master):
        global bar
        bar.append(master.create_rectangle(1200, 0, 1410, 830, fill="#222222", outline=''))
        bar.append(master.create_text(1370, 90, text="dice: 6", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='dice'))
        bar.append(master.create_text(1370, 190, text="turn: 4", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='turn'))
        bar.append(master.create_text(1370, 290, text="♡♡♡", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='health'))
        bar.append(master.create_text(1370, 490, text="Roll", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='roll'))
        bar.append(master.create_text(1370, 590, text="Save", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='save'))
        bar.append(master.create_text(1370, 690, text="Load", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='load'))
        bar.append(master.create_text(1370, 790, text="Quit", font=('Helvetica Neue UltraLight', 45),
                                      fill="white", anchor='se', tag='quit'))

players = {}

def make_players(player_no, current_tile):
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
    canvas.pack()
    global players
    for player in range(player_no):
        players = {player: [current_tile, canvas.create_text(580, 380, text='웃', font=('Helvetica Neue UltraLight', 40),
                                        fill="white", anchor='nw', tag='effect_text')]}
    return players


# TODO ☠


def move_player(player_no, diceval):
    global player
    current_tile = (player[player_no][0])
    new_tile = current_tile + diceval
    old_pos = canvas.coords(board[current_tile])
    position = canvas.coords(board[new_tile])

    canvas.move(player[player_no][1], (position[0] - old_pos[0]), (position[1] -old_pos[1]))
    player[player_no][0] = new_tile
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
    for i in range(22):
        for element in range(4):
            canvas.move(slide[element], x, 0)
            x += 1
        canvas.after(10)
        canvas.update()


def move_out(event):
    x = 0
    for i in range(30):
        for element in range(4):
            canvas.move(slide[element], x, 0)
            x += 1
        canvas.after(10)
        canvas.update()


slide = []


def slide_event(string, option0, option1):
    global slide
    slide.append(canvas.create_rectangle(-510, 200, -10, 600, fill="#222222", tag='effect'))
    slide.append(canvas.create_text(-490, 245, text=string, justify=tkinter.LEFT, width='420',
                                    font=('Helvetica Neue UltraLight', 20), fill="white", anchor='nw',
                                    tag='effect_text'))
    slide.append(canvas.create_text(-490, 500, text=option0, width='420', font=('Helvetica Neue UltraLight', 20),
                                    fill="white", anchor='nw', tag='choice_a'))
    slide.append(canvas.create_text(-215, 500, text=option1, font=('Helvetica Neue UltraLight', 20), fill="white",
                                    anchor='nw', tag='choice_b'))
    for element in slide:
        canvas.tag_raise(element)
    move_in('event')


def choice(option0, option1):
    global slide
    slide_event("choose either A or B", option0, option1)
    if canvas.tag_bind('choice_a', '<Double-1>', move_out):
        return 0
    elif canvas.tag_bind('choice_b', '<Double-1>', move_out):
        return 1
    slide = []


bar = []


def sidebar():
    global bar
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=1400, height=820, bg="#666666")
    canvas.pack()
    bar.append(canvas.create_rectangle(1200, 0, 1410, 830, fill="#222222", outline=''))
    bar.append(canvas.create_text(1370, 90, text="dice: 6", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='dice'))
    bar.append(canvas.create_text(1370, 190, text="turn: 4", font=('Helvetica Neue UltraLight', 45),
                                  fill="white", anchor='se', tag='turn'))
    bar.append(canvas.create_text(1370, 290, text="♡♡♡", font=('Helvetica Neue UltraLight', 45),
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
    bar[1] = canvas.create_text(1370, 90, text="dice: " + result, font=('Helvetica Neue UltraLight', 45),
                                fill="white", anchor='se', tag='dice')


def save(event):
    print('save')


def load(event):
    print('load')


def roll(event):
    print('roll')


s = 'lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem'

# window = tkinter.Tk()
SetBoard().print_board(100)
# window.mainloop()

# canvas.tag_bind('roll', '<Double-1>', roll)
# canvas.tag_bind('save', '<Double-1>', save)
# canvas.tag_bind('load', '<Double-1>', load)
# canvas.tag_bind('quit', '<Double-1>', quit)