"""Name: Cardin Nguyen
Date: 3/8/24 Assignment:
Unit 5 HW 3
Description:  https://docs.google.com/document/d/1_TKrhQSEWTh4AweB_w2UN1hikE7vz4O_Us9st90PVCk/edit
"""

# Problem 1
def reverse_lookup(d: dict, v: str) -> list:
    """
    This function takes a dictionary and a value and returns a list of keys that map to that value in the dictionary.
    :param d: dictionary
    :param v: value
    :return:
    """
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys



"""On some cell phones, text messages can be sent using the numeric keypad. Because each key has multiple letters 
associated with it, multiple key presses are needed for most letters. Pressing the number once generates the first 
letter on the key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character 
listed for that key.

Write a program that displays the key presses that must be made to enter a text message read from the user. Construct 
a dictionary that maps from each letter or symbol to the key presses. Then use the dictionary to generate and display 
the presses for the user’s message. For example, if the user enters Hello, World! then your program should output 
4433555555666110966677755531111. Ensure that your program handles both uppercase and lowercase letters. Ignore any 
characters that aren’t listed in the table above such as semicolons and brackets.

"""

# Problem 2
def text_to_keypress(text: str) -> str:
    """
    This function takes a string and returns the keypresses needed to enter the string on a cell phone.
    :param text: string
    :return: string
    """
    text = text.lower()
    keypresses = ""
    keymap = {
        "a": "2",
        "b": "22",
        "c": "222",
        "d": "3",
        "e": "33",
        "f": "333",
        "g": "4",
        "h": "44",
        "i": "444",
        "j": "5",
        "k": "55",
        "l": "555",
        "m": "6",
        "n": "66",
        "o": "666",
        "p": "7",
        "q": "77",
        "r": "777",
        "s": "7777",
        "t": "8",
        "u": "88",
        "v": "888",
        "w": "9",
        "x": "99",
        "y": "999",
        "z": "9999",
        " ": "0",
    }
    for char in text:
        if char in keymap:
            keypresses += keymap[char]
    return keypresses
def main():
    # Problem 1
    # frEn = {
    #     "le": "the",
    #     "la": "the",
    #     "livre": "book",
    #     "pomme": "apple",
    # }
    # print("The french words for 'the' are: ", reverse_lookup(frEn, "the"))
    # print("Expected: ['le', 'la']")
    # print()
    # print("The french words for 'apple' are: ", reverse_lookup(frEn, "apple"))
    # print("Expected: ['pomme']")
    # print()
    # print("The french words for 'asdf' are: ", reverse_lookup(frEn, "asdf"))
    # print("Expected: []")

    # Problem 2
    print(text_to_keypress("Hello, World!"))


if __name__ == "__main__":
    main()