#!/usr/local/bin/python3

import tkinter


# functions which make the input window

class NumPlayer:
    """ this function allows the user to choose the number of players for the game,
    using a slider to give a choice between 2 - 4 players."""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.numPlayer = tkinter.Label(frame, text='Select number of players', fg='black')
        self.numPlayer.pack(fill='both')

        self.play_slide = tkinter.Scale(frame, from_=2, to=4, orient='horizontal', fg='black')
        self.play_slide.pack()


class SetBoard:
    """ this function allows the user to choose the length of the board
    using a slider to give a choice between 15 - 110 tiles.
    (the choice of number of tiles can be changed later)"""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.board_len = tkinter.Label(frame, text='Select board length', fg='black')
        self.board_len.pack()

        self.slide = tkinter.Scale(frame, from_=15, to=110, orient='horizontal', fg='black')
        self.slide.pack()


class SetDifficulty:
    """ this function allows the user to choose the difficulty for the game,
    using a drop-down menu."""

    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()
        self.label = tkinter.Label(frame, text="select a difficulty level", fg='black')
        self.label.pack()
        items = ["Easy", "Medium", "Hard"]

        self.diff = tkinter.StringVar()
        self.diff.set(items[1])
        self.menu = tkinter.OptionMenu(frame, self.diff, *items)
        self.menu.pack(side='top')


class SetDice:
    """ this function allows the user to choose the dice-face,
    using a slider to give a choice between 4 - 12 faces.
    (the choice can be changed later to allow more faces). """

    def __init__(self, master):
        """

        :rtype : int
        """
        frame = tkinter.Frame(master)
        frame.pack()

        self.dice = tkinter.Label(frame, text='Select number of dice faces for your dice', fg='black')
        self.dice.pack()

        self.dice_slide = tkinter.Scale(frame, from_=4, to=12, orient='horizontal', fg='black')
        self.dice_slide.pack()


inputVal = {}


def on_click():
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
    """
    :rtype int, except for difficulty, which returns a str
    :param key: key of inputVal dictionary that you want the value of
    :return: returns the value from the dictionary for the key you typed
    """
    return inputVal[key]


# This runs all the functions and sets off the on_click function once the Submit button is clicked

root = tkinter.Tk()
root.protocol("WM_DELETE_WINDOW", quit)
root.title('The Goose Game Reimagined')
mainLabel = tkinter.Label(root, text='Options:', fg='black')
mainLabel.pack()

num_Player = NumPlayer(root)

set_difficulty = SetDifficulty(root)

set_board = SetBoard(root)

set_dice = SetDice(root)

mainButton = tkinter.Button(root, text='Submit', command=on_click)
mainButton.pack()


root.mainloop()