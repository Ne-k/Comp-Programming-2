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

# Print the first name, last name, and test # for all tests above 80 Iterate over each student
for student, tests in class_data_dict.items():
    scores = [score for test_num, score in tests["tests"].items()]
    print(f'{student.title()} in tests 1,2,3 got a score of {",".join(map(str, scores))}')


# Print the first and last name of the student with the highest grade for each test
highest_grades_per_student = {}

for student, tests in class_data_dict.items():
    highest_grade = 0
    for test_num, score in tests["tests"].items():
        if score > highest_grade:
            highest_grade = score
    highest_grades_per_student[student] = highest_grade

for student, highest_grade in highest_grades_per_student.items():
    print(f"The highest grade for {student} is {highest_grade}")

# Add a new student named Parker Letmate with test scores of 98, 94, and 99.
class_data_dict["Parker"] = {
    "tests": {
        1: 98,
        2: 94,
        3: 99
    }
}