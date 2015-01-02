#!/usr/local/bin/python3
import random
import copy


# Board and player data
board = {}
players = {}


# Board generator, create a dictionary with tile and effects
def board_generator(length, dice, effect_list, level):
    global board
    lst_effects = create_lst_effects(length, effect_list, level, dice)
    board = dict()
    for x in range(length + 1):
        if x == 0:
            board[x] = ('none',)
        elif x == length:
            board[x] = ('win',)
        elif x == (length - 4):
            board[x] = ('goto_t', 0)
        else:
            if x in lst_effects:
                board[x] = lst_effects[x]
            else:
                board[x] = ('none',)
    return


# Generate a player dictionary with all the possibility
def player_generator(n_players, dice):
    global players
    players = dict()
    players['s'] = [0, [dice[0], dice[1]], {}, 100]
    for x in range(1, n_players + 1):
        players[x] = copy.deepcopy(players['s'])
    return


# Little function to change the sign randomly in the creation of the effects
def sign(element, element2):
    signed = random.randint(0, 1)
    shift = random.randint(element, element2)
    if signed == 0:
        shift = - shift
    return shift


# Less powerful, more frequent effects
def part_create_lst_1(addresses, lst_effects, effect_list, length):
    address = random.randint(1, length - 5)
    while address in addresses:
        address = random.randint(1, length - 5)
        addresses.append(address)
    a = effect_list[random.randint(0, 2)]
    if a == 'step':
        number = sign(1, 10)
        while not (0 < address + number < length):
            number = sign(1, 10)
        lst_effects[address] = (a, number)
    elif a == 'health':
        number = sign(1, 75)
        lst_effects[address] = (a, number)
    else:
        lst_effects[address] = (a,)


# More powerful, less frequent effects
def part_create_lst_2(addresses, lst_effects, effect_list, length, dice):
    address = random.randint(1, length - 5)
    while address in addresses:
        address = random.randint(1, length - 5)
        addresses.append(address)
    a = effect_list[random.randint(3, 5)]
    if a == 'turn_mod':
        number = sign(1, 3)
        lst_effects[address] = (a, number)
    elif a == 'dice_mod':
        type_dice_mod = ['stuck', 'shift', 'exp_shr']
        temp_final = [a, type_dice_mod[random.randint(0, 2)]]
        if temp_final[1] == 'stuck':
            lst_effects[address] = (temp_final[0], temp_final[1], random.randint(1, dice[1]), random.randint(1, 2))
        elif temp_final[1] == 'shift':
            number = sign(1, dice[1] // 2)
            lst_effects[address] = (temp_final[0], temp_final[1], number, random.randint(1, 2))
        else:
            number = sign(1, dice[1] // 4)
            lst_effects[address] = (temp_final[0], temp_final[1], number, random.randint(1, 2))
    else:
        lst_effects[address] = (a, random.randint(0, (length - 1)))


# Create a dictionary of effects and assign in a particular tile with all the random number needed in the game.
def create_lst_effects(length, effect_list, level, dice):
    lst_effects = {}
    addresses = []
    for x in range(level * length // 100 // 3 * 2):
        part_create_lst_1(addresses, lst_effects, effect_list, length)
    for x in range(level * length // 100 // 3):
        part_create_lst_2(addresses, lst_effects, effect_list, length, dice)
    return lst_effects


# Checks player for skip turns
def check_for_skip(player, ):
    if 'turn_mod' not in player[2]:
        return False
    else:
        if player[2]['turn_mod'] < 0:
            return True
        else:
            return False


# Checks player for more turns
def check_for_more(player, ):
    if 'turn_mod' not in player[2]:
        return False
    else:
        if player[2]['turn_mod'] > 0:
            return True
        else:
            return False


# Moves player by offset
def step(current_p, offset, hp):
    global players
    if hp:
        players[current_p][3] += offset * 5
    else:
        players[current_p][0] += offset
    return


# Adds or subtracts turns from player
def turn_mod(current_p, mod, hp):
    global players
    if hp:
        players[current_p][3] += mod * 20
    else:
        if 'turn_mod' not in players[current_p][2]:
            players[current_p][2]['turn_mod'] = mod
        else:
            players[current_p][2]['turn_mod'] += mod
    return


# Moves player to another random player
def goto_p(current_p):
    global players
    ran = current_p
    while ran == current_p:
        ran = random.randint(1, len(players) - 1)
    players[current_p][0] = players[ran][0]
    return


# Moves player to tile
def goto_t(current_p, tile):
    global players
    players[current_p][0] = tile
    return


# Modifies player dice
def dice_mod(current_p, mode, number, duration):
    global players
    old_dice = players[current_p][1]
    if mode == 'stuck':
        players[current_p][1] = [number, number]
        players[current_p][2]['dice_mod'] = duration
    elif mode == 'shift':
        new_dice = [old_dice[0] + number, old_dice[1] + number]
        if new_dice[0] < 1:
            new_dice[0] = 1
        if new_dice[1] < new_dice[0]:
            new_dice[1] = new_dice[0]
        players[current_p][1] = new_dice
        players[current_p][2]['dice_mod'] = duration
    elif mode == 'exp_shr':
        new_dice = [old_dice[0] - number, old_dice[1] + number]
        if new_dice[0] < 1:
            new_dice[0] = 1
        if new_dice[1] < new_dice[0]:
            new_dice[1] = new_dice[0]
        players[current_p][1] = new_dice
        players[current_p][2]['dice_mod'] = duration
    return


# Affects player health
def health(current_p, x):
    global players
    players[current_p][3] += x
    return


# Handles effect duration
def effect_expire(current_p):
    global players
    if len(players[current_p][2]) == 0:
        return
    else:
        remove = []
        for effect in players[current_p][2]:
            if players[current_p][2][effect] == 0:
                remove.append(effect)
            elif players[current_p][2][effect] > 0:
                players[current_p][2][effect] -= 1
            elif players[current_p][2][effect] < 0:
                players[current_p][2][effect] += 1
        for effect in remove:
            if effect == 'dice_mod':
                players[current_p][1] = players['s'][1]
            del players[current_p][2][effect]
        return


def get_board(saved_board):
    global board
    board = copy.deepcopy(saved_board)
    return board


def get_players(saved_players):
    global players
    players = copy.deepcopy(saved_players)
    return players