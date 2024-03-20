from pathlib import Path

print("Cardin Nguyen")


def main():
    # Problem 1
    contents = Path('my_learning.txt').read_text()

    for line in contents.splitlines():
        print(line)

    # Problem 2
    for line in contents.splitlines():
        print(line.replace('Python', 'C'))


if __name__ == "__main__":
    main()
