# student = {
#     "name": "Nish Mandal",
#     "age": 36,
#     "courses":["C#", "Java"]
# }
#
# print(student["name"])
#
# student["phone"] = "+55555555"
# student["age"] =37
#
# print(student)
#
# del student["age"]
# print(student)
#
#
# print(student.keys())
# for key in student.keys():
#     print(key)
# print(student.values())
#
# for value in student.values():
#     print(value)
#
# print(student.values())
#
# for key, value in student.items(): # items return the KVP as a tuple
#     print(key)
#     print(value)
#
# # Checking for keys
#
# if "name" in student:
#     print("Name is present in the dictionary")

string = "The quick brown fox jumps over the lazy dog"
my_dict = {}

for character in string:
    if character not in my_dict:
        my_dict[character] = 1
    else:
        my_dict[character]+=1

print(my_dict)