def main():
    cat_name = "Diamond"
    cat_sentence = f"{cat_name} is one of six foster kittens"
    print(cat_sentence.lower())
    print(cat_sentence.upper())
    print(cat_sentence.capitalize())
    print(cat_sentence.title())
    print(cat_name.center(20, "*"))
    print(cat_sentence.count("o"))
    print(cat_sentence.count("foster"))
    print(cat_sentence.replace("six", "seven"))
    cat_sentence = cat_sentence.replace("six", "seven")
    print(cat_sentence)

    sentence = "The grey cat is grey."
    sentence = sentence.replace("grey", "orange", 1)
    cat_name = "         Applejack"
    print(cat_name.strip())

    user_in = "5"
    print(user_in.isdigit())
    print(user_in.isalpha())
    print(user_in.isalnum())




    # cat_name[0] = "d" Strings are immutable, cannot assign a character
    # cat_name = "d" + cat_name[1:]
    # print(cat_name)

    # list_number = "12356789876"
    # num = 0
    # # non pythonic way
    # for i in range(len(list_number)):
    #     if int(list_number[i]) % 2 == 0:
    #         num += 1
    #     print(num)
    #
    # # Printing every other item
    # for i in range(0, len(list_number), 2):
    #     print(list_number[i])
    #
    #     # pythonic way
    # for number in list_number:
    #     if int(number) % 2 == 0:
    #         num += 1
    # print(num)
    #
    # Write a function called val_counter that will go through an arbitrary string parameter and count how many
    # vowels, including upper and lower, are in it
    # The count will be returned not printed

    def vowel_counter(string: str) -> int:
        """
        This function will count the number of vowels in a string, case-insensitive
        :param string: Any string to count
        :return How many vowels are in the string
        """
        cnt = 0
        if not isinstance(string, str):
            return 0
        for char in string:
            if char.lower() in "aeiou":
                cnt += 1
        return cnt


    # assert vowel_counter("") == 0
    # assert vowel_counter("Rhythm") == 0
    # assert vowel_counter("aeiouaeiou") == 10
    # # You can do try and except to catch the error, I dont want to because im lazy as shit
    # print("All tests pass")


if __name__ == "__main__":
    main()
