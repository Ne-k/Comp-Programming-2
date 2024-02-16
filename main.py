"""
Name: Cardin
Date 2/14/2024
Class: Period 8
Description: Convering f-strings, functions with the default parameters,
string indexing, string slicing, as well as if __name__
"""


def slicing_demo(string):
    # access last character
    print(string[-1])
    print(string[len(string) - 1])

    # slicing
    # string[start : stop : step], stop is not included
    print(string[0: 3])  # step not specified means default to 1
    print(string[4:9])  # slicing so Smith only comes out
    print(string[4:])  # 2nd method to get Smith - If stop blank, goes to end of string

    print(string[0: len(string): 2])  # printing every other letter in the string starting at M
    print(string[::2])  # 2nd method to print every other letter in the string starting at M
    print(string[-5:])  # Try to get Smith using negative indices

    print(string[-1:-6:-1])  # print smith backwards
    print(string[::-1])  # print entire string backwards

    # Python oddity
    print(string[4:1000000])  # no out of bounds error
    # print(string[1000000])  # This will be an error bc not slicing

def salutation(name:str, title:str="boring", suffix:str="") -> None:
    print(f"Hello, {name} the {title} {suffix}.")


def main():
    # name = M  r  .     S  m  i  t  h
    #        0  1  2  3  4  5  6  7  8
    #       -9 -8 -7 -6 -5 -4 -3 -2 -1
    name = "Mr. Smith"
    slicing_demo(name)

    salutation("Brandon")

if __name__ == "__main__":
    main()
