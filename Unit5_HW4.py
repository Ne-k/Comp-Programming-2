class_data_dict = {
    "Billy": {
        "tests": {
            1: 95,
            2: 90,
            3: 87
        }
    },
    "Samantha": {
        "tests": {
            1: 85,
            2: 88,
            3: 91
        }
    },
    "John": {
        "tests": {
            1: 78,
            2: 82,
            3: 79
        }
    },
    "Emily": {
        "tests": {
            1: 92,
            2: 95,
            3: 96
        }
    },
    "Michael": {
        "tests": {
            1: 88,
            2: 84,
            3: 90
        }
    }
}

for student, tests in class_data_dict.items():
    for test_num, score in tests["tests"].items():
        if score > 80:
            print(student, test_num, score)

highest_grades = [[None, None, i, 0] for i in range(1, 4)]
for student, tests in class_data_dict.items():
    for test_num, score in tests["tests"].items():
        if score > highest_grades[test_num - 1][3]:
            highest_grades[test_num - 1] = [student, test_num, score]


# Add a new student named Parker Letmate with test scores of 98, 94, and 99.
class_data_dict["Parker"] = {
    "tests": {
        1: 98,
        2: 94,
        3: 99
    }
}

# Add a new student named Parker Letmate with test scores of 98, 94, and 99.
