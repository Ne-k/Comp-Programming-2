"""
Name: Cardin Nguyen
Date: 2/23/24
Assignment: Unit 4 HW 1
Description:
Problem 1

Create a function called list_of_cubes(start, stop). That function should make, and return, a list of the first 10 cubes using list comprehension. Be sure to use the parameters when you call it e.g. list_of_cubes(5,10). Then print the values from each of those lists to the console


Problem 2

Create a function called pizza_modifier(topping_list, new_topping) that allows a user to add a new topping to a list of toppings. The function should print the current toppings and print the toppings with the new topping added.

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
    return None
def main():
    list_of_cubes(5, 10)

if __name__ == "__main__":
    main()
