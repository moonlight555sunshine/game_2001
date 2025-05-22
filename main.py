import random
# Initialize scores
user_points = 0
computer_points = 0
# Start the game
input('Press ENTER to start')
# Variable to check if special rules for round apply (change after 2-nd round)
check_round = False
while True:
    user_roll = 0
    computer_roll = 0
    # User rolls two dice
    for _ in range(2):
        user_roll += random.randint(1, 6)
    # Computer rolls two dice
    for _ in range(2):
        computer_roll += random.randint(1, 6)
    # From the second round onward, check for special rules
    if check_round:
        if user_roll == 7:
            user_points //= 7
        elif user_roll == 11:
            user_points *= 11
        else:
            user_points += user_roll
        if computer_roll == 7:
            computer_points //= 7
        elif computer_roll == 11:
            computer_points *= 11
        else:
            computer_points += computer_roll
    else:  # First round: just add the roll totals
        user_points += user_roll
        computer_points += computer_roll
    print(f'Your points: {user_points}')
    print(f'Computer points: {computer_points}')
    # Check for a winner
    if user_points >= 2001:
        print('You win!')
        break
    elif computer_points >= 2001:
        print('Computer wins!')
        break
    # Enable special rules for next round
    check_round = True
    input('Press ENTER to continue')