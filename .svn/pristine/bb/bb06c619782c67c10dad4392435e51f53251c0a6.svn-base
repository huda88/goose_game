#!/usr/local/bin/python3

import tkinter



# -----------------------------------------------------input window-----------------------------------------------------
# TODO: link board GUI and control to the submit window
# TODO: make input window less ugly
class num_Player:
    """ this function allows the user to choose the number of players for the game,
    using a slider to give a choice between 1 - 4 players."""

    # FIXME: change from slider to radiobuttons

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.numPlayer = tkinter.Label(frame, text='Select number of players', fg='black')
        self.numPlayer.pack(fill='both')

        self.play_slide = tkinter.Scale(frame, from_=2, to=4, orient='horizontal', fg='black')
        self.play_slide.pack()


class set_board:
    """ this function allows the user to choose the length of the board
    using a slider to give a choice between 15 - 115 tiles.
    (the choice of number of tiles can be changed later)"""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.boardlen = tkinter.Label(frame, text='Select board length', fg='black')
        self.boardlen.pack()

        self.slide = tkinter.Scale(frame, from_=15, to=110, orient='horizontal', fg='black')
        self.slide.pack()


class set_difficulty:
    """ this function allows the user to choose the difficulty for the game,
    using a drop-menu."""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.label = tkinter.Label(frame, text='select a difficulty level', fg='black')
        self.label.pack()
        items = ["Easy", "Medium", "Hard"]

        self.diff = tkinter.StringVar()
        self.diff.set(items[1])
        self.menu = tkinter.OptionMenu(frame, self.diff, *items)
        self.menu.pack(side='top')


class set_dice:
    """ this function allows the user to choose the dice-face,
    using a slider to give a choice between 4 - 12 faces.
    (the choice can be changed later to allow more faces). """

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.dice = tkinter.Label(frame, text='Select the number of dice faces u wanna play with', fg='black')
        self.dice.pack()

        self.dice_slide = tkinter.Scale(frame, from_=4, to=12, orient='horizontal', fg='black')
        self.dice_slide.pack()


inputVal = {}


def onClick():
    """ this function adds the values of the choices from the input window
    to a dictionary for the control to use to create the game, and the visual to generate the GUI.
    The function is set off when the submit button is clicked in the input window and
    the after returning the values of the inputs, this function quits the input window. """

    inputVal['number of players'] = num_Player.play_slide.get()
    inputVal['difficulty'] = set_difficulty.diff.get()
    inputVal['board length'] = set_board.slide.get()
    inputVal['dice'] = set_dice.dice_slide.get()
    root.destroy()


def input_data(key):
    '''
    :param key: key of inputVal dictionary that you want the value of
    :return: returns the value from the dictionary for the key you typed
    '''
    return inputVal[key]


# This runs all the functions and sets off the onClick function once the Submit button is clicked

root = tkinter.Tk()

mainLabel = tkinter.Label(root, text='The Goose Game', fg='black')
mainLabel.pack()

num_Player = num_Player(root)

set_difficulty = set_difficulty(root)

set_board = set_board(root)

set_dice = set_dice(root)

mainButton = tkinter.Button(root, text='Submit', command=onClick)
mainButton.pack()

root.mainloop()

print(input_data('dice'))
print(input_data('board length'))
print(input_data('difficulty'))
print(input_data('number of players'))
print(inputVal)