# my_list = [char for char in 'hello']

# print(my_list)

# my_list = []

# for char in 'hello':
#     my_list.append(char)

# print(my_list)

#The two methods above serve the same function.
#The top one is referred to as a list comprehension.
#The bottom is referred to as a for loop.

# my_list2 = [num*2 for num in range(100)]
# print(my_list2)

# my_list3 = [num*2 for num in range(100)
#             if num % 2 == 0]

# print(my_list3)

#generate list of even numbers
# my_list = []

# for item in range(100):
#     if item % 2 == 0:
#         my_list.append(item)

# print(my_list)

my_list = []

for item in range(100):

    my_list.append(item)

print(my_list)