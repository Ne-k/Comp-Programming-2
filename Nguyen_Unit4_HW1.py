"""
Name: Cardin Nguyen
Date: 2/23/24
Assignment: Unit 4 HW 1
Description:
Problem 1

Create a function called list_of_cubes(start, stop). That function should make, and return, a list of the first 10 cubes
using list comprehension. Be sure to use the parameters when you call it e.g. list_of_cubes(5,10). Then print the values
from each of those lists to the console


Problem 2

Create a function called pizza_modifier(topping_list, new_topping) that allows a user to add a new topping to a list of
toppings. The function should print the current toppings and print the toppings with the new topping added.

"""


# Problem 1
def list_of_cubes(start: int, stop: int) -> None:
    """
    Create a list of the first 10 cubes using list comprehension.
    :param start: The starting number for the range of numbers to cube
    :param stop: The ending number for the range of numbers to cube
    :return: A list of the first 10 cubes
    """

    try:
        if not isinstance(start, int) or not isinstance(stop, int):
            raise ValueError
        return print([i ** 3 for i in range(start, stop)])
    except ValueError:
        print("Invalid input: Start and stop have to be integers.")


# Problem 2
def pizza_modifier(toppings: list, new_topping: str) -> None:
    """
    Allows the user to add a new topping to a list of toppings
    :param toppings: Current List
    :param new_topping: New toppings to add to toppings
    :return: Nothing, it prints to the console the new list
    """
    try:
        if not isinstance(toppings, list) or not isinstance(new_topping, str):
            raise ValueError
        print(f"Current toppings: {toppings}")
        toppings.append(new_topping)
        print(f"New toppings: {toppings}")
    except ValueError:
        print("Invalid input: Toppings have to be a list and new_topping has to be a string.")

def main():
    list_of_cubes(5, 10)
    pizza_modifier(["pepperoni", "cheese", "mushrooms"], "onions")


if __name__ == "__main__":
    main()
