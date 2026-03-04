# Tuples are similar to lists in Python BUT they are IMMUTABLE ()

# my_tuple = (2,3,4,3)
# print(my_tuple[0])

# As lists can containt any data types, we can add tuples to lists (and vice versa)

students = [
    ("Paul", 85),
    ("Ringo", 78),
    ("John", 92),
    ("George",88)
]

pauls_score = students[0][1]
print(pauls_score)

student4_name = students[3][0]
print(student4_name)

# unpacking - we can use tuple unpacking to assign multiple variables a value

liam, *noel = ("singer", "writer","bassist")
print(liam)
print(noel)

# Joining tuples together
gallaghers = ("Noel", "Liam")
others = ("Andy", "Paul", "Tony")
oasis = gallaghers + others
print(oasis)

my_tuple = (33,4,55,55)
my_list = [33,4,55]
my_list[0] =3

print(my_tuple.index(33))
print(my_tuple.count(55))

