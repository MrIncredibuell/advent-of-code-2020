player_1, player_2 = open('data.txt').read().replace('\r', '').split('\n\n')
player_1 = [int(l) for l in player_1.split('\n')[1:]]
player_2 = [int(l) for l in player_2.split('\n')[1:]]


def score(player_1, player_2):
    s = 0
    for i, v in enumerate(player_1[::-1]):
        s += (i + 1) * v
    for i, v in enumerate(player_2[::-1]):
        s += (i + 1) * v
    return s

def part1(player_1, player_2):
    while len(player_1) > 0 and len(player_2) > 0:
        if player_1[0] > player_2[0]:
            player_1 = player_1[1:] + [player_1[0], player_2[0]]
            player_2 = player_2[1:]
        else:
            player_2 = player_2[1:] + [player_2[0], player_1[0]]
            player_1 = player_1[1:]
    return score(player_1, player_2)

def pick_winner(player_1, player_2):
    if player_1[0] < len(player_1) and player_2[0] < len(player_2):
        p1, p2 = play(player_1[1:player_1[0] + 1], player_2[1:player_2[0] + 1])
        if len(p1) > 0:
            return 1
        else:
            return 2
    elif player_1[0] > player_2[0]:
        return 1
    else:
        return 2

def play(player_1, player_2):
    seen = set()
    while len(player_1) > 0 and len(player_2) > 0:
        if (str(player_1), str(player_2)) in seen:
            # just fake that 1 wins
            return [1], []
        seen.add((str(player_1), str(player_2)))
        if pick_winner(player_1, player_2) == 1:
            player_1 = player_1[1:] + [player_1[0], player_2[0]]
            player_2 = player_2[1:]
        else:
            player_2 = player_2[1:] + [player_2[0], player_1[0]]
            player_1 = player_1[1:]
    return player_1, player_2

 
def part2(player_1, player_2):
    player_1, player_2 = play(player_1, player_2)
    return score(player_1, player_2)

print(part1(player_1[:], player_2[:]))
print(part2(player_1[:], player_2[:]))
