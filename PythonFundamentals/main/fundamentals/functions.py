import math

# number = 3.7
# rounded_number = math.floor(number)
# print(rounded_number)

# def add(num1, num2):
#     return num1 + num2
#
# def greet(name="Erik", greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# print(greet())
# print(greet(name="Nish"))
# print(greet(name="Nish", greeting="Goodbye"))
# result = add("Nish ","Mandal")
# print(result)

# nums = [432, 34,32,342,44,9]
# sorted_nums = sorted(nums, reverse=True)
# print(sorted_nums)

## Type hints (aka annotations)

# def add_numbers(num1: int, num2: int) -> int:
#     return num1 + num2
#
# result = add_numbers(2, 1)
#
# print(result)

## args and kwargs

# def print_names(*names):
#     for name in names:
#         print(name)
#
# print_names("Fraz", "Atanaska", "Alessandra")
#


# def greet(greeting, *names):
#     for name in names:
#         print(f"{greeting}, {name}")
#
# greet("Hello", "Hiyab", "Ramim", 1)

# ** kwargs - variable keyword arguments

def print_info(**info):

    for key, value in info.items():
        print(f"{key}: {value}")
    print(info)
    print(type(info))

print_info(name="Nish",age=36,city="Birmingham")


def add_trainees(*trainees, **academy_details):
    print("Academy Details:")
    for key, value in academy_details.items():
        print(f"{key}: {value}")
    print("Trainees:")
    for trainee in trainees:
        print(f"- {trainee}")

# Sample call
add_trainees(
    "John", "Paul", "George", "Ringo",
    location="London",
    cohort="June 2024",
    trainer="Nish"
)