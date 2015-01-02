#!/usr/local/bin/python3

# Interface for functions that go from model to visual

import model
import random
import copy
import visual_options
import visual
import time
import json

# ---------------- Functions that interact with model ------------------- #


# check if some one has win
def check_win(length, players, current_player):
    if players[current_player][0] == length:
        return True
    else:
        return False


# change the current user
def current_player_generator(now, n_players):
    if now < n_players:
        now += 1
    else:
        now = 1
    return now


current_p = 1

# Main to generate the game


def game_generator():
    global current_p
    level, dice, length, n_players = ask_for_info()
    effect_list = ['step', 'health', 'goto_p', 'turn_mod', 'goto_t', 'dice_mod']
    current_p = 1
    model.board_generator(length, dice, effect_list, level)
    model.player_generator(n_players, dice)
    setup(model.board, n_players, model.players, current_p)



dice_counter = 0

# Dice roller
def roll_dice(dice):
    global dice_counter
    # result = random.randint(dice[0], dice[1])
    if dice_counter == 0:
        result = 4
    elif dice_counter == 1:
        result = 6
    elif dice_counter == 2:
        result = 3
    elif dice_counter == 3:
        result = 5
    elif dice_counter == 4:
        result = 2
    elif dice_counter == 5:
        result = 2
    elif dice_counter == 6:
        result = 6
    elif dice_counter == 7:
        result = 4
    elif dice_counter == 8:
        result = 5
    elif dice_counter == 9:
        result = 1
    elif dice_counter == 10:
        result = 2
    elif dice_counter == 11:
        result = 5
    elif dice_counter == 12:
        result = 4
    elif dice_counter == 13:
        result = 3
    elif dice_counter == 14:
        result = 2
    elif dice_counter == 15:
        result = 1
    elif dice_counter == 16:
        result = 3
    elif dice_counter == 17:
        result = 2
    elif dice_counter == 18:
        result = 1
    elif dice_counter == 19:
        result = 3
    elif dice_counter == 20:
        result = 4
    elif dice_counter == 21:
        result = 5
    elif dice_counter == 22:
        result = 2
    elif dice_counter == 23:
        result = 4
    elif dice_counter == 24:
        result = 6
    elif dice_counter == 25:
        result = 2
    elif dice_counter == 26:
        result = 4
    elif dice_counter == 27:
        result = 1
    elif dice_counter == 28:
        result = 2
    else:
        result = random.randint(dice[0], dice[1])
    display_dice(result)
    print(dice_counter)
    dice_counter += 1
    return result


# Checks and executes the tile effect
def tile_effect(players, current_player, board):
    position = players[current_player][0]
    if 'none' in board[position]:
        return

    elif 'step' in board[position] and board[position][1] < 0:
        if ask_for_choice('Step back by {0} tile(s)'.format(board[position][1] * -1),
                          'Lose {0} health'.format(board[position][1] * 5 * -1)):
            (model.step(current_p, board[position][1], False))
            visual.activated_effect(
                'Oh noo! You have to go back to help your friends! You step back by {0} tile(s).'.format(
                    board[position][1] * -1))
        else:
            (model.step(current_p, board[position][1], True))
            visual.activated_effect('You got hurt! You lost {0} health.'.format(board[position][1] * 5 * -1))

    elif 'step' in board[position] and board[position][1] > 0:
        if ask_for_choice('Step forward by {0} tile(s)'.format(board[position][1]),
                          'Gain {0} health'.format(board[position][1] * 5)):
            (model.step(current_p, board[position][1], False))
            visual.activated_effect(
                'Great! You go farther than you thought! Continue like that! You step forward by {0} tile(s).'.format(
                    board[position][1]))
        else:
            (model.step(current_p, board[position][1], True))
            visual.activated_effect(
                'Lucky you! You found a potion, you gain {0} health.'.format(board[position][1] * 5))

    elif 'turn_mod' in board[position] and board[position][1] < 0:
        if ask_for_choice('Skip {0} turn(s)'.format(board[position][1] * -1),
                          'Lose {0} health'.format(board[position][1] * 20 * -1)):
            (model.turn_mod(current_p, board[position][1], False))
            visual.activated_effect(
                'You walk into quicksands! It will take time to get out, you skip {0} turn(s).'.format(
                    board[position][1] * -1))
        else:
            (model.turn_mod(current_p, board[position][1], True))
            visual.activated_effect('You have to climb a mountain, it takes energy. You lose {0} health.'.format(
                board[position][1] * 20 * -1))

    elif 'turn_mod' in board[position] and board[position][1] > 0:
        if ask_for_choice('Gain {0} turn(s)'.format(board[position][1]),
                          'Gain {0} health'.format(board[position][1] * 20)):
            (model.turn_mod(current_p, board[position][1], False))
            visual.activated_effect(
                'You found a skateboard. You gain {0} turn(s) by riding it!'.format(board[position][1]))
        else:
            (model.turn_mod(current_p, board[position][1], True))
            visual.activated_effect(
                'You find a meadow where you can relax, you gain {0} health.'.format(board[position][1] * 20))

    elif 'goto_p' in board[position]:
        (model.goto_p(current_p))
        visual.activated_effect("Some strange magic teleports to another player, you don't like them much.")

    elif 'goto_t' in board[position]:
        (model.goto_t(current_p, board[position][1]))
        visual.activated_effect('You are teleported to tile {0} by an ancient spell.'.format(board[position][1]))

    elif 'dice_mod' in board[position]:
        (model.dice_mod(current_p, board[position][1], board[position][2], board[position][3]))
        visual.activated_effect('You ate a strange fruit, it seems that your dice is acting weird,'
                                'though it should wore off in {0} turn(s).'.format(board[position][3]))

    elif 'health' in board[position]:
        (model.health(current_p, board[position][1]))
        if board[position][1] < 0:
            visual.activated_effect('Ouch! You got hurt! You lose {0} health.'.format(board[position][1] * -1))
        else:
            visual.activated_effect('Great! A hot meal! Eat and gain {0} health.'.format(board[position][1]))

    return


# Swap players for new turn, and sets it up
def turn_handler():
    global current_p
    visual.print_turn(current_p)
    visual.print_health(model.players[current_p])
    turn(model.players, current_p, model.board)
    if check_win(len(model.board) - 1, model.players, current_p):
        display_winner(current_p)
    if not model.check_for_more(model.players[current_p]):
        current_p = current_player_generator(current_p, len(model.players)-1)
    visual.print_turn(current_p)
    visual.print_health(model.players[current_p])


# A single turn structure
def turn(players, current_player, board):
    # Turn setup
    visual.print_turn(current_player)
    visual.print_health(players[current_player])
    if model.check_for_skip(players[current_player]):
        model.effect_expire(current_player)
        visual.activated_effect('Player {0} skips a turn!'.format(current_player))
        return
    model.effect_expire(current_player)

    # First move
    steps = roll_dice(players[current_player][1])
    reverse = False
    for i in range(steps):
        if not reverse:
            players[current_player][0] += 1
            visual.print_move(players, current_player)
            if players[current_player][0] == len(board) - 1:
                reverse = True
            time.sleep(.025)
        else:
            players[current_p][0] -= 1
            visual.print_move(players, current_player)
            time.sleep(.025)

    # Effects
    previous = players[current_p][0]
    tile_effect(players, current_p, board)
    visual.print_health(players[current_p])
    visual.print_move(players, current_p)
    current = players[current_p][0]

    # Additional effects
    while previous != current and not (players[current_p][3] <= 0):
        previous = current
        tile_effect(players, current_p, board)
        visual.print_health(players[current_p])
        visual.print_move(players, current_p)
        current = players[current_p][0]

    # Death
    if players[current_p][3] <= 0:
        visual.activated_effect('Sorry player {0}! You died! You have to start over.'.format(current_p))
        players[current_p] = copy.deepcopy(players['s'])
        visual.print_health(players[current_p])
        visual.print_move(players, current_p)
    return


# ---------------- Functions that interact with view ------------------- #


# ask use old or new
def ask_old_new():
    return False


# Converts data from visual input to usable
def convert_data(level_v, dice_v):
    if level_v == 'Hard':
        level = 40
    elif level_v == 'Medium':
        level = 30
    elif level_v == 'Easy':
        level = 20

    dice = (1, dice_v)
    return level, dice


# Asks for board info
def ask_for_info():
    length_v = visual_options.input_data('board length')
    n_players_v = visual_options.input_data('number of players')
    dice_v = visual_options.input_data('dice')
    level_v = visual_options.input_data('difficulty')
    level_v, dice_v = convert_data(level_v, dice_v)
    return level_v, dice_v, length_v, n_players_v


# Call board drawer for initial setup
def setup(board, n_players, players, current_player):
    visual.print_board(board)
    visual.left_sidebar()
    visual.sidebar()
    visual.make_players(players, current_player)
    return


# Display dice result
def display_dice(result):
    visual.print_dice(result)
    return


# Ask for player choice
def ask_for_choice(option0, option1):
    a, b = visual.choice(option0, option1)
    return a == 0


# Display winner
def display_winner(current_player):
    visual.win_effect(current_player)
    time.sleep(3)
    quit()


# Loads a saved game
def load_save():
    try:
        file = open('save.txt')
        current_p_l = int(file.readline().strip())
        board = file.readline().strip()
        board = json.loads(board)
        board = {int(tile): tuple(board[tile]) for tile in board}
        players = file.readline().strip()
        players = json.loads(players)
        players = [(int(player), players[player]) if player.isdigit() else (player, players[player]) for player in
                   players]
        players = dict(players)
        file.close()
        if len(board) == 0 or len(players) == 0:
            return -1
        return board, players, current_p_l
    except:
        return -1


# Writes a save game
def write_save():
    global current_p
    board_s = json.dumps(model.board, separators=(',', ':'))
    players_s = json.dumps(model.players, separators=(',', ':'))
    current_p_s = str(current_p)
    file = open('save.txt', 'w')
    file.write(current_p_s + '\n')
    file.write(board_s + '\n')
    file.write(players_s + '\n')
    file.close()
    return


def get_current_p(saved_current_p_l):
    global current_p
    current_p = saved_current_p_l
    return


game_generator()
