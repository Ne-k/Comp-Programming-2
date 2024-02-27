'''
Name: Cardin Nguyen
Date: 2/27/24
Topic: Unit 4 - lists, tuples, list methods
'''


my_list = ["taco","salad","pot roast","cake"]
my_list[3] = "ice cream" # this is valid
my_tuple = ("taco","salad","pot roast","cake")
print(my_tuple)
# my_tuple[3] = "ice cream" # not valid

#                   0      1     2       3   list indices
#                  0 1    0 1   0 1    0   1 tuple indices
list_of_points = [(1,2),(-4,5),(7,4),(12,-12)]
print(list_of_points[2][0]) # prints 7
print(list_of_points[2:]) # prints [(7,4),(12,-12)]
print(list_of_points[1]) # (-4,5)
# change (7,4) to (-7,4)
# list_of_points[2][0] = -7 is not valid
list_of_points[2] = (-7,4)
print(list_of_points)

tuple_of_lists = ([1,2],[3,4],[5,6])
print(tuple_of_lists[0][1]) # 2
tuple_of_lists[2][0] = -5 #valid
# tuple_of_lists[2] = [-5,6] #invalid
big_tuple = ([1,2,3,4,5],[6,7,8])
# print 3,4,5
print(big_tuple[0][2:])