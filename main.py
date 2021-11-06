# # List comprehension
# numbers = [1, 2, 3]
# # new_numbers = [new_item for item in list]
# new_numbers = [item+1 for item in numbers]
# print(new_numbers)

# name = "Nabil"
# letters = [letter for letter in name]
# print(letters)

# range_list = range(1, 5)
# double_rangle_list = [item*2 for item in range_list]
# print(double_rangle_list)

# double_rangle_list = [item*2 for item in range(1, 5)]
# print(double_rangle_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# uppercase_names = [name.upper() for name in names if len(name) >= 5]
# print(uppercase_names)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
# #Write your 1 line code 👇 below:
# squared_numbers = [number**2 for number in numbers]
# #Write your code 👆 above:
# print(squared_numbers)


# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
# # Only print even numbers from the list
# #Write your 1 line code 👇 below:
# result = [num for num in numbers if num % 2 == 0]
# #Write your code 👆 above:
# print(result)


# Create a list of overlapping numbers in file1.txt and file2.txt
with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

overlapping_data = [int(item.strip('\n')) for item in file1_data if item in file2_data]
print(overlapping_data)