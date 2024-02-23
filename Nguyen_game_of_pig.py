"""
Name: Cardin Nguyen
Date: 2/24/24
Assignment: Game of pig
Description: Play a game of pig against a computer, first one to 100 wins.
"""

import random

player_score = 0
computer_score = 0


def roll_die(probability: float = 0) -> int:
    """
    Roll a 6 sided dice
    :param probability: Not used. I was going to mess around with editing the probability though.
    :return: The result of rolling the 6 sided dice
    """
    return random.randint(1, 6)


def player_turn(player_score: int) -> int:
    """
    Execute the player's turn.
    :param player_score: The current score for the player
    :return: Updated player's score after player's turn.
    """
    try:
        round_score = 0
        if not isinstance(player_score, int):
            raise ValueError
        while True:
            choice = input("'roll', or 'bank' your round score? (r/b) ")
            if choice.lower() == 'r':
                roll = roll_die()
                if roll == 1:
                    print("You rolled a 1! No points added to your total score.")
                    return player_score
                else:
                    round_score += roll
                    print(f"You rolled a {roll}. Your round score is {round_score}.")
            elif choice.lower() == 'b':
                player_score += round_score
                print(f"You banked your score. Your total score is now {player_score}.")
                return player_score
            else:
                print("Invalid choice. Please enter 'r' to roll, or 'b' to bank.")
    except ValueError:
        print("Invalid input: Player score has to be an int.")


def computer_turn(comp_score: int) -> int:
    """
    Play the computer's turn
    :param comp_score: The current computer score
    :return: The new, updated score for the computer
    """
    try:
        round_score = 0
        if not isinstance(comp_score, int):
            raise ValueError
        while True:
            roll = roll_die()
            if roll == 1:
                print("Computer rolled a 1! No points added to its total score.")
                return comp_score
            else:
                round_score += roll
                print(f"Computer rolled a {roll}. Its round score is {round_score}.")
                if round_score >= 20:
                    comp_score += round_score
                    print(f"Computer banked its score. Its total score is now {comp_score}.")
                    return comp_score
    except ValueError:
        print("Invalid input: Computer score has to be an int.")


def play_game() -> None:
    """
    Start playing the game.
    :return: Nothing, void method, which ends the game when it's needed.
    """
    player_score = 0
    computer_score = 0
    while player_score < 100 and computer_score < 100:
        print(f'\nYour turn.')
        print(f'| Your Score: {player_score} | Computer Score: {computer_score} |')
        player_score = player_turn(player_score)
        if player_score >= 100:
            print("Congratulations! You won the game!")
            if str(input("Play again? (y/n) ")).lower() == "y":
                play_game()
            else:
                return
        print("\nComputer's turn.")
        computer_score = computer_turn(computer_score)
    print("Computer won the game.")
    if str(input("Play again? (y/n) ")).lower() == "y":
        play_game()
    else:
        return


if __name__ == "__main__":
    play_game()