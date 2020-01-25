# solving Riddler Classic @ https://fivethirtyeight.com/features/how-many-pennies-should-you-pinch/


def is_legal(move):
    """
    Is it a legal move? i.e. either removing only from one heap or removing the same number of pennies from both heaps
    :param move: a 2-tuple (n1, n2) where n1, n2 are the number of pennies removed from heap1 and heap2 respectively
    :return: True or False
    """
    return move[0] >= 0 and move[1] >= 0 and (move[0] == move[1] or move[0] * move[1] == 0)


def there_is_move_between(situation1, situation2):
    """
    Is it possible to go from situation1 to situation2 in just one legal move of the game?
    :param situation1: a 2-tuple (n1, n2) where n1, n2 are the number of pennies in heap1 and heap2 respectively
    :param situation2: a 2-tuple (n1, n2) where n1, n2 are the number of pennies in heap1 and heap2 respectively
    :return: True or False
    """
    needed_move1 = (situation1[0] - situation2[0], situation1[1] - situation2[1])
    needed_move2 = (situation1[0] - situation2[1], situation1[1] - situation2[0])
    if is_legal(needed_move1) or is_legal(needed_move2):
        return True
    else:
        return False


n_max = 30  # max. nr. of pennies to play with
winning_choices = [(0, 0)]  # initial distributions into two heaps guaranteeing that I (player 1) win
has_winning_choices = {}  # nr. of pennies x has at least one winning initial distribution for me, player 1?

# let's increase the number of pennies to play, n, from 1 to n_max
for n in range(1, n_max + 1):
    has_winning_choices[n] = False
    for n1 in range(1, n):
        choice = (n1, n - n1)
        # this choice is winning if and only if player 2 cannot reach any winning choice from it
        is_winning_choice = True
        for wc in winning_choices:
            if there_is_move_between(choice, wc):
                is_winning_choice = False
                break
        if is_winning_choice:
            winning_choices.append(choice)
            has_winning_choices[n] = True
print('Initial distributions into two heaps guaranteeing victory to me (player 1):', winning_choices)
print('Number of pennies guaranteeing victory to me (player 1):', [n for n, w in has_winning_choices.items() if w])
print('Number of pennies guaranteeing victory to you (player 2):', [n for n, w in has_winning_choices.items() if not w])
