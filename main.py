"""
Reads the contents of a text file
From Python Crash Course 3rd edition
"""
from pathlib import Path
from math import factorial
from decimal import Decimal, getcontext
from tqdm import tqdm

getcontext().prec = 1000

import threading


def cal(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)

    for k in tqdm(range(n)):
        t = ((-1) ** k) * (factorial(6 * k)) * (13591409 + 545140134 * k)
        deno = factorial(3 * k) * (factorial(k) ** 3) * (640320 ** (3 * k))
        pi += Decimal(t) / Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1 / pi
    print(round(pi, 10))  # Print the result when done


def main():
    # cal_thread = threading.Thread(target=cal, args=(99999,))
    # cal_thread.start()
    # cal_thread.join()

    path = Path('./million_digits_pi.txt')
    # contents = path.read_text().strip()
    # print(contents)

    # Read line by line
    contents = path.read_text()
    lines = contents.splitlines()

    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    print(pi_string[:52])
    print(f"This is pi to {len(pi_string) - 2} decimal places.")

    # Ask the user for their birthday in mmddyy form
    # Tell them if their birdthday appears in the first n digits of pi

    while True:
        try:
            user_bday = input("Enter your birthday in mmddyy format: ")
            if user_bday == 'exit':
                break
            if not user_bday.isdigit():
                raise ValueError
        except ValueError:
            print(f"Incorrect form, try again")
            continue
        if user_bday in pi_string:
            value = len(pi_string)-2
            print(f"Your birthday is in the first {value:,} digits of pi")
        else:
            print(f"Sorry, your birthday is not in the first {len(pi_string)-2} digits of pi")

if __name__ == '__main__':
    main()
