favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jen': 'rust'  # overwrote 'python'
}


def print_dict():
    for key in favorite_language:
        print(f"The favorite language of {key} is {favorite_language[key]}")


# Dictionaries are made of keys and values
# The key jen has a value of python

print(f"Jen's favorite language is {favorite_language['jen']}")

# If you have a duplicate key, only the last one is valid.

# Modifying values in dictionary
favorite_language['sarah'] = 'c++'
for key in favorite_language:
    print(f"The favorite language of {key} is {favorite_language[key]}")
# The order of the keys is preserved - note that Jen is still first even though there was a second
# dictionary value for jen

# Remove a key value pair
del favorite_language['phil']
print('\n')
for key in favorite_language:
    print(f"The favorite language of {key} is {favorite_language[key]}")

# You can use pop, if you want to store the value, key is not stored.

# What if I try to retrieve a key that doesn't exist
# print(favorite_language['smith']) # KeyError exception, .get() returns none
print(favorite_language.get('edward'))
print(favorite_language.get('smith'))  # None

# Activity
# Make a dictionary of the favorite colors of each person in the class
# Then write a function called reverse_lookup that will take in a color and
# returns a list of each person with that favorite color

favorite_colors = {
    'Ajay': "Blue",
    "Aaron": "Green",
    "Cole": "Blue",
    "Eli": "Navy",
    "Vanessa": "Purple",
    "Tristan": "Red",
    "Aron": "Black",
    "Meri": "Red",
    "Enil": "Green",
    "Spencer": "Red",
    "Kevin": "Purple",
    "Colton": "Blue",
    "Vincent": "Purple",
    "Alex": "Orange",
    "Nick": "Black",
    "Matthew": "Purple"
}


def reverse_lookup(color: str, dict: dict) -> list:
    """
    This function takes in a color and a dictionary of people and their favorite colors
    :param color: Color you are looking for in the dictionary
    :param dict:  of people and their favorite colors
    :return: A list of people with the favorite color
    """
    people = []
    for key in dict:
        if dict[key].lower() == color.lower():
            people.append(key)
    return people


color = 'purple'
print(f"The following people have a favorite color of {color}\n{"\n".join(reverse_lookup(color, favorite_colors))}")

# Looping through dictionaries

# By key value pairs
#   key      value
for person, color in favorite_colors.items():
    print(f"{person.title()} likes the color {color.lower()}")

# By values
color_string = ""
for color in set(favorite_colors.values()):  # Set removes duplicates
    color_string += f"{color.lower()}, "

color_string = color_string[:-2] + "."  # Remove the last comma and add a period
print(f"The colors mentioned were: {color_string}")

# By keys
student_string = ""
for student in sorted(favorite_colors.keys()): # sorted will alphabetize the list
    student_string += f"{student}, "
student_string = student_string[:-2] + "."
print(f"The students are: {student_string}")

# Nesting info with dictionaries
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris"
    }
}
#   Dict name   key       value
print(users["aeinstein"]["location"])
print(users['mcurie']['first'].title())
print(users['aeinstein'])
