import math


def func(num_times: int) -> None:
    """
    This function will print 'Hello' num_times times
    """
    # Method 1
    for i in range(num_times):
        print("Hello")
    # method 2
    print("Hello\n" * num_times)


def mult_checker(number: int, factor: int) -> bool:
    """This function checks if a number is a factor of another number

    Parameters
    ----------
    number: int - number I want to check
    factor:int - factor I want to check

    Return
    ----------
    boolean - true if factor is a factor of number,
    false if not
    """

    return number % factor == 0


# write a function called length_comparison
# that takes in two string two arguments
# and returntells the user which string is longer
# and returns the length of the longest string
def length_comparison(word1: str, word2: str) -> str:
    if (type(word1) != str) | (type(word2) != str):
        return "Please enter a valid string"
    else:
        if len(word1) > len(word2):
            return f"{word1} is longer, with a length of {len(word1)}"
        elif len(word2) > len(word1):
            return f"{word2} is longer, with a length of {len(word2)}"
        else:
            return f"{word1} and {word2} are the same length"


# counter = 0
# while counter < 10:
#     print(f"counter value: {counter}")
#     counter += 1

# print(length_comparison(123, "goodbye"))
# func(1)
# print(mult_checker(4, 2))
