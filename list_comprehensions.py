'''
Name: Cardin Nguyen
Date: 2/29/24
Lesson: List Comprehensions

'''
import math

# filling up a list with 1-5
nums = []
for i in range(1, 6):
    nums.append(i)
print(nums)

# New way - list comprehensions
nums = [i for i in range(1, 6)]
print(nums)

# use list comprehension to make the list [2,4,6,8,10] in two different ways
nums = [i * 2 for i in range(1, 6)]
print(nums)

nums = [i for i in range(2, 12, 2)]
print(nums)

# Make the list [0,1,0,1,0,1]
nums = [i % 2 for i in range(6)]
print(nums)

nums = [round(abs(math.sin(i * math.pi / 2))) for i in range(6)]
print(nums)

# make the list [True, False, True, False, True, False]
nums = [i % 2 == 0 for i in range(6)]
print(nums)

string_list = [str(i) for i in range(1, 6)]
print(string_list)

# ake the list [1,4,7,10,13]

# method 1
nums = [i * 3 + 1 for i in range(5)]
print(nums)
# method 2
nums = [i for i in range(1, 14, 3)]
print(nums)
# method 3
nums = [i for i in range(1, 16) if i % 3 == 1]
print(nums)

# make the list [0,7,16,27,40, 55], not linear, is in the form x^2 + b*x
nums = [n ** 2 + 6 * n for n in range(6)]
print(nums)

# extra content - boolean expressions inside of list comprehenstions
# Format: [<expression> for item in list if <condition>]
# Same as
'''
for item in list: 
    if conditional: 
        expression
        
'''
list_one = [22, 13, 45, 50, 98, 71, 44, 1]
evens = [x for x in list_one if x % 2 == 0]
# how to use a elif in a list comprehension
fun_list = [x if x % 2 == 0 else 2 * x for x in list_one]
print(fun_list)
print(evens)
