import random
# Wait for the user to start the game
input('Press ENTER to start')

def user_roll(user_points, check_round):
    """
    Roll the dice and return the total points.
    Args:
        user_points (int): The current points of the user.
        check_round (bool): Whether this is the first round.

    Returns:
        int: The total points of the user.
    """
    roll = 0
    # Roll two six-sided dice
    for _ in range(2):
        roll += random.randint(1, 6)
    print(f'You rolled {roll}')
    # Apply special rules after the first round
    if check_round:
        if roll == 7:
            user_points //= 7
        elif roll == 11:
            user_points *= 11
        else:
            user_points += roll # Add roll to total
    else:
        user_points += roll  # In the first round, just add the roll
    return user_points
def computer_roll(computer_points, check_round):
    """
    Simulates the computer's dice roll and updates it's score.
    Args:
        computer_points (int): The current points of the computer.
        check_round (bool): Whether this is the first round.

    Returns:
        int: The total points of the computer.
    """
    roll = 0
    # Roll two six-sided dice
    for _ in range(2):
        roll += random.randint(1, 6)
    print(f'Computer rolled {roll}')
    # Apply special rules after the first round
    if check_round:
        if roll == 7:
            computer_points //= 7
        elif roll == 11:
            computer_points *= 11
        else:
            computer_points += roll # Add roll to total
    else:
        computer_points += roll # In the first round, just add the roll
    return computer_points

def main(check_round=False):
    """
    Main game loop. Rolls dice for user and computer, applies rules, and checks win condition.
    Args:
        check_round (bool): Indicates if special rules apply. Defaults to False.

    Returns:
        str: The winning message.
    """
    user_result = 0
    computer_result = 0
    while True:
        # Perform user and computer rolls
        user_points = user_roll(user_result, check_round)
        user_result = int(user_points)
        computer_points = computer_roll(computer_result, check_round)
        computer_result = int(computer_points)
        # Display current scores
        print('----------------------------------')
        print(f'Your points: {user_result}')
        print(f'Computer points: {computer_result}')
        print('----------------------------------')
        # Check for win condition
        if user_result >= 2001:
            return 'You win!'
        elif computer_result >= 2001:
            return 'Computer wins!'
        # Enable special rules for future rounds
        check_round = True
        input('\nPress ENTER to continue\n')
# Start the game if the script is run directly
if __name__ == '__main__':
    main()