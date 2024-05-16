def rules(rolls):
    if (rolls[0] == 1 and rolls[1] == 2) or (rolls[0] == 2 and rolls[1] == 1):
        if (rolls[2] == 1 and rolls[3] == 2) or (rolls[2] == 2 and rolls[3] == 1):
            return 'Tie'
        else:
            return 'Player 1 wins'

    elif (rolls[2] == 1 and rolls[3] ==2) or (rolls[2] == 2 and rolls[3] == 1):
        return 'Player 2 wins'
    
    elif (rolls[0] == rolls[1]) and (rolls[2] == rolls[3]):
        if max(rolls[0], rolls[1]) > max(rolls[2], rolls[3]):
            return 'Player 1 wins'
        elif max(rolls[0], rolls[1]) < max(rolls[2], rolls[3]):
            return 'Player 2 wins'
        elif min(rolls[0], rolls[1]) > min(rolls[2], rolls[3]):
            return 'Player 1 wins'
        elif min(rolls[0], rolls[1]) < min(rolls[2], rolls[3]):
            return 'Player 2 wins'
        else:
            return 'Tie'
        
    elif ((rolls[0] == rolls[2]) and (rolls[1] == rolls[3])):
        return 'Tie'
    elif ((rolls[0] == rolls[3]) and (rolls[1] == rolls[2])):
        return 'Tie'
    
    elif (rolls[0] == rolls[1]) and (rolls[2] != rolls[3]):
        return 'Player 1 wins'
    
    elif (rolls[0] != rolls[1]) and (rolls[2] == rolls[3]):
        return 'Player 2 wins'
    
    elif (rolls[0] != rolls[1]) and (rolls[2] != rolls[3]):
        if max(rolls[0], rolls[1]) > max(rolls[2], rolls[3]):
            return 'Player 1 wins'
        elif max(rolls[0], rolls[1]) < max(rolls[2], rolls[3]):
            return 'Player 2 wins'
        elif min(rolls[0], rolls[1]) > min(rolls[2], rolls[3]):
            return 'Player 1 wins'
        elif min(rolls[0], rolls[1]) < min(rolls[2], rolls[3]):
            return 'Player 2 wins'

def testing_cases(rolls):
    p1_wins = 0
    p2_wins = 0
    total_games = 0
    arr_is_nums = True
    num_stars = 0
    new_rolls = []
    for i in rolls:
        if i == '*':
            arr_is_nums = False
            num_stars += 1
            new_rolls.append(i)
        else:
            i = int(i)
            new_rolls.append(i)

    i_idx = 0
    j_idx = 0
    z_idx = 0
    if num_stars == 4:
        return 205, 0, 432
    if num_stars == 0:
        if rules(new_rolls) == 'Player 1 wins':
            p1_wins += 1
            total_games += 1
        elif rules(new_rolls) == 'Player 2 wins':
            p2_wins += 1
            total_games += 1
        elif rules(new_rolls) == 'Tie':
            total_games += 1


    if ('*' in new_rolls):
        i_idx = new_rolls.index('*')
        if num_stars >= 2:
            j_idx = new_rolls.index('*', i_idx+1)
            if num_stars == 3:
                z_idx = new_rolls.index('*', j_idx+1)
    #print(i_idx, j_idx)
    
        if num_stars == 1:
            for i in range(1,7):
                new_rolls[i_idx] = i
                if rules(new_rolls) == 'Player 1 wins':
                    p1_wins += 1
                    total_games += 1
                elif rules(new_rolls) == 'Player 2 wins':
                    p2_wins += 1
                    total_games += 1
                elif rules(new_rolls) == 'Tie':
                    total_games += 1


        if num_stars == 2:
            for i in range(1,7):
                for j in range(1,7):
                    new_rolls[i_idx] = i
                    new_rolls[j_idx] = j
                    if rules(new_rolls) == 'Player 1 wins':
                        p1_wins += 1
                        total_games += 1
                    elif rules(new_rolls) == 'Player 2 wins':
                        p2_wins += 1
                        total_games += 1
                    elif rules(new_rolls) == 'Tie':
                        total_games += 1
        
        if num_stars == 3:
            for i in range(1,7):
                for j in range(1,7):
                    for z in range(1,7):
                        new_rolls[i_idx] = i
                        new_rolls[j_idx] = j
                        new_rolls[z_idx] = z
                        if rules(new_rolls) == 'Player 1 wins':
                            p1_wins += 1
                            total_games += 1
                        elif rules(new_rolls) == 'Player 2 wins':
                            p2_wins += 1
                            total_games += 1
                        elif rules(new_rolls) == 'Tie':
                            total_games += 1

    return p1_wins, p2_wins, total_games

from fractions import Fraction
rolls = input().split()
unsimplified = 0
while rolls != ['0', '0', '0', '0']:
    #rolls = [int(i) for i in rolls]
    #print(rules(rolls))
    unsimplified = (testing_cases(rolls))
    #print(unsimplified)
    print(Fraction(unsimplified[0], unsimplified[2]))
    rolls = input().split()