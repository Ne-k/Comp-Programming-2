"""
The Game of Pig is a classic game played with a 6 sided die. In the game a player rolls the die. If they roll a 2
through 6, they add that score to their round score, but if they roll a 1, their round is over and their round score
resets to zero.

At any point, the player can choose to bank their round score. When they do that, the points are added to their overall
score and their round score resets back to zero.

Once the player’s overall score reaches 100, they win. While the die roll is random, there is a little strategy when
deciding whether to bank or continue in the round. If you try to be a pig and get more points, you may lose everything
and have to start over!

More information on the game can be found on wikipedia.

For the first part of this project, you are going to make the basic gameplay and keep track of how many turns it takes
to win. At the start of each turn, you should display the turn number and the player’s score. Each round, you should
ask the player if they want to roll or bank the points. If they bank, you move on to the next turn, otherwise you roll
again. If they roll a 1, then that round ends and the round score is reset. Otherwise, add the number from the die to
the round score. Play continues like that until you get to 100 or more.

You can implement this several different ways. One thing to consider is that in the next activity, you will be adding
a computer player. Keep that in mind as you think about the design.

You’ll also need to include randomization in your program to simulate rolling a die. There is information on including
randomization in the docs tab (Basics > Random Numbers) or in this tutorial.
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
