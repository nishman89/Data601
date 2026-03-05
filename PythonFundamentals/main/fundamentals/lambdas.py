# lambda arguments: expression
#
# add = lambda x,y: x + y
# result= add(3,4)
# print(result)
# def is_even(num: int)-> bool:
#     return num % 2 == 0
#
#
# my_list = [1,2,3,4,5]
# even_list = []
# for n in my_list:
#     if is_even(n):
#         even_list.append(n)
# print(even_list)
#
# even_list_lambda = filter(is_even,my_list) #get info from it - we need to use a loop
# print(list(even_list_lambda))
# even_sum = sum(filter(is_even,my_list))
# print(even_sum)
#
# for num in even_list_lambda:
#     print(num)


my_list = [1,2,3,4,5]

even_list_lambda_sum = sum(filter(lambda x: x % 2 == 0, my_list))
print(even_list_lambda_sum)

squared = map(lambda x: x** 2, my_list)
print(list(squared))

students = [
    ("Abinash", 99), #x[1] = 99
    ("Dean", 92), #x[1] = 92
    ("Nish", 78) #x[1] = 78
]


sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# my_list_alt = [11,22,13,43,5]
# sorted_list = sorted(my_list_alt)
# print(sorted_list)


# 1. *Calculate Age in Dog Years
ages = [5, 10, 15, 20, 25]
dog_years = list(map(lambda x: x * 7, ages))
print(dog_years)

# 2. Even letters in a list of stirngs
fruit = ["apple", "banana", "cherry", "date", "fig", "grape"]
even_letters = list(filter(lambda x:  len(x) % 2 == 0, fruit))
print(even_letters)

# 3. Sort by Second Element
characters = [(1, 'Rick'), (3, 'Morty'), (2, 'Summer'), (4, 'Beth')]
sorted_characters = list(sorted(characters, key=lambda x: len(x[1])))
print(sorted_characters)
