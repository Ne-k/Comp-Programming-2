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




# Problem 2
def text_to_keypress(text):
    # Define the mapping of characters to key presses
    keypresses = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '0', ',': '11', '.': '33', '!': '1111', '?': '9999'
    }
    text = text.lower()
    result = ""
    for char in text:
        if char in keypresses:
            result += keypresses[char]

    return result

# Problem 3
def count_unique_chars():
    text = input("Enter a string: ")
    unique_chars = {}
    for char in text:
        if char not in unique_chars:
            unique_chars[char] = 1
    print(f"The string has {len(unique_chars)} unique characters.")

# Problem 4
def number_to_words(n):
    ones = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
    }
    teens = {
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
    }
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
    }

    if 1 <= n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n]
    elif 20 <= n < 100:
        if n % 10 == 0:
            return tens[n // 10]
        else:
            return tens[n // 10] + ' ' + ones[n % 10]
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + ' hundred'
        else:
            return ones[n // 100] + ' hundred ' + number_to_words(n % 100)


# Test the function

def main():
    print("\033[94mCardin Nguyen\033[0m")

    # Problem 1
    frEn = {
        "le": "the",
        "la": "the",
        "livre": "book",
        "pomme": "apple",
    }
    print("The french words for 'the' are: ", reverse_lookup(frEn, "the"))
    print("Expected: ['le', 'la']")
    print()
    print("The french words for 'apple' are: ", reverse_lookup(frEn, "apple"))
    print("Expected: ['pomme']")
    print()
    print("The french words for 'asdf' are: ", reverse_lookup(frEn, "asdf"))
    print("Expected: []")
    print()

    # Problem 2
    print(text_to_keypress("Hello, World!"))

    print()

    # Problem 3
    count_unique_chars()

    print()

    # Problem 4
    print(number_to_words(int(input("Enter a number between 0 and 999: "))))

if __name__ == "__main__":
    main()
