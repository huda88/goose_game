import json


board = {0: ('none',), 1: ('none',), 2: ('none',), 3: ('step', -2), 4: ('none',), 5: ('step', 1), 6: ('none',),
         7: ('turn_mod', -2), 8: ('none',), 9: ('health', -40), 10: ('none',), 11: ('none',), 12: ('none',),
         13: ('none',), 14: ('health', -20), 15: ('none',), 16: ('none',), 17: ('dice_mod', 'shift', -1, 5),
         18: ('goto_p',), 19: ('health', -40), 20: ('dice_mod', 'stuck', 2, 3), 21: ('step', -10), 22: ('none',),
         23: ('none',), 24: ('step', 5), 25: ('goto_t', 30), 26: ('none',), 27: ('none',), 28: ('turn_mod', -2),
         29: ('none',), 30: ('health', -20), 31: ('none',), 32: ('health', -90), 33: ('none',), 34: ('turn_mod', -1),
         35: ('none',), 36: ('health', -75), 37: ('none',), 38: ('goto_t', 0), 39: ('none',)}

p = {'s': [0, [1, 6], {}, 100], 1: [0, [1, 6], {}, 100], 2: [0, [1, 6], {}, 100]}


t = 2

board_s = json.dumps(board, separators=(',', ':'))
player_s = json.dumps(p, separators=(',', ':'))
turn_s = str(t)


file = open('save.txt', 'w')
file.write(turn_s+'\n')
file.write(board_s+'\n')
file.write(player_s+'\n')
file.close()


file = open('save.txt')
turn_l = file.readline().strip()
turn_l = int(turn_l)
board_l = file.readline().strip()
board_l = json.loads(board_l)
board_l = {int(tile): tuple(board_l[tile]) for tile in board_l}
player_l = file.readline().strip()
player_l = json.loads(player_l)
player_l = [(int(player), player_l[player]) if player.isdigit() else (player, player_l[player]) for player in player_l]
player_l = dict(player_l)

print(turn_l)
print(board_l)
print(player_l)
