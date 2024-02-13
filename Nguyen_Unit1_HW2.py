"""
Name: Cardin Nguyen
Date: 2/12/24
Assignment: Unit 1 HW 2
Description: Ask a user if their shape is a polygon or a circle.
Then ask them for a side length and number of sides for a polygon or for a radius for a circle.
Use functions to do the calculations. Prompts should not be in the functions that do calculations.
Print the area of the shape in the following format:
If it's a circle: The area of circle with radius __ is __
If it's a polygon: The area of a __-sided shape with side length __ is ____
Use try/except to make sure the user enters appropriate input
"""
import math


shape = input("Is your shape a polygon or a circle? ")
if shape.lower() == "polygon":
    length = input("What is the side length for your polygon")
    sides = input("How many sides does your polygon have?")
elif shape.lower() == "circle":
    radius = input("What is the radius of your circle?")

def polygon_area(length: float, sides: int) -> float:
    if not isinstance(length, float) or not isinstance(sides, int):
        raise ValueError
    return (length ** 2 * sides) / (4 * (math.tan(math.pi / sides)))


if __name__ == "__main__":
    if shape.lower() == "polygon":
        try:
            length = float(length)
            sides = int(sides)
            print(f"The area of a {sides}-sided shape with side length {length} is {polygon_area(length, sides)}")
        except ValueError:
            print("Invalid input: Length has to be a float, sides has to be an int.")
    elif shape.lower() == "circle":
        try:
            radius = float(radius)
            print(f"The area of a circle with radius {radius} is {int(math.pi * radius ** 2)}")
        except ValueError:
            print("Invalid input: Length has to be a float, sides has to be an int.")
    else:
        print("Your shape seems to be an invalid input.")
