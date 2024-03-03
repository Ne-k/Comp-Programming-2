def main():
    class_data = [
        ["First Name", "Last Name", "Test #", "Grade"],
        ["Billy", "Bot", 1, 95],
        ["Samantha", "Smith", 1, 85],
        ["John", "Doe", 1, 78],
        ["Emily", "Jones", 1, 92],
        ["Michael", "Brown", 1, 88],
        ["Billy", "Bot", 2, 90],
        ["Samantha", "Smith", 2, 88],
        ["John", "Doe", 2, 82],
        ["Emily", "Jones", 2, 95],
        ["Michael", "Brown", 2, 84],
        ["Billy", "Bot", 3, 87],
        ["Samantha", "Smith", 3, 91],
        ["John", "Doe", 3, 79],
        ["Emily", "Jones", 3, 96],
        ["Michael", "Brown", 3, 90]
    ]
    print(class_data)

    highest_grades = [[None, None, i, 0] for i in range(1, 4)]

    # Print the first name, last name, and test # for all tests above 80
    for student in class_data[1:]:
        first_name, last_name, test_number, grade = student
        if grade > highest_grades[test_number - 1][3]:
            highest_grades[test_number - 1] = [first_name, last_name, test_number, grade]

# Print the first and last name of the student with the highest grade for each test
    for first_name, last_name, test_number, grade in highest_grades:
        print(f"Test #{test_number}: {first_name} {last_name} with a grade of {grade}")

# Add a new student named Parker Letmate with test scores of 98, 94, and 99.
    class_data.append(["Parker", "Letmate", 1, 98])
    class_data.append(["Parker", "Letmate", 2, 94])
    class_data.append(["Parker", "Letmate", 3, 99])
    print(class_data)
    # new_student_data = [["Parker", "Letmate", test_num, score] for test_num, score in zip(range(1, 4), [98, 94, 99])]
    # class_data += new_student_data
    # print(class_data)

# Then repeat the above steps


if __name__ == "__main__":
    main()