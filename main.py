"""Name: Cardin Nguyen
Date: 2/6/24
Assignment: Unit 1 HW 1
Description: Write a function called game_introduction
that takes no parameters and prints the introduction to a game of your choosing.

Write a function called
update_health that takes two parameters called current_health and health_change. The function will use f-strings to
print “Your original health is ____”,  update the current health with the health change (could be negative) and then
will print “Your health is now ______” with the updated
"""
import time


# Exercise 1
def game_introduction() -> None:
    """
    Introduction to the game.

    Parameter
    ---------
    None

    Returns
    -------
    None
    """
    print("Welcome to the game of life! In the game you'll have to do x and y to complete the game. Good luck!")


# Exercise 2
def update_health(current_health: int, health_change: int) -> None:
    """
    Update the current health with the health change.

    Parameters
    ----------
    current_health : int
        The current health of the player.
    health_change : int
        The amount of health change.

    Returns
    -------
    None
    """
    print(f"Your original health is {current_health}")
    current_health += health_change
    print(f"Your health is now {current_health}")


game_introduction()
time.sleep(2)
update_health(100, -10)
