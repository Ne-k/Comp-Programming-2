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
import time

round = 0
player_score = 0
computer_score = 0


def roll_die() -> int:
    return random.randint(1, 6)


def player_turn() -> int:
    round_score = 0
    while True:
        player_dice = roll_die()
        print("Rolling. . .")
        time.sleep(1.5)

        if player_dice == 1:
            print(f"You rolled a {player_dice}! Your turn is over.")
            return 0
        else:
            print(f"You rolled a {player_dice}!")
            round_score += player_dice
            print(f"Your round score is now {round_score}")
            choice = input("Would you like to roll again or bank your points? (r/b) ")
            if choice.lower() == "b":
                return round_score
            elif choice.lower() == "r":
                continue


def game():
    while player_score < 100 and computer_score < 100:
        round += 1
        print(f"Round: {round}")
        time.sleep(2.5)
        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}\n--------------")
        time.sleep(2.5)
        print("Player's Turn:")
    return None


def main():
    choice = input("Would you like to play a game of Pig? (y/n) ")
    if choice.lower() == "y":
        game()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
